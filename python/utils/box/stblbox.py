# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box
from utils.box.basebox import FullBox
from utils.box.stsdbox import SampleDescriptionBox
from utils.box.sttsbox import DecodingTimeToSampleBox
from utils.box.cttsbox import CompositionTimeToSample
from utils.box.stscbox import SampleToChunkBox
from utils.box.stszbox import SampleSizeBox
from utils.box.stcobox import ChunkOffsetBox
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


class SampleTableBox(Box):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘stbl’
    Container:   Media Information Box (‘minf’)
    Mandatory:   Yes
    Quantity:   Exactly one
    """

    def __init__(self):
        super(SampleTableBox, self).__init__()
        self.stsd = None
        self.stts = None
        self.ctts = None
        self.stsc = None
        self.stsz = None
        self.stco = None

    def parse(self, reader):
        super(SampleTableBox, self).parse(reader)

        while not self.read_box_done(reader):
            box_size, box_type = boxutils.read_box_header(reader)
            # print(f" {box_type}")
            if box_type == 'stsd':
                self.stsd = SampleDescriptionBox()
                self.stsd.parse(reader)
            elif box_type == 'stts':
                self.stts = DecodingTimeToSampleBox()
                self.stts.parse(reader)
            elif box_type == 'ctts':
                self.ctts = CompositionTimeToSample()
                self.ctts.parse(reader)
            elif box_type == 'stsc':
                self.stsc = SampleToChunkBox()
                self.stsc.parse(reader)
            elif box_type == 'stsz':
                self.stsz = SampleSizeBox()
                self.stsz.parse(reader)
            elif box_type == 'stco' or box_type == 'co64':
                self.stco = ChunkOffsetBox()
                self.stco.parse(reader)
            else:
                reader.seek(box_size, 1)

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(SampleTableBox, self).print_box()
        if self.stsd is not None:
            self.stsd.print_box()
        if self.stts is not None:
            self.stts.print_box()
        if self.ctts is not None:
            self.ctts.print_box()
        if self.stsc is not None:
            self.stsc.print_box()
        if self.stsz is not None:
            self.stsz.print_box()
        if self.stco is not None:
            self.stco.print_box()


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
