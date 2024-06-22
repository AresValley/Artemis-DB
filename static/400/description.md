Motorola's Radio Data Link Access Procedure (RD-LAP) is a 1G protocol that was used in ARDIS/Motient and DataTAC Networks, and is still used in some MDT's, as well as gas companies, police departments, fire departments, financial companies, etc. Its use has been on the decline as faster cellular networks are adopted and P25 used for public safety.

This format was developed from MDT4800 (4.8kbps). RD-LAP has faster data rates (9.6kbps/19.2kbps). The majority of deployments used the 19.2kbps mode.

# Characteristics
When idling, the 9.6 kbps mode has an ACF of ~25 ms (40sym/s), where the 19.2 kbps mode has an ACF of ~12.5 ms (80sym/s). RD-LAP employs 4FSK modulation with frequency deviations at -3600 Hz, -1200 Hz, +1200 Hz, and +3600 Hz.

Maximum message size is 2,048 bytes. Max OTA size is 512. 4FSK with SRRC filtering rO = 0.2. 9.6 kbps in 12.5 kHz channels; 19.2 kbps in 25 kHz channels

Trellis coded modulation, r = 3/4.

32-bit interleaving protects 1.7 ms Cascaded CRCs with a final 32-bit CRC.