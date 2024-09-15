# BLOCK-RECOVERY RATE HELPER

This is a simple program that analyzes your Mario & Luigi: Dream Team save file and tells you exactly which blocks you've missed so you can finally achieve a 100% Block-Recovery Rate. To use it, download the .zip file under Releases (no need to download the .xlsx file), extract it, run BRRHelper, point it to your save file, and it will give you images showing exactly where your missing blocks are.

If you are making a program involving the blocks, such as a save file editor, there is a spreadsheet in Releases listing the byte address and bit value of every block. Unfortunately, there are some formatting errors because I exported from Google Sheets, but it is still usable. Camera blocks are included because I did them before I knew exactly which kinds of blocks contribute to BRR.

Have any questions, or the program says you collected all 681 blocks even though you know for a fact you didn't? Contact me on Discord: 7Cs_

Credit to the Super Mario Wiki for images of block locations:
- [List of real world blocks in Mario & Luigi: Dream Team](https://www.mariowiki.com/List_of_real_world_blocks_in_Mario_%26_Luigi:_Dream_Team)
- [List of dream world blocks in Mario & Luigi: Dream Team](https://www.mariowiki.com/List_of_Dream_World_blocks_in_Mario_%26_Luigi:_Dream_Team_)


## How to Get Your Save File

Keep in mind whether your save file was in the first or second slot in the ingame menu. If it was in the first, it will be named 'ML4_001.sav', if it was in the second, 'ML4_002.sav'.

### 3DS

To get a save file stored on a 3DS, you will need to install custom firmware on your console. This is not a difficult process at all. For information on how to install, look at: [3DS Hacks Guide](https://3ds.hacks.guide/).

To extract your save file, follow this guide: [Export Saves](https://wiki.hacks.guide/wiki/3DS:Export_saves).

### Emulation

To get your save file using Citra:

1. Open Citra and right-click on **Mario & Luigi: Dream Team**.
2. Click on **Open Save Data Location**.

For some unknown reason, Lime3DS has removed the "Open Save Data Location" option. I'm not sure if there's any other way to get to the save files via the emulator, so here are the default file paths:

- **Linux:** /home/user/.local/share/Lime3DS/sdmc/Nintendo 3DS/00000000000000000000000000000000/00000000000000000000000000000000/title/00040000/000d5a00/data/00000001/ML4_00(1 or 2).sav

- **Windows:** C:\Users\user\AppData\Roaming\Lime3DS\sdmc\Nintendo 3DS\00000000000000000000000000000000\00000000000000000000000000000000\title\00040000\000d5a00\data\00000001\ML4_00(1 or 2).sav

I recommend moving your save file to a more easily accessible place, like your desktop or Downloads folder.
