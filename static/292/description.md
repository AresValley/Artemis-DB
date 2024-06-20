A variant of the NOAA HRPT signal, which has a different data structure and better low-signal handling characteristics.

The Meteor-M series of satellites transmit high resolution pictures from the MSU-MR (main radiometer) and additionally, data from MTVZA (a microwave sounding instrument) over an HRPT link. However, while the signal is still being PSK modulated, the data structure is different than the NOAA HRPT signal. This gives improved low-signal handling characteristics and makes the signal incompatible with NOAA HRPT decoders.

# Data transmitted
6 channels from MSU-MR radiometer
30 channels from MTVZA microwave sounder
DCP (Data Collection Platform) data
BIS-M (onboard information system) data
Spacecraft RTC (Real Time Clock)
Spacecraft telemetry

# Data structure
The signal is transmitted as a continuous sequence of phase-shift keyed Manchester encoding at 665.4 Kbit/s rate (transport rate is 1330.8 Kbit/s). Logical "1" is represented by symbol “10” (two bits), and logical "0" - by symbol "01" (two bits).

Data is packed into frames that are sent continuously one after another without intervals using time-division multiplexing. One frame consists of 1024 bytes. The most significant bit of each octet comes first.

# Signal characteristics
Right-hand circular polarization
Phase shift keying modulation
3 MHz bandwidth
Transmit power 5 watts