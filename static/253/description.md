This is the L-band uplink/downlink for the Low Earth Orbit Iridium Satellite Constellation. This system is used for satellite based phone calls.

Iridium uses Differentially Encoded QPSK (DEQPSK) with an occupied bandwidth of 31.5 kHz. Each channel is spaced 41.667 kHz from each other as this is the minimum bandwidth needed for receivers to properly receive Iridium signals. Iridium uses both TDMA and FDMA in its transmissions.

The transmitter duty cycle allows for bursted transmission every 8.28 ms out of 90 ms, or 9.2%, at a rate of 50 kbps, with a symbol rate of 25000 bd.

For the voice communications, Iridium uses a 2.4 kbps Advanced Multi-Band Excitation (AMBE) vocoder developed by Digital Voice System Inc. (DVSI). This vocoder is tailored to the Iridium communication channel.

# Frequencies
The subscriber links are in L-band between 1616 MHz and 1626.5 MHz. There are 240 main channels between 1616 MHz and 1626 MHz. These are spaced 41.667 kHz from each other. The center frequency of each channel can be calculated by 1616 + 0.020833(2n - 1) MHz where (n = 1, ..., 240).

In addition, A 12-frequency access band is reserved for the simplex (ring alert and messaging) channels. These channels are located in a globally allocated 500 kHz band between 1626.0 MHz and 1626.5 MHz. They are:

| Channel Number | Center Frequency      | Allocation            |
|----------------|-----------------------|-----------------------|
| 1              | 1626.020833 MHz       | Guard Channel         |
| 2              | 1626.062500 MHz       | Guard Channel         |
| 3              | 1626.104167 MHz       | Quaternary Messaging  |
| 4              | 1626.145833 MHz       | Tertiary Messaging    |
| 5              | 1626.187500 MHz       | Guard Channel         |
| 6              | 1626.229167 MHz       | Guard Channel         |
| 7              | 1626.270833 MHz       | Ring Alert            |
| 8              | 1626.312500 MHz       | Guard Channel         |
| 9              | 1626.354167 MHz       | Guard Channel         |
| 10             | 1626.395833 MHz       | Secondary Messaging   |
| 11             | 1626.437500 MHz       | Primary Messaging     |
| 12             | 1626.479167 MHz       | Guard Channel         |
