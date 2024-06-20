KG-STV is an image transmission mode developed by JJ0OBZ in Japan. The mode transmits one 16x16 compressed jpeg block at a time, so that partial transmissions can still reveal the image with missing holes. You can see each block as it's received being reconstructed. The software allows the receiver to send a repeat request in case there are received blocks that have errors. In addition to images, users can send and receive short text messages to each other with this mode.

KG-STV has two modulation modes. MSK (Minimum Shift-Keying) and 4LFSK (4-Level Frequency-Shift Keying). The 4LFSK mode transmits twice as fast as MSK, but is more prone to being affected significantly by propagation effects. Most transmissions are done in MSK mode. Each mode has a choice of convolution encoding or no encoding. The error correction used is Viterbi Encoding (NASA standard K=7 mode)

MSK uses two frequencies, 1800 Hz for 1 and 1200 Hz for 0. For 4L-FSK, '00' 1200 Hz; '01' 1400 Hz; '10' 1600 Hz; '11' 1800 Hz.

All signals operate at 1200 Bd, and occupy a bandwidth of between 500 Hz to 2500 Hz, depending on signal quality.