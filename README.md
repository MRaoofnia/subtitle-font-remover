# subtitle-font-remover
Remove embded fonts from .ass subtitles 

## Why remove fonts?
Subtitles with`.ass` file format can are able to contain fonts within themselves. Some video players( like kodi) doesn't support embded fonts and it may cause them to be unable to open this subtitles. And maybe some users prefer to use their system's default font.

So this tool removes `[Fonts]` section from `.ass` subtitle file.

## Usage
Simply use this script using:
```bash
python3 sourcefile
# or
python3 sourcefile destinationfile
```
