Motorola Type II refers to the second generation Motorola Trunked Radio Systems that replaced fleets and sub fleets with the concept of talkgroups and individual radio IDs.

# Characteristics
There are multiple variations of the Type II Trunking system these include: Smartnet, SmartZone, SmartZone, OmniLink, VOC, & Hybrid
Type II systems have no dependencies on fleetmaps, and therefore no limitations to how many radio ids that can participate on a talkgroup. This allows for greater flexibility for the agency.

Motorola Type II talkgroups appear on a scanner as an even number without a hyphen, ranging from 16 to 65504 in increments of 16 or 32 (depending on whether the system uses Priority Monitor or not).
Talkgroups on systems using Priority Monitor will display as 16, 48, 80, 112 and so on; on systems where Priority Monitor is not used, talkgroups display as 16, 32, 48, 64, 80 and so on.
Individual radio IDs, on the other hand, appear as a number between 1 and 65534; while Type II systems have some gaps in usable IDs (for system technical reasons), most are capable of up to at least 65000 individual radio IDs.

# Emergency Flagging
Motorola systems have two potential forms of flagging a talk group as being in an emergency mode (this gives a user priority on a talk group until the emergency state is cleared by the user or the dispatcher): the first method is to set a status bit in the management traffic, the second is to shift the talk group ID by +2 and patching it to the original talk group ID (+0). Uniden scanners are only capable of detecting the first method. A hack of a solution is to add the original talk group ID and the offset talk group ID (+2) to the system in the scanner and set the priority of the +2 talk group ID to be On; one can then add an alert tone and alert backlight to the offset talk group to simulate the emergency detection functionality available to systems that use the second flagging method.

# Status Bits
Type II Smartnet systems uses status bits for special transmissions such as Emergency, Patches, DES/DVP scrambled transmissions, and Multi selects on Motorola Trunking systems. Motorola Trunking radios directly interpret them for their special functions, thus no difference is noticed by the person with the radio. The Trunktracker scanners however interpret these special talkgroup status bits as different talkgroups entirely. To the right is the conversion chart for these special status bits.

Therefore, if a user was transmitting a multi-select call on talkgroup 1808, the trunktracker would actually receive those transmissions on 1815. Some common uses of these status bits are as follows:

- When a user hits their emergency button, all conversations on the talkgroup revert to the emergency status talkgroup (ID+2) until the dispatch clears the emergency status. Therefore, if someone hit their emergency button and their radio was on talkgroup 16, all communications would switch to talkgroup 18.
- A lot of Fire and EMS departments dispatch tone-outs and alarms as Multi-select communications (ID+7). Therefore, if your fire department dispatch talkgroup is 1616, and they do dispatch tone-outs and alarms as Multi-selects, then those communications will be on talkgroup 1623.

This can be a problem, because you will miss communications if you don't have those talkgroups programmed. By setting the Type II block you are monitoring with a fleetmap of S-1 (Mot Size A), you'll essentially get Type I sub fleets for each Type II talkgroup - encompassing all of the status bits into one subfleet. Some scanners also allow you to disable the status bit information so that you will always see the ID+0 regardless of the status of the talkgroup.

SmartNet systems also added a scanning feature, called "Priority Monitor," which permitted priority scanning of talkgroups. The subscriber radio has the choice of selecting two priority talkgroups (one high and one low priority in addition to eight non-priority talkgroups). When the radio is in the middle of a voice call it is continually receiving sub-audible data on the voice channel indicating the talkgroup activity on the other channels of the system. If a talkgroup id pops up which is seen as a higher priority to the active call the radio will switch back to the control channel to look for the late entry data word indicating which channel to tune to.

This voice channel sub-audible datastream has a limitation in the number of bits it can use to represent a talkgroup id. Because of this the last digit of the talkgroup id (right-most) is removed. The radio then presumes any id it receives is an odd numbered talkgroup id. This is the reason behind odd numbering of talkgroups on SmartNet systems. If the systems administrator assigned odd AND even numbered talkgroups there would be a lot of confusion with the Priority Monitor feature when reading the data over the voice channel. With the early versions of the Radio Shack PRO-92 you saw this trouble as it used only the sub-audible data to track trunked systems.

# Motorola Subtypes
## Motorola Type IIi Hybrid

A Motorola Type IIi Hybrid system has "blocks" of the system that are Type I Fleets/Sub fleets and Type II talkgroups. All radios may be Type II, or the Type I radios might be used exclusively in sub fleets while the Type II's are used exclusively in talkgroups.

Motorola Type IIi Hybrid is a system that has Type I fleets and sub fleets, and has Type II radios that are able to use those Type I fleet/sub fleets. The common reason that an agency sets up a Type IIi Hybrid system is because they have newer Type II radios that they want to interoperate with older Motorola Type I radios, without having to create new Type II talkgroups.

## Motorola Type II Smartnet
Motorola Type II Smartnet is a 2nd generation Motorola Trunking system. The term Smartnet refers to a set of features that make Motorola Type I and II trunked systems APCO-16 compliant. These include better security, emergency signaling, dynamic regrouping, remote radio monitoring, and other features.

The following is true of a Type II Smartnet system:

- Up to 28 system channels
- Up to 65534 unique radio ids
- Up to 4095 talkgroups
- They use odd numbered talkgroups

## Motorola Type II SmartZone
SmartZone systems are comprised of Smartnet systems that are networked together via microwave or land-line data circuits to provide multi-site wide-area communications. Many large public safety and state agencies use SmartZone systems, and is among the most common trunked system. Each individual trunked system is considered a site, or sub-system if you a considering a Simulcast system, and is controlled by the Zone Controller, which is the master controller for all activity and is where all network links are terminated at. Your primary type of sites are 6809 (single or Simulcast configurations), MTC-3600 (introduced to take the place of the 6809), and Intelli Repeaters (single-site only). A feature unique to SmartZone and allows efficient use of channels at each site is called "Dynamic Site assignment." Its simple purpose is to determine whether a site needs to broadcast a call or not. In order to make this feature work subscriber radios are required to affiliate, or send in their radio id and talkgroup, whenever they power-up, change channels, or change sites. These affiliations are compiled into a table which the Zone Controller maintains. When a call is requested at a site the Zone Controller determines which site that talkgroup is registered at and routes that audio via a switch, commonly called the Ambassador Electronics Bank, to the appropriate channel at the site. Many large public safety and state agencies use SmartZone systems for wide-area communications. Up to four SmartZone systems can be linked together into one Motorola Type II SmartZone OmniLink network.

The characteristics of a Motorola SmartZone system are similar to Smartnet systems with the following changes:

- Up to 28 channels per site
- Up to 64 sites (older ZC versions were limited to 48)
- Analog and/or digital voice

Monitoring a SmartZone system with a trunk tracking scanner is the same process as monitoring any other Smartnet system, except that you can only monitor one site at a time. For you to monitor a specific talkgroup on a SmartZone site, someone's radio must be affiliated to that specific site. Therefore, if you are monitoring talkgroup "POLICE-NORTH" on a site with no affiliated radios on that talkgroup, then you will not hear any communications on that talkgroup on that site.

The new MZC3000 SmartZone Zone Controller introduced an ethernet based connection point for sites, consoles, data broadcast boxes, and C/DIUs. A Release 3.x system will support up to 48 sites and Release 4.1 system will support 64 sites, and eliminates pieces of hardware that previously limited the number of sites because the connection ports were shared.

## Motorola Type II SmartZone OmniLink
Type II SmartZone OmniLink provides a broad range of robust system features and utilizes a distributed call processing architecture which links up to four multi-site Type II SmartZone systems together into one seamless network, supporting up to 192 sites. Typical users of SmartZone OmniLink systems include organizations who have vast geographic requirements -- such as electric and gas utilities, and extremely large public safety agencies.

Each Zone in an OmniLink network is considered its own SmartZone network, will have its own unique system id, and is controlled by its own Zone Controller. The Zone Controllers are controlled by the Master Controller. Radios can be permitted or restricted to roam from one Zone to another. The OmniLink infrastructure permits each Zone Controller to communicate and coordinate these roaming actions. (This is similar to cellular networks and roaming onto another carrier's network)

## Motorola Type II VOC
The introduction of SmartZone introduced the Intelli Repeater. An Intelli Repeater, or IR, site is a bare-bones trunked site which has no database of users or talkgroups. It is simply sophisticated software running on a Quantar repeater. It is meant to be controlled by the Zone Controller and to be commanded as to who has permission and who does not. There are some very basic restrictions in the event Site Trunking (a site loses its link to the Zone Controller) does occur but for all intents and purposes once an IR site is in Site Trunking mode it's a free-for-all site.

IR sites are generally used for a small geographic area or to fill in holes. For sites that are used to fill in coverage traffic is very limited. To allow as limited a number of channels for use, and to be spectrum efficient, Voice On Control (VOC) was developed to permit the control channel to temporarily act as a voice channel. This allows as little as one channel per site, but access must be severely restricted to the site or communication problems will occur.

When all channels at a VOC enabled site are in use, or a single channel site gets a call request, there is specific data sent out over the control channel to notify all radios at the site that the control channel will be momentarily switching to voice channel mode. Once this happens radios resort to their programmed information which contains timing values that determine what to do once the timer runs out and there is still no control channel (Signal "Out of Range," switch sites, etc.) available.
