The E084 is a radiosonde designed in 1990 by Deutsche Wetterdienst. These radiosondes are fairly common and cheap as surplus items, and it is possible to adjust the frequency to transmit in the 70cm ham band.

# Circuit Description
A temperature sensor controls the frequency of a sawtooth generator. The prescaler divides the transmit frequency by a factor of 64. The signal generated then modulates a UHF transmitter, which transmits the measurement data in frequency modulation with a deviation of ± 2.8 kHz. A 74HC4066 is configured as a phase detector and now tries to adjust the divided transmission frequency to the quartz frequency using a control voltage (VCO). Both the tone generator and the UHF transmitter are built in SMD on 0.8mm thick FR4 for reasons of space and weight, the whole circuit is encased in a lightweight expanded polystyrene shell.

# Decoding Tutorial
A frequency meter on the demodulated audio is sufficient to recover the temperature information. At 0 °C the audio frequency will be 300 Hz, at 26 °C 375 Hz.

Based on the official documents, the formula for the conversion is: temperature = 0.33 × frequency - 105

With a frequency of 396 Hz, the temperature is 0.33×396-105 = about 25.6 °C.

This temperature needs to be corrected by the correction factors stated on the label attached to the radiosonde itself.