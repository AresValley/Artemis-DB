Method for transmitting digital images via radio, similar to WinDRM or KG-STV.

A number of problems experienced with the OFDM NBTV system led to the development of this Digital NBTV mode. First, the OFDM signal is very difficult to tune, especially for beginners, and requires extreme transceiver accuracy and stability. Then in addition, the pictures tend to be noisy and individual frames can be marred by multi-path effects, especially when used on the lower bands.

The approach taken for the Digital NBTV mode is completely different, in many senses:
   It uses separate programs for modem and codec in the transmitter and receiver
   TCP/IP communications is used between program modules
   The modem is high speed single-tone PSK, similar to NATO's STANAG 4285
   An equalizer system is included to compensate for ionospheric path variation
   Wavelet image compression and forward error correction are used
   It provides completely noise-free and error-free image reception, even on 80m

The transmission consists of a stream of packets, each containing data for a small number of image lines. The amount of data in the packet varies according to the image complexity, the compression level and the level of forward error correction included, but the packet size is constant at 256 symbols plus an 80 symbol header.

Modulation Digital NBTV uses a modulation technique which is widely used by high speed HF radio modems. A single 1500Hz phase modulated carrier is used to send both packet sync and payload. Using BPSK modulation, a pseudo-random binary (PN) sequence starts each packet, and is used to identify an exact point in the transmission from which the data can be synchronized. A cross-correlator is used in the receiver to locate the one point in the whole message where the sequence matches up with the local copy of the sequence. The cross-correlator works with a known pattern to look for, and is a very powerful and sensitive tool.

These radio modems use the PN sequence technique to enable complex high speed data to be decoded accurately - the ranging information determined from the cross-correlator is used to correct the received data timing to reduce errors induced by the ionosphere, using a signal processing device called an 'equalizer'. The equalizer also corrects for Doppler errors which affect carrier phase, making the use of 8-PSK practical.

Digital NBTV uses a 31-bit PN sequence borrowed from STANAG 4285, with one chance in two billion of a perfect score being caused by noise. It uses 80 symbols (modulation time slots) to send this sequence about 2.5 times. Each packet is contained in a 336 symbol frame. 256 symbols are used for image data and FEC information. Since 4-PSK is used for the data, each packet could contain 512 bits of image data, or 3047 bps raw data rate. The data symbols are scrambled in an 8-PSK pattern to improve resistance to selective fades.

Like the STANAG 4285 system, single-tone PSK Digital NBTV can also operate at 2400 baud, using a sub-carrier frequency of 1800Hz. The corresponding bandwidth (just under 3kHz)
is too much for most HF transceivers, but quite suitable for VHF, and gives a worthwhile speed improvement. However, to fit the signal into a normal amateur transceiver IF,
it is usually operated at 2000 baud using a 1500Hz sub-carrier.
Modem The modem section of the transmitter or receiver converts digital data into PSK audio for the transmitter, or received audio into digital data, respectively. The receiver modem also has to manage sync and equalization.

Each transmitted packet commences with a BPSK pseudo-random (PN) sequence (same sequence as STANAG 4285), which is used to synchronize the receiver timing with the start of the packet, and also serves as a measuring point for the receiver equalizer software which measures and compensates for frequency offset and drift, and other code which compensates for timing errors. Detection of the PN sequence is achieved using a cross-correlator. This technique is extremely sensitive, so no matter how weak the signal is, packet synchronization is secure.

The packet data payload is transmitted as 4-PSK, to ensure a high data rate. There are nearly six packets per second, using a 2000 baud modem.

Codec Because a digital system is inherently much less bandwidth-efficient than an analog one, in order to achieve even reasonable frame rate, considerable effort must be made to reduce the amount of data transmitted to a minimum. Two coding and decoding (codec) strategies are used: a pixel interpolation technique, and a wavelet compression technique.

The Digital NBTV system offers some flexibility of image size:

- 48 x 48 pixels zoomed 
- 64 x 64 pixels 
- 96 x 96 pixels zoomed 
- 128 x 128 pixels 
- 256 x 256 pixels
- 
The 48 x 48 and 96 x 96 images are zoomed-in versions of the next size up.

Interpolation All transmitted pictures are square (1:1) in pixel ratio, but due to interpolation techniques used, are generated from 4:3 ratio images, and result in received images that are again conventional 4:3 landscape format. This gives a built-in compression to 3/4 of the original data. The images are always displayed the same size, but of course vary in resolution. The image at the top of this page shows the receiver image view pane, with a 64 x 64 pixel image displayed. The image was received over a 500km path on 80m at night, and is completely noise-free.

Compression Standard image compression algorithms such as JPEG, JP2 and MPEG are designed for significantly higher image resolution than those used here, and do not work well on such small (low resolution) images. A special series of 'Wavelet' compression algorithms was therefore developed, tuned for small images. The wavelet transforms to work at their highest efficiency when operating with images that are 2n (a power of two) wide and high, which is accomodated by the interpolation to 1:1 aspect ratio and the choice of image sizes. Three alternative transforms are offered:

- Haar 
- Daubechies D4 
- Cohen-Daubechies-Feaveau 9/7 CDF97 (default) 

The last of these is the default and generally gives the best images. Haar is useful for images with high contrast, such as text. Because the transmitter software shows the effect of image size and compression in real time, it is easy to select the most suitable for any image. The CDF97 wavelet is used in the JPEG2000 image compression system, but has been adapted for this particular application. Wavelet compression, as with any image compression system, merely reduces the number of bits per pixel and requires additional 'packing' of the bits to achieve the high compression ratios. Arithmetic coding is used to compress the data.