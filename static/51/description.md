Automatic Picture Transmission (APT), also known as NOAA-GEOSAT, is an analog image transmission mode used to by the NOAA weather satellites and formerly some Russian weather satellites to transmit satellite weather photos. Currently only 3 active NOAA satellites transmit APT images.

- **NOAA 15** - 137.620 MHz
- **NOAA 18** - 137.9125 MHz
- **NOAA 19** - 137.100 MHz

# Structure
The broadcast transmission is composed of two image channels, telemetry information, and synchronization data, with the image channels typically referred to as Video A and Video B. All this data is transmitted as a horizontal scan line. A complete line is 2080 pixels long, with each image using 909 pixels and the remainder going to the telemetry and synchronization. Lines are transmitted at 2 per second, which equates to a 4160 words per second, or 4160 baud.

| Name        | Length in pixels | Description                                                 |
|-------------|------------------|-------------------------------------------------------------|
| Sync A      | 39               | Bits 000011001100110011001100110011000000000                |
| Space A     | 47               |                                                             |
| Image A     | 909              | Image pixels, a higher amplitude results in a brighter pixel|
| Telemetry A | 45               |                                                             |
| Sync B      | 39               | Bits 000011100111001110011100111001110011100                |
| Space B     | 47               |                                                             |
| Image B     | 909              | Image pixels, a higher amplitude results in a brighter pixel|
| Telemetry B | 45               |                                                             |
| Total       | 2080 / 0.5 seconds |                                                           |

# Images
On NOAA POES system satellites, the two images are 4 km / pixel smoothed 8-bit images derived from two channels of the advanced very-high-resolution radiometer (AVHRR) sensor. The images are corrected for nearly constant geometric resolution prior to being broadcast; as such, the images are free of distortion caused by the curvature of the Earth.

Of the two images, one is typically long-wave infrared (10.8 micrometers) with the second switching between near-visible (0.86 micrometers) and mid-wave infrared (3.75 micrometers) depending on whether the ground is illuminated by sunlight. However, NOAA can configure the satellite to transmit any two of the AVHRR's image channels.

# Synchronization and telemetry
Included in the transmission are a series of synchronization pulses, minute markers, and telemetry information.

The synchronization information, transmitted at the start of each video channel, allows the receiving software to align its sampling with the baud rate of the signal, which can vary slightly over time. The minute markers are four lines of alternating black then white lines which repeat every 60 seconds (120 lines).

The telemetry section is composed of sixteen blocks, each 8 lines long, which are used as reference values to decode the image channels. The first eight blocks, called "wedges," begin at 1/8 max intensity and successively increase by 1/8 to full intensity in the eighth wedge, with the ninth being zero intensity. Blocks ten through fifteen each encode a calibration value for the sensor. The sixteenth block identifies which sensor channel was used for the preceding image channel by matching the intensity of one of the wedges one through six. Video channel A typically matches either wedge two or three, channel B matches wedge four.

The first fourteen blocks should be identical for both channels. The sixteen telemetry blocks repeat every 128 lines, and these 128 lines are referred to as a frame.

# Broadcast signal
The signal itself is a 256-level amplitude modulated 2400Hz subcarrier, which is then frequency modulated onto the 137 MHz-band RF carrier. Maximum subcarrier modulation is 87% (±5%), and overall RF bandwidth is 34 kHz. On NOAA POES vehicles, the signal is broadcast at approximately 37dBm (5 watts) effective radiated power.
