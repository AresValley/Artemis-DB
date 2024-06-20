JJY, also known as JJY-40 and JJY-60, is the call sign for a pair of longwave Time Signal stations in Japan.

The station is located in Japan and broadcasts from two sites, one on Mount Otakadoya, near Fukushima, and the other on Mount Hagane, located on Kyushu Island . JJY is operated by the National Institute of Information and Communications Technology (NICT), an independent administrative institution affiliated with the Ministry of Internal Affairs and Communications of the Japanese government.

# Characteristics
JJY has two separate frequencies, one on 40kHz (JJY-40) and one on 60kHz (JJY-60). JJY-40 is transmitted from Mount Otakadoya, where JJY-60 is transmitted from Mount Hagane.

Both JJY-40 and JJY-60 signals contain an identical pulse-width modulated time code and are transmitted 24 hours a day. Low frequency (LF) transmissions are used to enhance accuracy and reduce the possibility of atmospheric interference.

Japan Standard Time is set by a caesium atomic clock in Tokyo. This information is sent to the transmitter stations and is used to set a caesium atomic clock at each station. These clocks are housed in an environmentally controlled and electromagnetically shielded room to prevent outside interference with the clocks.

The time code format is very similar to that of WWVB in the United States but technically is a variant of IRIG. Similarly to WWVB or MSF the signal of JJY is used to synchronize consumer radio-controlled clocks sold throughout Japan.

Time Format with Callsign Diagram
As with most longwave time code stations, the JJY signal is amplitude-modulated to send one bit per second, transmitting a complete time code every minute.

The time code is most similar to that transmitted by WWVB, but each bit is reversed: on the second, the carrier is increased to full power. Some time during the second (depending on the bit to be transmitted), the carrier is reduced by 10 dB, to 10% power, until the beginning of the next second.

There are three different signals that are sent each second:

- 0 bits consist of 0.8 s of full power, followed by 0.2 s of reduced power.
- 1 bits consist of 0.5 s of full power, followed by 0.5 s of reduced power.
- Marker bits consist of 0.2 s of full power, followed by 0.8 s of reduced power.

As with WWVB, seconds 0, 9, 19, 29, 39, 49 and 59 of each minute are marker bits. The remaining 53 encode Japan Standard Time using binary-coded decimal. JST does not include summer time, but bits are reserved to handle it. Leap second warning bits are also provided, these announce leap seconds starting at the beginning of the UTC month (09:00 JST on the first day of the month), and ending with the leap second insertion (just after 08:59 JST on the first day of the following month).