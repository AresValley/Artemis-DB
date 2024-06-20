OFDM NBTV is an analog technique, in fact it is a true Fuzzy design as well. The transmission technique used is quite different from conventional TV - each line is transmitted separately, but all lines are sent at the same time, on a slightly different frequency. Because the transmitter and receiver operate at precisely the same speed, controlled by the computer sound card, there is no need for any sync pulses to align the picture; in fact there is no automatic synchronizing mechanism at all: isn't necessary.

Modulation on each of the many carriers is very narrow FM (a few Hz), for best noise rejection, and the overall transmission bandwidth is only 2kHz, so an SSB transmitter and receiver can be used. These modes are Fuzzy Modes, which means that although the computer samples the images for transmission and display, the signals are essentially analog in nature, and at the receiver the images are presented without decoding decision or intepretation by the computer - they are interpreted by eye and brain at the receiver. This means that the signals are inherently very noise immune and continue to be useable despite interference and propagation effects until they fade into the noise.

The design is very versatile, and you can use still photographs (like a slide show), moving GIF images, AVI movies and many different types of live video, including 'web cams', video capture cards, digital cameras, screen shots from other software, and even live (fast scan) TV, although only one frame in many is transmitted in this case. A 'drag-and-drop' technique makes all this very easy.

## Limitations
Because of the low bandwidth, it is not possible to send moving pictures in real time. Each image frame takes from one second to nine seconds to transmit, depending on the mode used. However, the received signal can be recorded and later played back faster for a very realistic effect. Standard .AVI format files are used, and the transmitters can also retransmit previous recordings. The images can also be post-processed for noise reduction and smooth motion effect. The quality of moving images is such that you'd never believe that the pictures contain only 48 or 72 lines!

On lower HF bands, especially with NVIS conditions (strong fading and multi-path reception), performance suffers as noise and colour stripes invade the picture. The 96 x 72 pixel colour mode is most affected. However, on the higher bands and VHF, the pictures are superb.

Another limitation is that tuning requirements are fairly stiff - you CANNOT use a VFO rig - it simply isn't stable enough. Most modern synthesized transceivers are OK if used with care. Tuning needs to be within 1Hz of the transmission. On VHF the secret is to use FM transceivers, and thus avoid the problem completely.

## The OFDM NBTV Modes

There are in total five modes, two black and white, and three colour. There is some compatibility between the B&W and Colour modes, so you can soon work out which is being transmitted. There are two different image resolutions, 48 x 48 pixel low resolution (which is faster and more robust), and 96 x 72 pixel modest resolution, which of course is slower, but gives more picture detail. A special compressed 96 x 72 pixel colour-only version is provided - this provides a frame rate twice as fast as the standard 96 x 72 colour mode, but is suited only to higher bands and VHF. The picture on the right below shows typical 48 x 48 colour reception.

- 48 x 48 Low resolution B&W and RGB colour for NVIS conditions
- 96 x 72 Modest resolution B&W and RGB colour for HF use
- 96 x 72 Modest resolution compressed RGGB colour for VHF 