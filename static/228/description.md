Horus 4FSK is a binary frequency shift keyed transmission mode developed by the Project Horus amateur HAB (High-altitude balloon) group. This mode is similar to RTTY, although it is 4FSK instead of 2FSK. Horus 4FSK offers better SNR performance (~7dB) compared to most telemetry modes previously used for HAB telemetry. In addition, this mode transmits binary data at 100 baud instead of ASCII text (typically at 45 or 50 baud) like RTTY, making it more efficient per a given transmission period.

There are two versions of Horus 4FSK, v1 and v2. The only notable difference between them is the packet length being 22 bytes for v1, and 32 for v2. v1 is deprecated and no longer in use.

# Usage
Currently, Horus 4FSK is implemented in the RS41ng amateur radio firmware for the Vaisala RS-41 radiosonde, or by using Arduino hardware, and the RadioLib Arduino library, which works with many compatible radio modules. The RS41 radiosondes are balloon bourne instruments launched by various meteorological agencies around the world and are frequently hunted and recovered by enthusiasts. These sondes can then be re-flashed with the aforementioned firmware to enable usage of the hardware on the amateur radio bands.

Transmission intervals of Horus 4FSK are done in 3 second intervals.

# Decoding
Typically, transmissions are done in the 70cm amateur band, so you will need a radio that can recieve those frequencies and demodulate upper sideband. An RTL-SDR works best alongside the official software linked below.

A yagi-uda antenna would be the ideal choice for reception of a HAB flight, though due to the mode's performance in low SNR situations, a simple ground plane or vertical antenna may suffice depending on your range.
