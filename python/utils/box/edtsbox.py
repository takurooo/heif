# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box
from utils.box.basebox import FullBox
from utils.box.elstbox import EditListBox
from utils.box import boxutils

# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------
class EditBox(Box):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘edts’
    Container:   Track Box (‘trak’)
    Mandatory:   No
    Quantity:   Zero or one
    """

    def __init__(self):
        super(EditBox, self).__init__()
        self.elst = None

    def parse(self, reader):
        super(EditBox, self).parse(reader)

        while not self.read_box_done(reader):
            box_size, box_type = boxutils.read_box_header(reader)

            if box_type == 'elst':
                self.elst = EditListBox()
                self.elst.parse(reader)
            else:
                reader.seek(box_size, 1)

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(EditBox, self).print_box()
        if self.elst is not None:
            self.elst.print_box()


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
