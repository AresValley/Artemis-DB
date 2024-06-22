PSK is a digital amateur radio mode based on Phase-Shift Keying (PSK) modulation. Most commonly used in HF, rarely seen at higher frequencies.

# Modes and Samples
There are many different PSK modes. These modes are ones found available with the fldigi software. The most popular and commonly used mode is PSK 31 (developed by Peter G3PLX). Its narrow bandwidth and typing-speed baud rate make it popular for Ham Operators to use for keyboard to keyboard communications within the amateur bands.

PSK 63 (developed by Moe Wheatley (AE4JY) and Howard Teller (KH6TY)) is twice as fast as PSK 31, and occupies 160 Hz of bandwidth. These can occasionally be seen. PSK 63 FEC (developed by Nino Porcino IZ8BLY) is a variant of PSK 63 that uses convolutional encoding to provide forward error correction. It is more suitable in more noisy environments where the other PSK modes would have large error rates.

The other modes (PSK 125, 250, 500, 1000) are used for sending large text files or binary files. These have a far higher transfer rate. Due to the high rate of transfer, typically ARQ (Automatic Repeat Request) is also applied when sending files via these modes to ensure that the recipient gets 100% of the file. When sending binary files, one missed bit can make a file completely worthless, so it's important that the recipient has a complete copy without any loss. PSKMail is a good example of using ARQ and PSK to send files.

Within PSK, there are 2 primary modulation modes: Binary PSK (Also known as 2-PSK) and Quadrature PSK (Also known as 4-PSK). Binary PSK uses only 2 phase constellations to send characters, whereas Quadrature PSK uses 4 phase constellations.