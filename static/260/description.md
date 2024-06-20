JT65 is an amateur radio QSO communication protocol developed by Joe Taylor, K1JT. JT65 has 3 submodes: JT65A, JT65B, and JT65C. The most popular submode of JT65 is JT65A. JT65 gets '65' from the 65 tones it uses.

Each transmission begins at t = 1s after the start of a UTC minute and finishes at t = 47.8 s. Each transmission must begin within the first 4 seconds of the minute to be decoded. Multiple stations transmit on the same carrier using both FDM and TDM methods. Initiating stations choose either the Even or Odd minute to transmit and responding stations transmit on the opposite minute.

A sync (low) tone is to mark the lower boundary of each station's signal. The synchronizing tone is at 1270.5 Hz. The initiating station is responsible for choosing an offset that does not conflict with another station's signal. JT65 uses 126 contiguous time intervals, each of length 0.372 s (4096 samples at 11025 samples per second). Within each interval, the waveform is a constant-amplitude sinusoid at one of 65 pre-defined frequencies, and frequency changes between intervals are accomplished in a phase-continuous manner.

# Submodes
The three main submodes, JT65A, B, and C, differ in the frequency shifts between each of the 65 tones. For JT65A, the shift is 2.7 Hz. For JT65B, it's 5.4 Hz. For JT65C, it's 10.8 Hz. The general rule used is the resolution function 2.7m, where A uses m=1, B uses m=2, and C uses m=4.

Two experimental submodes, JT65B2 and JT65C2 are twice as fast as their counterpart JT65B and JT65C respectively. The tone frequency shifts are the same.

# Frequencies
The signals are usually found in the data portion of the Amateur Radio Bandplans between the CW (Morse) and the PSK/RTTY windows. They are always transmitted in USB mode regardless of band.

## JT65A
- 160m: 1838.0 kHz USB
- 80m: 3576.0 kHz USB
- 40m International: 7039.0 kHz USB
- 40m USA: 7076.0 kHz USB
- 30m: 10139.0 kHz USB.
- 20m: 14076.0 kHz USB
- 17m: 18102.0 kHz USB.
- 17m Alternate: 18098.0 kHz USB
- 12m: 24917.0 kHz USB
- 6m EME: 50276 kHz USB

## JT65B
- 2m UK Beacon: 144,430 kHz Kent
- 70cm UK Beacon: 432,430 kHz Kent

## JT65C
- 23cm UK Beacon: 1,296,800 kHz Isle of Wight