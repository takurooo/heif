# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box
from utils.box.basebox import FullBox
from utils.box.vmhdbox import VideoMediaHeaderBox
from utils.box.smhdbox import SoundMediaHeaderBox
from utils.box.hmhdbox import HintMediaHeaderBox
from utils.box.stblbox import SampleTableBox
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


class MediaInformationBox(Box):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘minf’
    Container:   Media Box (‘mdia’)
    Mandatory:   Yes
    Quantity:   Exactly one
    """

    def __init__(self):
        super(MediaInformationBox, self).__init__()
        self.vmhd = None
        self.smhd = None
        self.hmhd = None
        self.sthd = None
        self.nmhd = None
        self.dinf = None
        self.dref = None
        self.stbl = None

    def parse(self, reader):
        super(MediaInformationBox, self).parse(reader)

        while not self.read_box_done(reader):
            box_size, box_type = boxutils.read_box_header(reader)

            if box_type == 'vmhd':
                self.vmhd = VideoMediaHeaderBox()
                self.vmhd.parse(reader)
            elif box_type == 'smhd':
                self.smhd = SoundMediaHeaderBox()
                self.smhd.parse(reader)
            elif box_type == 'hmhd':
                self.hmhd = HintMediaHeaderBox()
                self.hmhd.parse(reader)
            elif box_type == 'sthd':
                reader.seek(box_size, 1)  # TODO sthd
            elif box_type == 'nmhd':
                reader.seek(box_size, 1)  # TODO nmhd
            elif box_type == 'dinf':
                reader.seek(box_size, 1)  # TODO dinf
            elif box_type == 'dref':
                reader.seek(box_size, 1)  # TODO dref
            elif box_type == 'stbl':
                self.stbl = SampleTableBox()
                self.stbl.parse(reader)
            else:
                reader.seek(box_size, 1)

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(MediaInformationBox, self).print_box()
        if self.vmhd is not None:
            self.vmhd.print_box()
        if self.smhd is not None:
            self.smhd.print_box()
        if self.hmhd is not None:
            self.hmhd.print_box()
        if self.stbl is not None:
            self.stbl.print_box()

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
