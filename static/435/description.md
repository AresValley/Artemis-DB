STP403 is a bus PIT system used to update digital displays at bus stops. STP403 was developed by French companies INEO and CESATEC. STP403 sends data such as arrival time of buses.

Also seen in France at 164 MHz, and at 469 MHz close to an MPT1327 control channel used for bus transport.

After a little reverse-engineering, it seems this is a downlink channel used by Keolis to communicate with bus displays in France.

It serves multiples purposes :

- update various informations used by the bus display firmware : informations of the lines (bus number, name of destination), formatting strings... This is done once a day, around 3 AM.
- send the time
- update the arrival time of buses at each stop.
Remark : the layer 3 protocol is used in other cities over TETRA to send the same informations.

# Modulation
The modulation is FM modulated FFSK at 1200 bit/s : the mark (1) and space (0) frequencies are 1200/1800 Hz.

# Demodulation
Since it's FFSK, you can get the bit stream by multiplying the signal with a version of itself delayed by one period, and applying a low-pass filter :

mpg123 -r 48000 -0 -w resampled.wav Fouine91_MPT1327-Like.mp3

sox --norm --combine multiply resampled.wav "|sox resampled.wav -p delay 40s" out.wav lowpass 1200

Here is the resulting wav file :

File:Mpt1327-like-bits.wav

You can open it in Audacity and read the decoded bits (1 bit every 40 frames).

Bit decoding
The binary data is encoded like a serial port with parameters 1200Hz/8-N-1.

A byte is encoded by a starting bit (0) followed by the bits lsb-first, and a stop bit (1). When there is no data to send, only 1s are transmitted.