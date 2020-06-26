# -----------------------------------
# import
# -----------------------------------
from collections import OrderedDict

from utils.box.basebox import Box
from utils.box.mvhdbox import MovieHeaderBox
from utils.box.trackbox import TrackBox
from utils.box.edtsbox import EditBox

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
class MovieBox(Box):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘moov’
    Container:   File
    Mandatory:   Yes
    Quantity:   Exactly One
    """

    def __init__(self):
        super(MovieBox, self).__init__()
        self.mvhd = None
        self.trak = []

    def parse(self, reader):
        super(MovieBox, self).parse(reader)
        while not self.read_box_done(reader):
            box_size, box_type = boxutils.read_box_header(reader)
            if box_type == 'mvhd':
                self.mvhd = MovieHeaderBox()
                self.mvhd.parse(reader)
            elif box_type == 'trak':
                trak = TrackBox()
                trak.parse(reader)
                self.trak.append(trak)
            else:
                reader.seek(box_size, 1)

    def print_box(self):
        super(MovieBox, self).print_box()
        if self.mvhd is not None:
            self.mvhd.print_box()
        for trak in self.trak:
            trak.print_box()


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
