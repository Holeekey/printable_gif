import argparse
import os
from image_helpers import *

def main():
    parser = argparse.ArgumentParser(description="Process GIF file to print it")
    parser.add_argument("--path", type=str, required=True, help="GIF file path")
    parser.add_argument("--frames", type=int, default=5, help="Frames to extract")
    parser.add_argument("--output", type=str, default="./output", help="Output folder")
    parser.add_argument("--interval", type=float, default=1, help="Interval between images in mm")

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)

    frames: list[Image.Image] = extract_frames(args.path, args.frames)
    combined_image = combine_images(frames, mm_to_px(args.interval))
    combined_image.save(args.output + '/combined.png')

if __name__ == "__main__":
    main()