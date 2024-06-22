Iranian Navy QPSK Modem is a QPSK mode used by the Iranian Navy. It has gone through several versions. The current version (2015) is V2 and supports speeds of 468 Bd, 936 Bd, and 1872 Bd.

# Original QPSK 207 Bd Modem
The original Iranian Navy QPSK Modem only supported one baudrate, 207 Bd. The data is transmitted in packets, and each transmission starts with an unmodulated pre-carrier of 2000 Hz. 100 ms before data transmission, the carrier has a phase jump of 180 degrees. At the end of each transmission two tones are sent at 1000Hz, first one 100ms long and the second one 110 ms long right after the first. Total length of this two-tone end of message transmission is ~250 ms.

# V1 Adaptive Modem
V1 Adaptive Modem is a further development of the original QPSK modem. V1 supports four different speeds: 207 Bd, 414 Bd, 828 Bd, and 1656 Bd and all are QPSK modulated. Like the original QPSK modem, each packet is sent with a pre-carrier burst.

- 207 Bd (414 bps), 300 Hz Bandwidth
- 414 Bd (828 bps), ~620 Hz Bandwidth (approx)
- 828 Bd (1656 bps), ~1250 Hz Bandwidth (approx)
- 1656 Bd (3312 bps), ~2520 Hz Bandwidth (approx)

# V2 Adaptive Modem
V2 is an upgrade of the V1 Adaptive modem, replacing V1 and using different speeds of 468 Bd, 936 Bd, and 1872 Bd. All use QPSK modulation and like the original QPSK modem, each packet is sent with a pre-carrier burst.

- 468 Bd (936 bps), 700 Hz Bandwidth: 1500 ms long packets are sent with a 430 ms long pre-carrier burst.

# Additional Speeds:
- 936 Bd (1872 bps), ~1420 Hz Bandwidth (approx)
- 1872 Bd (3744 bps), ~2850 Hz Bandwidth (approx)