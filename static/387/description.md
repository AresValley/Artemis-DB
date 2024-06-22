Q15X25, also known as NEWQPSK, is an experimental amateur radio packet modem developed by Pawel Jalocha SP9VRC. Q15X25 is an OFDM QPSK implementation of the AX.25 Packet protocol used in PACKET. Q15X25 uses ARQ and FEC and performs just like a packet radio terminal.

# Characteristics
Q15X25 uses 15 QPSK subcarriers to transmit AX.25 data packets at between 1000 bps to 5000 bps. The original mode is set for 2500 bps with an additional mode for 3000 bps.

| Original 8000 Sample Rate Mode | Modified 9600 Sample Rate Mode |
|--------------------------------|-------------------------------|
| Data Rate: 2500 bps            | Data Rate: 3000 bps           |
| Carrier Spacing: 125 Hz        | Carrier Spacing: 150 Hz       |
| 83.33 Baud                     | 100 Baud                      |
| ~1950 Hz Bandwidth             | ~2350 Hz Bandwidth            |


Q15X25 is adjusted by five configuration parameters: bps, interleaving depth, FEC level, tune length, and sync length.

4 FEC modes are supported with Q15X25:

Original 2500 bps | Modified 3000 bps
- no FEC: 2500 bps | 3000 bps User Data Rate
- Simple (11/15) FEC: 1833.3 bps | 2200 bps User Data Rate
- BCH (7/15) FEC: 1166.7 bps | 1400 bps User Data Rate
- Walsh (5/15) FEC: 833.3 bps | 1000 bps User Data Rate