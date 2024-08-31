<div align="center">
  <img src="docs/assets/logo_large_black.svg" alt="Logo" width="400">
</div>

<div align="center">

  ![GitHub Release](https://img.shields.io/github/v/release/AresValley/Artemis-DB?label=Latest%20DB)
  ![GitHub repo file or directory count (in path)](https://img.shields.io/github/directory-file-count/aresvalley/artemis-db/static?type=dir&label=Recognized%20Signals)
  ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/AresValley/Artemis-DB/total?label=DB%20requests&color=blue)
  ![GitHub Release Date](https://img.shields.io/github/release-date/AresValley/Artemis-DB?label=DB%20Latest%20Release&color=blue)

</div>

This repository is used to store the last version of the SigId wiki database for [Artemis](https://github.com/AresValley/Artemis) and its crawler.

> [!IMPORTANT]  
> The repository is intended for internal use only. However, if bugs/errors are present in the database or if you have suggestions for additions and changes to any signal record, we encourage you to open an issue

## Media

### Waterfall/Spectrum (FFT)
The image is converted to **png** format. The resolution is arbitrary (yet).

### Audio Sample
The standard format of an audio sample is **ogg** with a sampling rate equal to the original recording. The audio codec depends on the native format:

- **vorbis**, if the original audio is compressed
- **flac**, if the original audio is lossless

To keep the total DB size within reasonable limits, the audio sample duration is limited to 1 minute (60 seconds). This is more than enough for recognition 'by ear' and analytical audio analysis.

## License
Artemis is licensed under the [**GPL-3**](https://github.com/AresValley/Artemis/blob/master/LICENSE) license. 
