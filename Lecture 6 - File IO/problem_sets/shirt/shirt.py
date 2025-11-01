import sys
import os
from PIL import Image, ImageOps

def main() -> None:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file, output_file = sys.argv[1], sys.argv[2]

    name1, ext1 = os.path.splitext(input_file)
    name2, ext2 = os.path.splitext(output_file)
    ext1 = ext1.lower()
    ext2 = ext2.lower()


    if ext2 not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    if not os.path.exists(input_file):
        sys.exit("Input does not exist")

    try:
        put_shirt(input_file, output_file)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

def put_shirt(input_file: str, output_file: str) -> None:
    img = Image.open(input_file)
    img_shirt = Image.open("shirt.png")
    size = img_shirt.size
    resized_photo = ImageOps.fit(img, size)
    resized_photo.paste(img_shirt, (0, 0), img_shirt)
    resized_photo.save(output_file)

if __name__ == "__main__":
    main()
