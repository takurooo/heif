# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import FullBox

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
        self.item_ID = None

    def parse(self, reader):
        super(PrimaryItemBox, self).parse(reader)

        self.item_ID = reader.read16('big')
        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def get_primary_item_id(self):
        return self.item_ID

    def print_box(self):
        super(PrimaryItemBox, self).print_box()
        print('item_ID :', self.item_ID)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass