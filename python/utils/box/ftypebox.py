# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box


# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------
class FileTypeBox(Box):
    """
    ISO/IEC 14496-12
    Box Type: `ftyp’
    Container: File
    Mandatory: Yes
    Quantity: Exactly one
    """

    def __init__(self):
        super(FileTypeBox, self).__init__()
        self.major_brand = None
        self.minor_version = None
        self.compatible_brands = None

    def parse(self, reader):
        super(FileTypeBox, self).parse(reader)
        self.major_brand = reader.read32('big', decode=False)
        self.minor_version = reader.read32('big', decode=False)

        self.compatible_brands = []

        while not self.read_box_done(reader):
            self.compatible_brands.append(reader.read32('big', decode=True))

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(FileTypeBox, self).print_box()
        print("major_brand :", self.major_brand)
        print("minor_version :", self.minor_version)
        print("compatible_brands :", self.compatible_brands)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass