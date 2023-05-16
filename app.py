import argparse
import os
from PIL import ImageColor, Image, ImageDraw, ImageFont
import time
from tqdm import tqdm

def generate_plain_image(width, height, color):
    try:
        # Set up tqdm progress bar
        pbar = tqdm(total=width * height, desc='Generating plain image', unit='pixels')

        rgb_color = ImageColor.getrgb(color)
        image = Image.new('RGB', (width, height), rgb_color)

        # Add dimensions text to the image
        draw = ImageDraw.Draw(image)
        text = f'{width}x{height}'
        font_path = os.path.join('assets', 'arial.ttf')  # Path to the font file
        
        # Adjust the font size based on image size
        font_size = max(int(min(width, height) / 20), 10)
        font = ImageFont.truetype(font_path, font_size)
        
        text_width, text_height = draw.textsize(text, font)
        text_position = ((width - text_width) // 2, (height - text_height) // 2)
        draw.text(text_position, text, fill='black', font=font)

        output_dir = 'output'   # Output directory path
        os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

        timestamp = int(time.time())
        filename = f'plain_image_{timestamp}.jpg'  # Unique filename with timestamp
        filepath = os.path.join(output_dir, filename)  # Output file path

        # Iterate over each pixel and update the tqdm progress bar
        for i in range(width):
            for j in range(height):
                image.putpixel((i, j), rgb_color)
                pbar.update(1)
        pbar.close()

        image.save(filepath)  # Save the image as JPEG
        print("Image filepath:", filename)
    except ValueError as e:
        print("Invalid color name:", str(e))
    except Exception as e:
        print("Error generating plain image:", str(e))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a plain color image.')
    parser.add_argument('--width', type=int, default=300, help='Width of the image')
    parser.add_argument('--height', type=int, default=300, help='Height of the image')
    parser.add_argument('--color', default='gray', help='Color of the image')
    args = parser.parse_args()

    generate_plain_image(args.width, args.height, args.color)
