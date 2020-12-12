# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import FullBox
from utils.file.binaryfilereader import BinaryFileReader


# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------


class PrimaryItemBox(FullBox):
    """
    Box Type: ‘pitm’
    Container: Meta box (‘meta’)
    Mandatory: No
    Quantity: Zero or one
    """

    def __init__(self):
        super(PrimaryItemBox, self).__init__()
        self.item_ID = 0

    def parse(self, reader: BinaryFileReader) -> None:
        super(PrimaryItemBox, self).parse(reader)

        self.item_ID = reader.read16()
        assert self.read_complete(
            reader), '{} num bytes left not 0.'.format(self.type)

    def get_primary_item_id(self) -> int:
        return self.item_ID

    def print_box(self) -> None:
        super(PrimaryItemBox, self).print_box()
        print('item_ID :', self.item_ID)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
