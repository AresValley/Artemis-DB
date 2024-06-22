The Global Positioning System (GPS) is a global navigation satellite system (GNSS) which provides precision position, navigation, and timing (PNT) services to devices around the globe. It is broken up into the space segment (the constellation formed of 31 active satellites or "space vehicles" that broadcast a precision code and navigation message), the control segment (ground stations which monitor and manage the health of the satellites) and the user segment (the equipment used for receiving and utilizing signals from the space segment). In order to obtain a fix, a receiver must obtain almanac/ephemeris data containing orbit information and decode the precise timing code for at least four space vehicles (a fourth is necessary to determine the receiver's time so it can calculate pseudorange, as the time of the receiver usually not known to the degree of precision required for distance calculations).

# Frequencies
"Space Vehicles" broadcast different signals (some of which are on the same frequency as each other) for various services. Depending on the generation/block of satellites, each space vehicle broadcasts navigation signals on the L1, L2, and L5 bands which contain the satellite's precise time which can then be used in conjunction with orbital ephemeris data (which is also broadcast as "navigation messages" at 50 bits/second) to determine the receiver's position, velocity, and time (PVT). C/A, L2C, and L5 are currently the only publicly-available navigation services available for civilians to use. The L5 band only contains one service.

| Band     | Frequency (MHz) | Bandwidth (MHz) | Usage/Services                                      |
|----------|------------------|-----------------|-----------------------------------------------------|
| L1 Band  | 1575.42          | 24              | Navigation: C/A, L1C, P(Y) Code, and M-Code Broadcasts|
| L2 Band  | 1227.60          | 22              | Navigation: L2C, P(Y) Code and M-Code Broadcasts     |
| L3 Band  | 1381.05          | -               | Nuclear Detonation Detection                        |
| L4 Band  | 1379.913         | -               | Ionospheric Correction Studies                      |
| L5 Band  | 1176.45          | 25              | Navigation (Safety-of-Life): L5 Signal              |
