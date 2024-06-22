Fast Simple QSO (FSQ) is an amateur radio digital modulation mode developed by Con Wassilieff ZL2AFP with Murray Greenman ZL1BPU in 2015. FSQ is used on HF on fixed frequency channels. VHF adaptions of FSQ are also supported using VHF FM. FSQ uses IFK+ and has efficient alphabet encoding as well as no need for syncing to receive. The FSQ modulation, coding and FSQCall protocol are publicly disclosed and described, and the software is open source.

FSQ is intended for fixed frequency (channelized) operation, with dedicated calling frequencies.

# Characteristics
FSQ is essentially a speeded-up version of the weak-signal mode WSQ2, introduced in 2013. It also uses 33 tones, in this case spaced 9Hz apart (actually 8.7890625 Hz, exactly 1.5 x the baud rate at the highest speed), resulting in a signal bandwidth of 300Hz, including the keying sidebands. The ITU Emission Designator is 300HF1B. The modulation is constant amplitude, phase coherent MFSK, using IFK+ coding with 32 frequency differences, yielding 32 unique codes. This means that each symbol carries enough information for all lower case letters to be expressed in just one symbol, which greatly enhances the speed.

## Some key features of FSQ:
- IFK+, providing drift-proof operation and good tolerance of multi-path interference.
- Efficient Alphabet, where most letters and punctuations can be sent in just 1 symbol.
- No synchronization required for decoding, allowing fast acquisition of signal
- Arbitrary transmission speed, allowing transmission and reception of baudrates at any rate between 2-6 Bd, without requiring adjustment on the receiver's side.
- Chat operation, behaves like a messaging app.
- Supports selective calling functions,telemetry,image transfer, and file transfer functions.