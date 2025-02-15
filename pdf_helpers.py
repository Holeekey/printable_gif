from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def generate_printable_gif_pdf (
    moving_frame_path: str,
    combined_image_path: str,
    pdf_path: str
):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    
    with Image.open(moving_frame_path) as img:
        img = img.rotate(90, expand=True) 
        rotated_moving_frame_path = moving_frame_path.replace(".png", "_rotated.png")
        img.save(rotated_moving_frame_path)
        width, height = img.size
        c.drawImage(rotated_moving_frame_path, 40, 0, width, height)
        c.showPage()

    with Image.open(combined_image_path) as img:
        img = img.rotate(90, expand=True) 
        rotated_combined_image_path = combined_image_path.replace(".png", "_rotated.png")
        img.save(rotated_combined_image_path)
        width, height = img.size
        c.drawImage(rotated_combined_image_path, 40, 0, width, height)
        c.showPage()

    c.save()
    
    