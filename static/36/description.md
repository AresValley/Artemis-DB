AHSC uses a randomly generated One-Time-Pad to secure communications between transmitter and receiver. Used for unscheduled transferring of data due to the architecture of the protocol / mode which makes decoding the message impossible if the transmission was not listened to from the beginning.

The transmission is split into two parts,

1. The data of the key
2. The data encrypted with the key

This means that if the receiver cannot receive the key or is late in recording / decoding the transmission, then the message cannot be decrypted and read.

Problems arise with this mode, however, since,

1. The real receiver must know the exact time in which the transmission will occur
2. If the imposter receiver also knows the exact time, the security of the communication can, if the right software is used, be cracked

# AHSC structure for transmission

| Period     | Purpose                                 | Correlation |
|------------|-----------------------------------------|-------------|
| 800ms      | Sync / Start                            | 400Hz (2.5ms) |
| 200-300ms  | Bit 0 [OTP]                             | 400Hz       |
| 400-500ms  | Bit 1 [OTP]                             | 400Hz       |
| 700ms      | End of OTP / Start of encrypted data    | 400Hz       |
| 200-300ms  | Bit 0 [REAL DATA]                       | 400Hz       |
| 400-500ms  | Bit 1 [REAL DATA]                       | 400Hz       |
| 800ms      | Sync / End                              | 400Hz       |
