JORN is an Australian over-the-horizon radar system. It transmits an FMCW signal in bursts, and each burst has an intro tone. Sweep rates can vary over a wide range. The most common bandwidth is 10 kHz but other bandwidths such as 3 kHz or 15 kHz may be used. The sounder modes (see below) use many different bandwidths. Transmission frequency can vary from 5.7 MHz to 33 MHz or even lower or higher.
The intro tone can be very short and plain, or it can be slightly longer and have noticeable modulation. It is not known why different intro tones are used. The radar can also transmit without an intro tone, but it's uncommon, see the video example below. The purpose of the intro tone has not been confirmed, but according to a post in the UDXF group, it is used to check impedance matching between the transmitters and the antennas. If impedance matching is not correct, transmission would be aborted.
JORN's OTH network is comprised of three radar sites. One at Alice Springs (1RSU), the first OTH to be built in Australia, and two other ones at Laverton and Longreach.
JORN can be confused with the Relocatable Over-the-Horizon Radar (ROTHR) of USA, but can be usually differentiated by its different bandwidth and different intro tone. The waterfall appearance of HFDL also resembles JORN but the former can be differentiated by its narrow bandwidth and entirely different sound when demodulated.
There may be a Chinese OTH radar that can use a similar transmission mode as JORN.  It may be difficult to tell that and JORN apart.

# Sounder mode
The purpose of this mode has not been confirmed but it may be used for ionospheric sounding to check ionospheric conditions so that optimal frequency can be chosen for the main radar transmission.
The sounder mode typically uses slow sweep rates of less than 10 Hz and bandwidth from 3 kHz up to 50...60 kHz. Either 64 or 128 sweeps are usually transmitted. Transmissions often happen on or near integer MHz frequencies, and after one transmission is complete, frequency is typically changed by 1 MHz downwards or sometimes upwards. Unlike some other OTH radars, this sounder mode often seems to avoid frequencies that are in use. This behavior is seen when the sounder chooses a frequency that is slightly above or below the expected integer MHz value.

# 16x64 sounder mode
The 16x64 sounder is a special mode used by JORN. In this mode, the radar transmits 16 bursts, each with 64 FMCW sweeps, with sweep rate decreasing after each burst. Like the basic sounder mode, this mode also typically hops in 1 MHz steps downwards. Bandwidth of this mode is usually 3 kHz.

The purpose of the 16x64 sounder mode is not known but it has been suggested that it's used to check ionospheric conditions. It has also been called "searchlight mode".

A 14-burst variant with pauses between bursts and changes in sweep count has been observed in 2024.