SIGFOX is a IoT wireless network system utilizing ETSI's specification for Low Throughput Networks (LTN) and Ultra Narrow-Band (UNB) modulation.

The signal on this page is specifically the uplink between the IoT device and the central network station. This uplink employs BPSK modulation with ultra-narrowband technology and pseudo-random frequency hopping. Messages are very short. User has a maximum of 12 bytes of info available.

Each packet sent can have anywhere between 0-12 bytes of payload data, with a fixed frame of about 12 bytes that contains preamble, device id, and other metadata. In total, each packet sent has between 12-24 bytes, with some extra bits used for authentication parameters.

Each packet transmits in about 2 seconds, and each transmission from the IoT SIGFOX device to the main station consists of 3 of these packets transmitted on 3 pseudorandom frequencies, each transmission offset by about 45 ms. This is done as a redundancy measure.

SIGFOX currently has a tiered option plan for how many uplink transmissions you are allocated per day, as well as how many downlink transmissions you get from the main network station to your device (which is a different signal, using GFSK at 600 Bd).

- Platinum : 101 to 140 uplink messages + 4 downlink
- Gold : 51 to 100 uplink messages + 2 downlink
- Silver : 3 to 50 uplink messages + 1 downlink
- One : 1 to 2 uplink messages + no downlink
The early SIGFOX reference includes authentication and anti-replay protection, but not payload encryption.