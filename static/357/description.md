Packet, also known as FSK300, AFSK1200, BPSK300, QPSK600, BPSK1200, QPSK2400, AX.25 and IL2P, is a packet based protocol derived from X.25 and HDLC computer network protocols. Packet radio is a synchronous system in which data is transmitted in frames.

There are a number of variants that exist. For HF, FSK300, BPSK300 and QPSK600 are typically used, while at VHF and above, AFSK1200, BPSK1200, and QPSK2400 are typically used, though these are by no means set.

# Early History
Teletype machines were first developed in the 1930’s. As soon as they became available on the surplus market, hams began to use them on the air.

It wasn’t difficult to get started. You just needed to add a simple modem which was called a “terminal unit.”

It was not a efficient way to send text. First you would turn on the transmitter and it would sit there transmitting a 100% duty cycle carrier. The frequency would shift by 170 Hz in a certain pattern for each key pressed. There was no error detection so you would often see garbled messages.

It used a 5 bit code, commonly known as “baudot.” This allows only 32 different combinations, not enough for all letters and digits. Some of the codes were for control functions like carriage return, line feed, or bell. 26 of the codes were for letters. A “shift” control code was used to get digits or special characters instead of letters. If noise clobbered the shift or unshift code, you would see digits and special characters instead of letters or vice versa.

In 1978 Canadian hams began experimenting with a much different method of sending data over the air. Rather than keeping the transmitter on and sending one character at a time, it was sent in a short package (or “packet”).

Each transmission contained:

- Source address. (e.g. ham callsign)
- Destination address.
- Optional repeater addresses.
- Control / protocol bytes.
- Information part.
- Error checking (FCS, CRC).

With RTTY we had only a simple modem to convert between digital data and audio tones. When a key was pressed the corresponding code was sent immediately.

We now have some brains in between the terminal and modem to implement the protocol used over the air. This device is called a Terminal Node Controller (TNC).

The operator could take a while to compose a message but the complete message gets sent in a short burst.

This new approach offers many advantages.

- Rather than tying up a radio channel with one person typing a character at a time, a message could be sent in a short burst.
- Each packet contains information about where it came from and where it should be going.
- This allows many people to share one frequency.
- Error detection provided confidence that the data was not corrupted.
- The TNC would send acknowledgements when data was received correctly an perform retries when it doesn’t get thru the first time.
- Data was not limited to printable characters. You can send files such as JPEG images.

American ham radio operators had a disadvantage. The FCC did not allow the ASCII code to be used over ham radio until 1980. Special permission was required to perform the same type of experimentation as the Canadians.

The Vancouver Amateur Digital Communications Group made their design available as a bare printed circuit board. It was necessary to gather up all the other parts which discouraged most.

In 1983, Tucson Amateur Packet Radio (pronounced tapper) introduced their TNC-1 kit which made it a lot easier.

- All parts including modem and power supply.
- Documentation about 2 inches thick.
- $350 not including case.

They threw a lot of hardware at the problem. About 27 integrated circuits. This was later available as the Heathkit HD-4040.

The TNC-2 came along a couple years later. It was smaller and cheaper. MFJ and others produced products based on this design. For a while, everyone was churning out new TNC products.

Today, the 20th Century TNCs are pretty much extinct. You can now get better results and more features at lower cost by connecting your radio to the “soundcard” interface of a computer (e.g. Raspberry Pi) and using software, such as Dire Wolf, to decode the signals. You can also take advantage of an emerging breed of hardware DSP based KISS modems such as NinoTNC, which handle audio processing in hardware but defer bitstream processing to the host, which offer comparable levels of performance in hardware with the simplicity, reliability and compatibility of a physical modem.

## 300 Baud Packet
Legacy 300 baud packet uses FSK modulation with a 200Hz shift and a 300 Bd symbol rate (seldom seen with 600 Bd). On amateur frequencies above 30 MHz, higher speeds such as 1200 and 9600 baud are typically used. In the US, until 2024 it was illegal for hams to use speeds above 300 baud on frequencies below 28 MHz due to FCC regulations.

Today, BPSK (binary phase shift keying, 1 bit per symbol), and QPSK (quadrature phase shift keying, 2 bits per symbol) implementations are present and are entering wider use. BPSK300 is around 7dB more sensitive than FSK300, with QPSK600 around 3dB less sensitive than BPSK300 (although more sensitive to accurate frequency matching in current implementations).

In addition, IL2P is being used to augment AX.25, with a further variant IL2P+CRC adding a checksum to prevent AX.25 corruption.

## 1200 Baud Packet
Legacy 1200 baud packet, common to 2m APRS and "traditional" TNCs, uses FSK modulation with a 1000Hz shift and 1200 Bd symbol rate. There are a number of variations that exist of PACKET-1200, including a PSK-based satellite version, although these are rare in practice. 1200 baud AFSK packet can be seen particularly in the VHF band with indirect FM modulation, commonly with APRS. Required FM channel spacing is 12.5 kHz.

There now exist phase-shift keying 1200 baud modes: BPSK (1200bps) and QPSK (2400 bps). These are designed for use in an SSB voice channel although do offer a small advantage over AFSK in an FM voice channel.

IL2P and, preferentially, IL2P+CRC are now also seen on VHF/UHF, layered over any/all of the above modulations.

## PACKET-2400 and PACKET-4800
These are just some more variants of PACKET that operate on 2400Bd and 4800Bd.

## 9600 Baud Packet
The variant of 9600 baud packet which uses GFSK with a 4800 Hz and 9600 Bd symbol rate is known as G3RUH, after its inventor. This form of packet can be seen in the UHF-SHF band. Required FM channel spacing is 25kHz, and very flat audio response across the whole of the audio passband is required to transmit and decode it.

G3RUH packet can be combined with IL2P+CRC as above.