from PIL import Image, ImageDraw

def mm_to_px(mm:float) -> float:
    return mm * 3.77952756

def extract_frames(gif_path: str, frames_quantity: int) -> list[Image.Image]:
    frames = []
    
    with Image.open(gif_path) as img:
        if img.n_frames < frames_quantity:
            raise ValueError(f"Frames quantity exceeded, given gif only has {img.n_frames} frames")
        for frame in range(min(frames_quantity, img.n_frames)):
            img.seek(frame)
            frame_image = img.copy().convert("RGBA")
            frames.append(frame_image)
            
    return frames

def cut_image(image: Image.Image, x: int, cut_width_px: int):
    draw = ImageDraw.Draw(image)
    draw.rectangle([x, 0, x + cut_width_px, image.height], fill=(0, 0, 0, 0))

def slice_image(image: Image.Image, slice_separation_px: int, slice_width_px:int, x_offset: int = 0) -> Image.Image:
    image_width = image.width
    image_width_travelled = -x_offset
    while True:
        cut_image(image, image_width_travelled, slice_width_px - 1)
        image_width_travelled += slice_separation_px + slice_width_px
        if image_width_travelled < image_width:
            continue
        else:
            break
        
def overlay_images(image1: Image.Image, image2: Image.Image) -> Image.Image:
    combined_image = Image.new('RGBA', image1.size)
    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, 0), image2)
    
    return combined_image
        
def combine_images(images: list[Image.Image], image_interval_width_px: int) -> Image.Image:
    image_quantity = len(images)
    for index, image in enumerate(images):
        slice_image(
            image=image,
            slice_separation_px=image_interval_width_px,
            slice_width_px=image_interval_width_px * (image_quantity - 1),
            x_offset=mm_to_px(index)
        )
    combined_image = Image.new('RGBA', images[0].size)
    for index in range(image_quantity):
        combined_image = overlay_images(images[index], combined_image)
    return combined_image   