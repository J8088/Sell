import os, sys
from PIL import Image


def prevent_rotation():
    image = Image.open("/Sell/media/product_photos/IMG_2201.JPG")
    if hasattr(image, '_getexif'):
        orientation = 0x0112
        exif = image._getexif()
        if exif is not None:
            orientation = exif[orientation]
            rotations = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            if orientation in rotations:
                image = image.transpose(rotations[orientation])
    image.save('/Sell/media/product_photos/IMG_2201.JPG')


def crop_images():
    #TODO should be adjusted to the sell requirements
    size = 2016, 2016

    for infile in sys.argv[1:]:
        outfile = os.path.splitext(infile)[0] + ".JPG"
        if infile != outfile:
            try:
                im = Image.open(infile)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(outfile, "JPG")
            except IOError:
                print("cannot create JPG for '%s'" % infile)


def crop_image():
    # Coordinates are (left, upper, right, lower).
    # The Python Imaging Library uses a coordinate system with (0, 0) in the upper left corner.
    # https://pillow.readthedocs.io/en/5.3.x/handbook/tutorial.html?highlight=crop#cutting-pasting-and-merging-images
    infile = "/Sell/media/product_photos/DSC_0183.JPG"
    outfile = "/Sell/media/product_photos/DSC_0183.JPG"

    try:
        im = Image.open(infile)
        width, height = im.size
        left = (width - height)/2
        top = 0
        right = height + (width - height)/2
        bottom = height
        print("__file__={0}, ==> () => {1}".format(__file__, (left, top, right, bottom)))
        croped = im.crop((left, top, right, bottom))
        print('CROPPED SIZE: ' + str(croped.size))
        # croped.show()
        croped.save(outfile)
    except IOError:
        print("cannot create JPG for '%s'" % infile)


def make_transparent():
    infile='/Users/ij/Projects/development/Sell/media/product_photos/IMG_2201.JPG'
    image = Image.open(infile)
    width, height = image.size
    new_width = 512
    image.convert("RGBA")  # Convert this to RGBA if possible
    canvas = Image.new('RGBA', image.size, (0, 0, 0, 0))
    # canvas.paste(image, mask=image)
    canvas.paste(image, (0, 0))
    # canvas.thumbnail([width, height], Image.ANTIALIAS)
    canvas.show()


def adjust():
    infile = '/Users/ij/Projects/development/Sell/media/product_photos/IMG_2201.JPG'
    image = Image.open(infile)
    image = image.convert('RGBA')
    width, height = image.size
    new_width = 512
    new_height = 512
    image = image.resize((new_width, new_height), resample=Image.ANTIALIAS)
    new_image = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    upper = 250
    new_image.paste(image, (0, upper))
    new_image.show()

if __name__ == '__main__':
    """
    run your function
    """
    adjust()
    # make_transparent()

