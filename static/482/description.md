UK AM Data System (UK-AMDS) was developed by BBC Research and Development in 1984 as a way to transmit low bitrate data on BBC Radio 4's LF AM carrier. Elements of this system were adopted into ETSI's AMSS.

# Characteristics
Digital data is transmitted by directly modulating the 198 kHz carrier using bi-phase 22.5 degree PSK encoding. The PSK subcarriers are transmitted 25 Hz from the main AM carrier. The PSK data signal operates at 50 symbols/sec, with data rate at 25bps from Manchester Encoding.

30 messages are transmitted per minute, each message having 50 bits of data. The total block length of each frame is 50 bits. 2 seconds = 1 block = 50 bits.

The BBC header of each block consists of 6 bits. The first bit is a fixed logic 1 bit that is used for synchronization. The following 4 bits of the BBC header represent the Block Application Code, with codes 0-15. This allows for 16 possible data channels. For example, one data channel is used to transmit an accurate time code. Another channel is used by UK electricity companies for switching domestic storage heaters and setting off-peak electricity tariffs.

The next 32 bits contains the user data payload. Following the 32 bits, there is a 13 bit CRC tail, which completes the 50 bit block.

All blocks transmit their most significant bit first. Thus, the last bit transmitted in a block has weight 2^0. The data transmission is fully synchronous and there are no gaps between blocks.