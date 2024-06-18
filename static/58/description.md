BPM is a time signal transmitted by the Chinese Academy of Sciences, broadcasting from CAS's National Time Service Center in Pucheng County, China.

Signals emitted in advance on UTC by 20 ms. Second pulses of 10 ms duration with 1 kHz tones. Minute pulses of 300 ms duration with 1 kHz tones. UTC time signals are emitted from minute 0 to 10, 15 to 25, 30 to 40, 45 to 55. UT1 time signals are emitted from minute 25 to 29, 55 to 59.

# Transmission Format
| Minute | Duration | Transmission                                                                                         |
|--------|----------|------------------------------------------------------------------------------------------------------|
| 00     | 30       | UTC: 10 ms second ticks, 300 ms minute ticks.                                                        |
| 10     | 40       | Carrier (no time code)                                                                               |
| 15     | 45       | UTC: 10 ms second ticks, 300 ms minute ticks.                                                        |
| 25     | 55       | UT1: 100 ms second ticks, 300 ms minute ticks.                                                       |
| 29     | 59       | Station identification: Morse call sign for 40 seconds, then voice announcement "BPM 标准时间标准频率发播台" ("BPM standard time, standard frequency transmission station") twice for 20 seconds. |

| MHz | UTC       | China Standard Time |
|-----|-----------|---------------------|
| 2.5 | 7:30-1:00 | 15:30-9:00          |
| 5   | 0:00-24:00| 0:00-24:00          |
| 10  | 0:00-24:00| 0:00-24:00          |
| 15  | 1:00-9:00 | 9:00-17:00          |
