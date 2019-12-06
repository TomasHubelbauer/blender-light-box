# Blender Light Box

![](https://github.com/tomashubelbauer/blender-light-box/workflows/render/badge.svg)

![](text_0000.png)

## Development

Use Visual Studio Code and open `script.py`.
Split the editor into two columns and open `text_0000.png` next.
Open the integrated terminal of VS Code and run:

`blender --background light-box.blend --python script.py --render-output //text_ --engine $ENGINE --render-format PNG --use-extension 1 --render-frame 0`

Replace `$ENGINE` with `CYCLES` or `BLENDER_EEVEE`.
List all available engines using `blender --background --engine help`.

Make changes to `python.py` and rerun the command above.
Watch `text_0000.png` to refresh in the VS Code preview.

Remove `--background` from the command to open Blender and debug issues.
Use the same to save a Blend file with the cards solidified in.

## To-Do

### Center the letters within the cards

### Center the card chain within the line

### Discard cards which would put the card chain over the line size

Probably error out in the Python script.

### Assing a correct translucent material to the card plan
