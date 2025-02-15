import argparse
import os
from image_helpers import *
from pdf_helpers import *

def main():
    parser = argparse.ArgumentParser(description="Process GIF file to print it")
    parser.add_argument("--path", type=str, required=True, help="GIF file path")
    parser.add_argument("--frames", type=int, default=5, help="Frames to extract")
    parser.add_argument("--offset", type=int, default=0, help="Frames to skip")
    parser.add_argument("--output", type=str, default="./output", help="Output folder")
    parser.add_argument("--interval", type=float, default=1, help="Interval between images in mm")
    parser.add_argument("--hm", type=int, default=30, help="Horizontal margin in mm")
    parser.add_argument("--vm", type=int, default=10, help="Vertical margin in mm")
    parser.add_argument("--extension", type=float, default=1.5, help="Frame extension in relation to gif width")


    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    
    file_name = os.path.splitext(os.path.basename(args.path))[0]

    frames: list[Image.Image] = extract_frames(args.path, args.frames, args.offset)
    combined_image = combine_images(frames, mm_to_px(args.interval))
    combined_image_path = os.path.join(args.output, f'{file_name}_combined.png')
    combined_image.save(combined_image_path)
    
    horizontal_margin = args.hm
    vertical_margin = args.vm
    
    moving_frame = Image.new(
        'RGBA',
        (round(frames[0].width * args.extension) + horizontal_margin * 2, frames[0].height + vertical_margin * 2),
        (0, 0, 0, 0)
    )
    
    slice_moving_frame(
        image=moving_frame,
        x=horizontal_margin,
        y=vertical_margin,
        width=round(frames[0].width * args.extension),
        height=frames[0].height,
        slice_width_px=mm_to_px(args.interval),
        slice_separation_px=mm_to_px(args.frames - 1)
    )
    
    overlay_image = Image.new(
        'RGBA',
        (moving_frame.width, moving_frame.height),
        (0, 0, 0, 0)
    )
    
    overlay_image.paste(combined_image, (horizontal_margin, vertical_margin), combined_image)
    overlay_image.paste(moving_frame, (0, 0), moving_frame)
    
    overlay_image.save(os.path.join(args.output, f'{file_name}_overlay.png'))
    
    moving_frame_path = os.path.join(args.output, f'{file_name}_frame.png')
    moving_frame.save(moving_frame_path)
    
    generate_printable_gif_pdf(
        combined_image_path=combined_image_path,
        moving_frame_path=moving_frame_path,
        pdf_path=os.path.join(args.output, f'{file_name}.pdf')
    )

if __name__ == "__main__":
    main()