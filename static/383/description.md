Project 25 (P25 or APCO-25) is a trunked radio standard developed by The Association of Public Safety Communications Officials International (APCO-25) for use with public safety organizations around the world. P25 supports encrypted voice.

# Modulations
## Phase I FDMA
Phase 1 uses a 9600bps data rate to transfer IMBE-encoded voice or packet data. Phase 1 can use either C4FM (continuous 4-level FM) or CQPSK (Compatible Quadrature Phase-Shift Keying, also known as Linear Simulcast Modulation) modulations. Both uses a 4800bd symbol rate with four-level signaling, resulting in the 9600bps data rate. CQPSK modulation is more resistant to inter-symbol interference than C4FM, and thus is much easier to transmit in a simulcast configuration. It is labelled "Compatible" because the deviation at symbol time is the same as C4FM, so FM receivers can still decode it. CQPSK modulation requires a linear amplifier and thus can only be produced by appropriately equipped fixed equipment, such as repeaters and trunked sites. Subscriber equipment, such as portables and mobiles, will transmit in C4FM regardless of whether it is receiving CQPSK.

A non-standard Motorola modulation, wide-pulse, uses 4FSK to occupy a wideband radio channel; wide-pulse is rarely found nowadays due to its spectral inefficiency. It was designed to create a wider eye in the waveform, allowing very large distances between simulcast sites. Trunked wide-pulse is only found in Motorola Type II trunked systems with digital voice, as it is not compliant with APCO's Project 25 standard. Most Motorola conventional repeaters and subscriber equipment can transceive in wide-pulse.

## Motorola X2-TDMA
X2-TDMA is a non-standard variation of P25 that Motorola used on some units to implement TDMA before the Phase 2 standard was completed. X2-TDMA uses the same 9600bps bit rate as Phase 1, but uses the two timeslots and AMBE+2 vocoder of Phase 2. Like Phase 2, it was only found on trunked systems. X2-TDMA is no longer supported and virtually all operational equipment has been upgraded to standards-compliant Phase 2.

## Phase 2 TDMA
The Phase 2 standard is a 2-slot, 12000bps TDMA signal that fits inside a 12.5 kHz wide channel. Fixed site output modulation is H-DQPSK with subscriber units using H-CPM on the input. This allows existing 12.5 kHz wide license holders to double call capacity by upgrading their infrastructure to Phase 2. The Phase 2 standard was approved in November 2010, and as of August 2011 Motorola has begun shipping Phase 2 systems. Phase 2 operation is only supported on trunked systems, and conventional operation still uses Phase 1. Additionally, Phase 2 capability applies to the voice channels, and control channels are sent with the same C4FM or CQPSK modulation seen in Phase 1 systems.

Motorola ASTRO 25 systems can also have an optional feature known as Dynamic Dual Mode (DDM), which will seamlessly revert a talkgroup to FDMA operating mode if a Phase I only capable radio affiliates with a Phase II capable talkgroup.

Very recently, some Harris systems began to implement TDMA control channels. Audio samples can be found here.

# System IDs and NACs
Project 25 signals carry a three-digit hexadecimal Network Access Code, or NAC. NACs are used similar to CTCSS or DCS on an analog signal, and are used to ensure a radio is receiving the correct signal. Each P25 site, be it a trunked site or a conventional repeater, will use one NAC. The $ symbol before a number represents a hexadecimal value. A few NACs are special:

- $293: The default NAC used on P25 equipment. This NAC is commonly found on interoperability channels and ham radio equipment.
- $F7E: A receiver configured to receive $F7E will ignore the received NAC and always unmute.
- $F7F: A repeater configured to repeat $F7F will retransmit any received NAC intact. For example, it will send NAC $487 if NAC $487 is received, and NAC $293 if $293 is received.

Talkgroup IDs are logical channels used to subdivide traffic on each site. If two groups want to share a single P25 system and not hear each other, they can configure separate talkgroups. Talkgroup IDs are four-digit hexadecimal numbers, but are usually written as the decimal equivalent. Talkgroup 1 is the default value used (and sent by equipment not configured to use talkgroups), and 65535  is used as an all-call.

Trunked systems carry an additional set of IDs, called the WACN, System ID, RFSS, and Site ID. The WACN and System ID identify the trunked system, while the RFSS and Site ID identify the trunked site. The WACN and System ID are (intended to be) unique across all trunked systems, while the RFSS and Site ID must be unique only within a trunked system.

- WACN (Wide Area Communications Network) is a 20-bit hexadecimal value used when different trunked systems need to interoperate, and subscriber radios can be configured to roam within other systems with the same WACN. The default WACN is $BEE00.
- System ID is a 12-bit hexadecimal value, together with the WACN, identifies a trunked system. While the default System ID is $001, trunking systems do not use $001 for security reasons. There is no one common value used for System IDs, even in deployable interoperability systems.
- RFSS (RF Sub-System) is a one-byte hexadecimal (though commonly expressed as decimal) value which identifies a cluster of sites intended to carry the same set of users. Subscriber radios can be configured to roam seamlessly between sites within the same RFSS. The default RFSS is 1 ($1).
- Site ID is a one-byte hexadecimal (though commonly expressed as decimal) value that identifies a single trunked site. The combination of RFSS and Site ID uniquely identify a trunked site within a trunked system. The default Site ID is 1 ($1).
On a trunked system, NACs are not used for transmission identification. Instead, the NAC is commonly set with the first two digits being the first two digits of the System ID, and the last digit being the last digit of the Site ID.