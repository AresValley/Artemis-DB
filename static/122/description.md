Contrôle de vitesse par balises (Speed control by beacons, abbreviated to KVB) is a railway safety system used in Mainland France and in the United Kingdom between London and the Channel Tunnel. The passive beacons are placed trackside and store line information that is transmitted to the train as it passes over. A signal similar to the Eurobalise downlink is constantly transmitted from the train which energizes the beacon and clocks the data with a OOK signal. The reply to the train is coded by the beacon by selectively echoing a ring at 1/6th of the carrier frequency.

# Frequencies
Power and clock downlink to beacon: 27.115 MHz carrier, 50kHz AM
Data uplink to train: 27.115 MHz / 6 ~= 4.5 MHz, 50kHz AM

# Data
The analog version of the system continuously repeats a 32-bit frame with a fixed 8-bit start marker, and a 12-bit payload doubled by its complement. Most beacons transmit fixed data. Some are connected to light signals to transmit variable data depending on their state.