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
        self.major_brand = reader.read32(decode=True)
        self.minor_version = reader.read32(decode=False)

        self.compatible_brands = []
        while not self.read_complete(reader):
            self.compatible_brands.append(reader.read32(decode=True))

        assert self.read_complete(reader), '{} num bytes left not 0.'.format(self.type)

    def get_major_brand(self):
        return self.major_brand

    def get_minor_version(self):
        return self.minor_version

    def get_compatible_brands(self):
        return self.compatible_brands

    def print_box(self):
        super(FileTypeBox, self).print_box()
        print("major_brand       :", self.major_brand)
        print("minor_version     :", self.minor_version)
        print("compatible_brands :", self.compatible_brands)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
