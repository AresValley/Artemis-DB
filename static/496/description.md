A small unit is fixed to the road where the cars will drive. It is probably interrogated by the 'zone controller' unit using something similar to RFID. A directional antenna from the zone controller is pointed at the road sensor (the frequency of this is currently unknown). Data is transmitted from the zone controller regularly, even when no traffic is present.

The communication format is unknown, it uses frequency hopping over 10 MHz.

It appears to be similar to the system described in this website http://www.trafficparking.com.au/vehicle-counting-systems.php and the equipment appears to be provided by http://www.smartparking.com/ (but that website doesn't have much information).

# Characteristics
The system appears to be using frequency hopping FSK signals that have a very high data rate. Each burst is 5.625 ms long with a minimum of 0.850ms between bursts. Each burst is a FSK burst at 200 kBd with a shift of 200 kHz. Each burst sends a frame of 1125 bits at a raw data rate of 200 kbps.