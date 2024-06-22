Motorola SECURENET is an obsolete voice encryption algorithm supported by Motorola MTS/MCS, Saber/Spectra, ASTRO XTL/XTS, and APX radios. Analog voice is digitized with CVSD at 12 kHz, and the bitstream is encrypted before transmission using 2-level FSK. There is minimal data transmitted alongside the CVSD voice to prevent interruptions in the voice audio, and due to the encryption algorithms' high-entropy output, SECURENET sounds like noise when tuned with a conventional FM receiver (with exception to the 6 kHz end-of-transmission tone). SECURENET decoded audio quality is poor due to the heavy lowpassing necessary with CVSD.

SECURENET can be used simplex, through a repeater (capable of passing unfiltered audio, or via reconstruction of the bitstream), or as a system voice option of a Motorola Type I or Type II trunked system. If MDC1200 pre-transmission PTT-ID/RAC is enabled on a secure channel, the radio will send the MDC in clear analog with any configured PL/DPL, drop PL/DPL after sending MDC1200, and proceed with SECURENET voice; this permits repeaters to use PL/DPL squelch and/or MDC Repeater Access Codes with secure voice.

# Algorithms
SECURENET supports several algorithms:

- DES 56-bit
- DVP 32-bit
- DES-XL 56-bit
- DVP-XL 96-bit
- DVI-XL (export version of DVP-XL)

XL algorithms use a different mode of clock synchronization to improve weak-signal reception; range is still poorer than clear analog voice.