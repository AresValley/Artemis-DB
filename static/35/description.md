AHICDM is a simple, slow and reliable modulation protocol that allows binary data in standard ASCII to be sent over audio.

The mode was originally invented to be a fast yet stable means of transferring binary data over radio, however, the use of only one frequency means that this mode is best for narrowband communication.

It uses a tone of 440HZ and each pulse is a consistent sine wave for 100MS (50MS in newer revisions).

The data is decoded via the duration of the silence between pulses.

The baud rate of a message depends on the message being sent. It is faster to send '1' than it is to send '0'.

The name originates from the ability to send Base64 encoded images using AHICDM