Globe Wireless's HF Network was a system of 24 stations around the globe offering data services to large cargo vessels. Since 2014, GW has discontinued their HF network, and the company has been purchased by Inmarsat, which is focusing primarily on satellite networks. Globe Wireless was a provider of HF and satellite email and data services to the shipping industry.

The remnants of the Globe Wireless network is scattered all over the world. Parts of the HF network are now used by Swisscom, including its own Bern Radio in Switzerland. Swisscom solely uses PACTOR III with huffman compression for data transfer.

# Modes
There are a number of modes that were used with Globe Wireless, including their own proprietary ODFM DQPSK modes used for data transmission.

## GW-FSK:
GW-FSK is Globe Wireless's "Idle Channel" or "Free Signal" marker. It is continuously broadcasted from shore stations out to sea, and ships use them to know which channel has the best signal quality if they want to establish a connection. Has a bandwidth of 400Hz and operates as Simplex ARQ.

## GW-PSK:
GW-PSK is also used in place of FSK depending on the propagation situation. Also operated with 400Hz bandwidth and Simplex ARQ.

## GW-OFDM (Orthogonal Frequency-Division Multiplexing):
GW-OFDM is the main data mode for Globe Wireless. GW-OFDM uses DQPSK with OFDM modulation and features adaptive speed with modes from 12 to 32 sub-carriers with 62.5Hz sub-carrier spacing. They are chosen dynamically based on the noise level and propagation ability. The bandwidth range for OFDM is from 700-2700 Hz.

## GW-CLOVER-400 with SITOR:
Before GW-OFDM and the FSK/PSK modes, Globe Wireless used SITOR as the "Idle Channel", as SITOR was more ubiquitous at the time among the maritime industry. To transmit data, Globe Wireless partnered with HAL Communications to develop a special proprietary mode, CLOVER-400, that could be used for shore to ship communications. It was a special variant of CLOVER that only occupied 400Hz of bandwidth, which met FCC requirements (FCC Part 80.211 (f) Limits). The shore stations would transmit first in SITOR. If they were able to identify a ship that was CLOVER-400 compatible, they would switch to CLOVER to transmit the data.