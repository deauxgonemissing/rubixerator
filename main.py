#!/usr/bin/env python3
from dialog import Dialog

def main():
    d = Dialog(dialog="dialog")

    while True:
        code, text = d.Inputbox("Edge length, # of cubes:", init="3")

        if code != d.OK:
            return

        try:
            cube_size = int(text)
        except ValueError:
            d.msgbox("need whole number")
            continue

        if cube_size < 1:
            parser.error("BECOMETH THE MONOLITH.............FLING PAST JUPITER...................................................FOR THE SOLVE OF THE CUBE PASSES THE EVENT HORIZON")

        break

    d.msgbox(f"Cube size {cube_size}: solved!")

if __name__ == "__main__":
    main()

