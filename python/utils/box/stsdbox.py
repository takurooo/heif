# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box
from utils.box.basebox import FullBox
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


class SampleEntry(Box):

    def __init__(self):
        super(SampleEntry, self).__init__()
        self.data_reference_index = None

    def parse(self, reader):
        super(SampleEntry, self).parse(reader)

        for _ in range(6):
            _ = reader.read8()  # reserved=0
        self.data_reference_index = reader.read16()

    def print_box(self):
        print("data_reference_index :", self.data_reference_index)


class AudioSampleEntry(SampleEntry):

    def __init__(self):
        super(AudioSampleEntry, self).__init__()
        self.channelcount = None
        self.samplesize = None
        self.pre_defined = None
        self.samplerate = None

    def parse(self, reader):
        super(AudioSampleEntry, self).parse(reader)

        for _ in range(2):
            _ = reader.read32()  # reserved=0

        self.channelcount = reader.read16()
        self.samplesize = reader.read16()
        self.pre_defined = reader.read16()
        self.samplerate = reader.read32()

        self.to_box_end(reader)  # TODO

    def print_box(self):
        print("channelcount :", self.channelcount)
        print("samplesize   :", self.samplesize)
        print("samplerate   :", self.samplerate)


class SampleDescriptionBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘stsd’
    Container:   Sample Table Box (‘stbl’)
    Mandatory:   Yes
    Quantity:   Exactly one
    """

    def __init__(self):
        super(SampleDescriptionBox, self).__init__()
        self.avc1 = None
        self.twos = None
        self.ipcm = None
        self.rtmd = None

    def parse(self, reader):
        super(SampleDescriptionBox, self).parse(reader)

        self.entry_count = reader.read32()
        for _ in range(self.entry_count):
            box_size, box_type = boxutils.read_box_header(reader)
            # print(box_type)
            if box_type == 'avc1':  # Advanced Video Coding
                reader.seek(box_size, 1) # TODO avc1
            elif box_type == 'twos':  # Uncompressed 16-bit audio
                self.twos = AudioSampleEntry()
                self.twos.parse(reader)
            elif box_type == 'ipcm':
                self.ipcm = AudioSampleEntry()
                self.ipcm.parse(reader)
            elif box_type == 'rtmd':  # Real Time Metadata Sample Entry(XAVC Format)
                reader.seek(box_size, 1)  # TODO rtmd
            else:
                reader.seek(box_size, 1)

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(SampleDescriptionBox, self).print_box()
        if self.avc1 is not None:
            self.avc1.print_box()
        if self.twos is not None:
            self.twos.print_box()
        if self.ipcm is not None:
            self.ipcm.print_box()
        if self.rtmd is not None:
            self.rtmd.print_box()


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass