Coherent BPSK, also known as C-BPSK, was an experimental amateur mode developed by Bill DeCarle VE2IQ.

Coherent BPSK is actually DBPSK (Differential BPSK) with a user-defined baud rate. The length of each symbol can be anywhere between 5 ms to 1000 ms (200 Bd to 1 Bd) in 5 ms increments. Typically, 40 Bd (25MS, used in HF band) and 1 Bd (1000MS, used in 130 kHz experimenters band). are used.

10 bits make an ASCII character (7 data bits, one start bit, two stop bits). For successful reception, 1 Hz frequency resolution is required to successfully receive Coherent PSK.

In addition to baud rates, there are optional FEC encoding modes to improve robustness. These are named ET1 and ET2, ET short for Extended Table. For ET1, instead of 10 bits per ASCII character, there's 16 bits, and for ET2, 27 bits are used.