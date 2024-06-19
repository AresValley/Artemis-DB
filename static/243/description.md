Inmarsat Aero is the protocol that's used to link ground stations with aircraft via Inmarsat's satellite link. This protocol carries digital voice, fax and low speed data such as ACARS and ADS-C.

# Characteristics
Inmarsat Aero in this article is the Forward TDM link from ground station to plane. The links use OBPSK or OQPSK modulated with 600, 1200, and 10500 bps signals. The 600 and 1200 bps links are part of Inmarsat's Classic Aero service which is due to be discontinued in 2018. the 10500 bps link is part of Inmarsat's Aero H and H+ services which are capable of transmitting both data (10.5 kbps) and digital voice (9.6 kbps).

The Inmarsat Aero system has both forward and return links, as well as digital voice channels.

## Forward (Ground Station to Plane)
- P-channel packet switched data TDM: 600 bps, 1200 bps A-BPSK (SDPSK), 10.5 kbps A-QPSK (OQPSK), convolutional FEC R = ½, k = 7
- Digital Voice circuit mode SCPC: 8.4 kbps A-QPSK (OQPSK), convolutional FEC R = 2/3, k = 7, 10.5 kbps A-QPSK (OQPSK), convolutional FEC R = ½, k = 7
## Return (Plane to Ground Station)
- R-channel slotted Aloha: 600 bps, 1200 bps A-BPSK (SDPSK), 4.8 kbps, 10.5 kbps A-QPSK (OQPSK), convolutional FEC R = ½, k = 7
- T-channel TDMA: 600 bps, 1200 bps A-BPSK (SDPSK), 10.5 kbps A-QPSK (OQPSK), convolutional FEC R = ½, k = 7
- Digital Voice circuit mode SCPC: 8.4 kbps A-QPSK (OQPSK), convolutional FEC R = 2/3, k = 7, 10.5 kbps A-QPSK (OQPSK), convolutional FEC R = ½, k = 7

## Inmarsat Forward TDM Link
- 600 bps: Aviation-BPSK (SDPSK or Pi/2-BPSK) modulation at 600 Bd. Spans 800 Hz of bandwidth.
- 1200 bps: Aviation-BPSK (SDPSK or Pi/2-BPSK) modulation at 1200 Bd. Span 1600 Hz of bandwidth.
- 10500 bps: Aviation-QPSK (OQPSK) modulation at 10500 Bd with convolutional FEC (Raw data throughput is 21000 bps, actual data rate with FEC is 10500 bps). This is part of Inmarsat's Aero H and H+ service.