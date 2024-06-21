STANAG 4285 is specified by the NATO (North Atlantic Treaty Organization) Military Agency for Standardization in "Characteristics of 1200 / 2400 / 3600 Bits per Second Single Tone Modulators / Demodulators for HF Radio Links". This data modem is very similar to MIL-STD-188-110 Serial.

# Characteristics
STANAG 4285 has a variety of speeds and interleaving. Speeds range from 75 bps up to 3600 bps. Two interleaving modes exist: Short and Long. Short interleaving allows for faster transmission at the cost of less robustness against effects of fading. Long interleaving extends the interleaving period so that messages take longer to send, but are more robust against fading from propagation effects.

BPSK, QPSK, and 8PSK are used with STANAG 4285 for specific speeds.

| Symbol Rate (baud) | User Data Rate (bps) | Bits per Symbol (Modulation) | FEC Encoding Rate | Supported Interleaving |
|--------------------|----------------------|------------------------------|-------------------|------------------------|
| 2400 Bd            | 2400 bps             | 3 (8-PSK)                    | 2/3               | Short or Long          |
| 2400 Bd            | 1200 bps             | 2 (QPSK)                     | 1/2               | Short or Long          |
| 2400 Bd            | 600 bps              | 1 (BPSK)                     | 1/2               | Short or Long          |
| 2400 Bd            | 300 bps              | 1 (BPSK)                     | 1/4               | Short or Long          |
| 2400 Bd            | 150 bps              | 1 (BPSK)                     | 1/8               | Short or Long          |
| 2400 Bd            | 75 bps               | 1 (BPSK)                     | 1/16              | Short or Long          |
| 2400 Bd            | 3600 bps             | 3 (8-PSK)                    | None              | None                   |
| 2400 Bd            | 2400 bps             | 2 (QPSK)                     | None              | None                   |
| 2400 Bd            | 1200 bps             | 1 (BPSK)                     | None              | None                   |
