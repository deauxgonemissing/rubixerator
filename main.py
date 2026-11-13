#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Rubix cube solver")
    parser.add_argument("cubeSize", type=int, help="#cubes per edge")
    args = parser.parse_args()

    if args.cubeSize < 1:
        parser.error("BECOMETH THE MONOLITH.............FLING PAST JUPITER...................................................FOR THE SOLVE OF THE CUBE PASSES THE EVENT HORIZON")

    print("solved!")

if __name__ == "__main__":
    main()

