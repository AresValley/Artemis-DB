FM NBTV is a method to send moving images in a very narrow bandwidth (maximum 3 KHz).

The OFDM NBTV and Digital NBTV systems have advantages and disadvantages, but one thing they both suffer from is lack of user familiarity! It would have been quite straight-forward to adapt conventional SSTV into a narrow-band (NBTV) system, with consequent user familiarity, but it was felt that there were good reasons to improve on matters.

Thus the Hybrid NBTV system was born. The image modulation is conventional SSTV (FM subcarrier), most similar to the ROBOT24 mode, with a colour difference system for colour transmission. Since one of the main aims of the design was to provide a good frame rate, suitable for transmitting movie clips, it was important to develop a faster system than SSTV. This higher frame rate also works in favour of reducing the number of frames damaged by burst noise such as lightning.

However, by using a high line rate that high frame rate requires, the effect of multi-path timing variations (the bane of SSTV) becomes quite a serious problem. This was the motivation behind adding a PN sequence sync 'pulse' at the start of each block of data. Using this PN sequence in the same way as the Digital NBTV system, it is possible to not only provide very secure and sensitive sync for the receiver, but to also allow the image data to be lined up exactly, even if the timing changes part way through the image, thanks to an Equalizer system.

You might think the picture on the right looks noisy, and poorly synchronized. It certainly is noisy, as it shows a single frame of Hybrid NBTV transmission which had been sent twice over a 500km path on 80m at night. SSTV would fare no better. However, look at the edges of the vertical black bar - no tearing or misalignment at all, thanks to the PN sequence digital sync.

The Hybrid NBTV system transmits data in packets, like the Digital system, but they aren't data packets - they are Hybrid packets, with a digital header and analog image information. Each packet contains a sync 'pulse' (PN sequence), which is BPSK modulated, followed by analog image information, which is frequency modulated. Each packet contains the brightness information for three lines, plus the colour difference information for the average of these three lines, in another 'line'. The 128 x 96 pixel image frame can be transmitted in 24 packets. Each image takes about ten seconds to transmit.

The sync operates by identifying the PN sequence using a cross-correlator (exactly as in the Digital SSTV)and using the very precisely timed peak to identify when the image information starts, thus aligning the image perfectly, even if the signal is received with considerable multi-path timing variation. The timing difference between one PN sequence and the next is also used to measure the subcarrier frequency (for receiver tuning) and to measure the timing differences between PN sequences, in order to operate the Equalizer which controls sampling of the demodulated image.

Operating Modes Just one mode is offered at present. Images of 128 x 96 pixels (conventional 4:3 landscape format) are transmitted with no image compression, other than the colour encoding.

There is an option to use positive image modulation (the default is negative), which may sometimes improve impulse interference rejection. This needs to be manually selected at both transmitter and receiver.

Modulation As mentioned above, Hybrid NBTV uses a single-carrier system. A 1500Hz subcarrier is BPSK modulated with a pseudo-random binary (PN) sequence at the start of each packet, and is used to identify an exact point in the transmission from which the image can be synchronized. A cross-correlator is used in the receiver to locate the one point in the whole message where the sequence matches up with the local copy of the sequence. The cross-correlator works with a known pattern to look for, and is a very powerful and sensitive tool.

The image however is analog, and the nominal 1500Hz subcarrier is FM modulated with brightness and colour difference information in exactly the same way as SSTV.

The ITU 'Emission Designation' for this mode is 2K00W1FNF