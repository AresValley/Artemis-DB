The Yugoslavian 20-Tone Modem, also known as YUG-MIL 20-Tone and YUG Diplo 20-tone, is a 20 tone OFDM PSK modem used in former Yugoslavia for military and diplomatic use. No longer used today.

# Characteristics
The 20-tone modem spans about 2200 Hz of bandwidth. Each subcarrier is shifted 110 Hz and uses BPSK at 75 Bd each, for a total data rate of 1500 bps. The preamble is similar to that of the MIL-STD-188-110 39-Tone Modem.

# Military
The first three unmodulated tones have a duration of ~530ms with an 880 Hz shift between them. Afterwards, a two-tone BPSK preamble starts, also at 880 Hz shift but centered and with a duration of ~550ms. Some data is transmitted by the two-tone BPSK preamble, possibly for syncing and decoding purposes.

# Diplomatic
Has the same three unmodulated tones but with a longer duration of ~650ms with 950 Hz shift between tones. Afterwards, there is a single BPSK preamble with a unmodulated tone at a 900 Hz shift. This preamble lasts ~440ms. Like the Military variant, the BPSK preamble sends data.

The Diplomatic variant uses ARQ, so there is an ISS and IRS signal for the transmitting station and receiving station.