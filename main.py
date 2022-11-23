from PIL import Image
def merge(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

def roll(im, delta):
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im

print("Welcome to the photo editor. We have three photos for to choose from to edit.")
peakock = Image.open(r"C:\Users\joseschu\Pictures\image.jpg")
tree = Image.open(r"C:\Users\joseschu\Pictures\trees.jfif")
fire = Image.open(r"C:\Users\joseschu\Pictures\Fire.jpg")
print(peakock.format, peakock.size, peakock.mode)
#  peakock.show()
box = (400, 400, 900, 900)
region = peakock.crop(box)
#  region.show()
#  merge(tree, fire).show()
r, g, b = peakock.split()
peakock = Image.merge("RGB", (g, b, r))
out = peakock.resize((233, 128))
out = peakock.rotate(45)  # degrees counter-clockwise
out = peakock.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
out = peakock.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
out = peakock.transpose(Image.Transpose.ROTATE_90)
out = peakock.transpose(Image.Transpose.ROTATE_180)
out = peakock.transpose(Image.Transpose.ROTATE_270)
fire = fire.convert("L")
