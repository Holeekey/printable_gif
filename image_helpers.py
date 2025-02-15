from PIL import Image, ImageDraw

def mm_to_px(mm:float) -> float:
    return mm * 3.77952756

def extract_frames(gif_path: str, frames_quantity: int, offset: int = 0) -> list[Image.Image]:
    frames = []
    
    with Image.open(gif_path) as img:
        if img.n_frames < frames_quantity + offset:
            raise ValueError(f"Frames quantity exceeded, given gif only has {img.n_frames} frames")
        range_n = range(offset, min(frames_quantity + offset, img.n_frames))
        for frame in range_n:
            img.seek(frame)
            frame_image = img.copy().convert("RGBA")
            frames.append(frame_image)
            
    return frames

def draw_transparent_rectangle(image: Image.Image, x: int, y: int, width: int, height:int, color: tuple = (0, 0, 0, 0), outline: tuple = (0, 0, 0, 0)):
    draw = ImageDraw.Draw(image)
    draw.rectangle([x, y, width, height], fill=color, outline=outline)

def cut_image(image: Image.Image, x: int, cut_width_px: int):
    draw_transparent_rectangle(image, x, 0, x + cut_width_px, image.height)

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
        
def slice_moving_frame(
    image: Image.Image,
    x: int,
    y:int,
    width:int,
    height:int,
    slice_separation_px: int, 
    slice_width_px:int
):
    image_width_travelled = x
    while True:
        draw_transparent_rectangle(
            image=image,
            x= image_width_travelled,
            y= y,
            width= image_width_travelled + slice_width_px - 1,
            height= y + height,
            color=(0, 0, 0, 0),
            outline=(255,255,0,255)
        )
        
        image_width_travelled += slice_separation_px + slice_width_px
        if image_width_travelled < x + width:
            continue
        else:
            break
    
    
def overlay_images(image1: Image.Image, image2: Image.Image, position: tuple = (0,0), size = None) -> Image.Image:
    
    bigger_image = 1 if image1.width > image2.width else 2
    
    if not size:
        size = image1.size if image1.width > image2.width else image2.size
    
    combined_image = Image.new('RGBA', image1.size)
    combined_image.paste(image1, (0, 0) if bigger_image == 1 else position, image1)
    combined_image.paste(image2, (0, 0) if bigger_image == 2 else position, image2)
    
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