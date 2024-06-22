Differential GPS (DGPS), also known as M823 DGPS and SC-104 DGPS, is a supplementary correction signal used by GPS receivers to increase the accuracy of GPS based positioning.

DGPS came in two formats, MSK and QPSK. QPSK was used in the higher frequency bands (1-3 MHz) but the vast majority of them have stopped broadcasting, while MSK based systems in the 284 kHz-325 kHz region are plentiful and expanding.

MSK DGPS uses Minimum Shift Keying (MSK) and has typical baud rates of 100 Bd or 200 Bd. The 100 Bd DGPS signal has about 150 Hz of bandwidth and 50 Hz shift, and the 200 Bd DGPS signals has about 250Hz of bandwidth with 100 Hz shift. There are some reports that suggest some DGPS stations run with 300 Bd and a shift of 200 Hz.

The QPSK DGPS used Quadrature Phase Shift Keying (QPSK) and had ~330 Bd with 450 Hz of bandwidth.

Note that DGPS has been officially discontinued in the US as of 30 June 2020. See the DGPS Discontinuance page on the US Coast Guard site for more information.

# Message Format
DGPS transmits data in frames. Each frame passes along a certain type of information. These are categorized by Message Types.

The most common message type transmitted is Type 9, which transmits satellite corrections for a few satellites, often up to three at at time. Although Message Type 1 is the standard type used to send satellite corrections for all satellites in view of the DGPS radio beacon, the Type 9 message is more resistant to noise and allows for faster resync for GPS receivers, so most DGPS beacons transmit Type 9 messages over Type 1.