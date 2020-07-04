# -----------------------------------
# import
# -----------------------------------
from utils.box.item_property import ItemFullProperty


# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------
class ImageSpatialExtentsProperty(ItemFullProperty):
    """
    ISO/IEC 23008-12
    Box Type: ‘ispe’
    """

    def __init__(self):
        super(ImageSpatialExtentsProperty, self).__init__()
        self.image_width = None
        self.image_height = None

    def parse(self, reader):
        super(ImageSpatialExtentsProperty, self).parse(reader)

        self.image_width = reader.read32()
        self.image_height = reader.read32()
        assert self.read_complete(reader), '{} num bytes left not 0.'.format(self.type)

    def get_image_width_height(self):
        return self.image_width, self.image_height

    def print_box(self):
        super(ImageSpatialExtentsProperty, self).print_box()
        print("image_width  :", self.image_width)
        print("image_height :", self.image_height)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
