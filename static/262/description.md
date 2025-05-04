JT9 is a 9-FSK mode for making contacts (QSO's) under extreme weak-signal conditions. It is part of the WSJT-X software.

JT9 has eight submodes, JT9A to JT9H, with different tone spacings. The normal "slow" operating mode is primarily designed for weak-signal communications on HF and lower bands. 60-second transmit/receive slots are used. Transmission takes 49 seconds and the remaining 11 seconds are reserved for decoding and timing inaccuracies. Compared to JT65, the most common submode JT9A is about 1 dB more sensitive while using less than 10% of the bandwidth.

Submodes JT9E to JT9H can also be operated in fast mode which is designed for meteor scatter and other propagation modes with short openings. In this mode, the messages are sent fast and repeated many times during the transmission window. The fast mode uses 5, 10, 15 or 30 second transmit/receive slots.

# JT9 Slow Submodes

| Submode | Tone spacing | Bandwidth | Minimum SNR for decoding |
| :------ | :----------- | :-------- | :----------------------- |
| JT9A    | 1.74 Hz      | 15.6 Hz   | -26 dB                   |
| JT9B    | 3.47 Hz      | 29.5 Hz   | -26 dB                   |
| JT9C    | 6.94 Hz      | 57.3 Hz   | -25 dB                   |
| JT9D    | 13.9 Hz      | 113 Hz    | -24 dB                   |
| JT9E    | 27.8 Hz      | 224 Hz    | -23 dB                   |
| JT9F    | 55.6 Hz      | 446 Hz    | -22 dB                   |
| JT9G    | 111 Hz       | 891 Hz    | -21 dB                   |
| JT9H    | 222 Hz       | 1780 Hz   | -20 dB                   |

The fast submodes use slightly more bandwidth than their slow counterparts. Duration of one cycle decreases with wider tone spacing - one JT9E fast cycle takes 3.4 seconds but one JT9H fast cycle takes only 0.425 seconds. These cycles are repeated over the transmit window.
