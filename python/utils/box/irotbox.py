# -----------------------------------
# import
# -----------------------------------
from utils.box.item_property import ItemProperty


# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------
class ItemRotation(ItemProperty):
    """
    ISO/IEC 23008-12
    Box Type: ‘irot’
    """

    def __init__(self):
        super(ItemRotation, self).__init__()
        self.angle = None

    def parse(self, reader):
        super(ItemRotation, self).parse(reader)

        tmp = reader.read8()
        self.angle = (tmp & 0x3)
        assert self.read_complete(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(ItemRotation, self).print_box()
        print("angle :", self.angle)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
