Hellschreiber (Also known as Feld Hell or just Hell) is a teleprinter system developed in the late 1920's by Rudolf Hell, a German inventor. Hell physically prints characters onto the screen, unlike other modern teletype modes which encode and decode signals.

Feld Hell (and it's immediate variants) and Slow Hell use On-Off Keying, where Feld Hell 80 (Rudolf Hell's last original Hell mode, designed in the 1970's) uses 2-FSK modulation and the FSK Hell modes use 2-DMSK (Differential Minimum Key Shifting).

| Mode         | Symbol Rate | Typing Speed       | Duty Cycle | Modulation | Bandwidth | ITU Designation |
|--------------|-------------|--------------------|------------|------------|-----------|-----------------|
| Feld-Hell    | 122.5 baud  | ~2.5 cps (25 wpm)  | ~22%       | OOK ASK    | 350Hz     | 350HA1B         |
| Slow Hell    | 14 baud     | ~0.28 cps (2.8 wpm)| ~22%       | OOK ASK    | 40Hz      | 40H0A1B         |
| Feld-Hell X5 | 612.5 baud  | ~12.5 cps (125 wpm)| ~22%       | OOK ASK    | 1750Hz    | 1K75A1B         |
| Feld-Hell X9 | 1102.5 baud | ~22.5 cps (225 wpm)| ~22%       | OOK ASK    | 3150Hz    | 3K15A1B         |
| FSK-Hell     | 245 baud    | ~2.5 cps (25 wpm)  | ~80%       | 2-MSK      | 490Hz     | 490HF1B         |
| FSK-Hell 105 | 105 baud    | ~2.5 cps (25 wpm)  | ~80%       | 2-MSK      | 210Hz     | 210HF1B         |
| Hell 80      | 245 baud    | ~5.0 cps (50 wpm)  | 100%       | 2-MSK      | 800Hz     | 800HF1B         |

# Modulation details
The signal is transmitted in columns. The receiver generally displays each column twice, one below the other. This is done to mitigate the skew that can be cause by timing errors.

Each column is sent on equal time slices, and the time it takes to send one column depends on the variant. Here’s a small table that shows this.

| Mode          | Column time (seconds)      |
|---------------|----------------------------|
| Feld-hell     | 1 / 17.5                   |
| Slow hell     | 1 / 17.5 * 8               |
| Feld-hell X5  | 1 / 17.5 / 5               |
| Feld-hell X9  | 1 / 17.5 / 9               |

It can be seen from this table that the default method transmits 17.5 columns in one seconds, the faster modes are 5 and 9 times faster, and the slower mode is 8 times slower. A small disclaimer is that I have only tested these values by using software decoders made by other people, since I don’t have a real machine.

The faster variants use more bandwidth and are less resistant to noise, while the slower variants become narrow signals that can be decoded with plenty of noise. If you know the conditions beforehand, you can make a good tradeoff in order to transmit your signal as fast as possible without making it unintelligible.

If the signal is being generated as sound, it needs to be put on a carrier frequency. 1500 Hz can be a good default.