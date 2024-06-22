A high-speed digital link used by METOP weather satellites for direct data dissemination.

The METOP series of satellites transmit high resolution pictures from AVHRR and data from several other instruments over an AHRPT link.

Due to a much larger instrument payload than NOAA POES satellites, a faster method of disseminating data from the satellites had to be devised. BPSK was replaced by QPSK and to ensure correct decoding, forward error correction (FEC) was added too. As a result, the data rate passed from 664.5 kbit/s of POES HRPT to 3.5 Mbit/s, over 5 times faster, not including overhead of FEC which brings the total data rate to 4.7 Mbit/s.

# Data transmitted
- 6 channels from AVHRR radiometer, of which 5 transmitted at the same time (satellite switches between channel 3A and 3B depending on light conditions)
- Image and data from IASI interferometer
- Data from ASCAT scatterometer
- 15 channels from AMSU-A sounder
- 20 channels from HIRS sounder (Not available on METOP C)
- 5 channels from MHS
- Data from GOME
- Data from ARGOS-A DCS data collection system
- Data from SEM (Space Environment Monitor)
- Spacecraft RTC (Real Time Clock)
- Spacecraft telemetry and monitoring (TLM)
- Administration messages and satellite status

# Data structure
Data are distributed as a stream containing Channel Access Data Units (CADUs), which require further processing to produce Metop L0 products. The stream holds multiplexed data from all Metop instruments, as well as spacecraft telemetry and administrative messages. In addition to being time ordered, frame synched and randomized, CADU’s also hold Reed-Solomon decoding information and quality information.

# Signal characteristics
- Right-hand circular polarization
- QPSK modulation
- 6 MHz bandwidth
- Data rate 3.5 Mbps (4.666667 Mbps including FEC)
- Viterbi and Reed-Solomon FEC
- Transmit power 15 watts
- 1701.3 MHz prime transmitter, 1707 MHz backup transmitter