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
class MediaDataBox(Box):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘mdat’
    Container:   File
    Mandatory:   No
    Quantity:   Zero	or	more
    """

    def __init__(self):
        super(MediaDataBox, self).__init__()

    def parse(self, reader):
        super(MediaDataBox, self).parse(reader)
        self.to_box_end(reader)

    def print_box(self):
        super(MediaDataBox, self).print_box()


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
