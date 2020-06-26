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


class TrackHeaderBox(FullBox):
    """
    ISO/IEC 14496-12
    Box Type: ‘tkhd’
    Container: Track Box('trak')
    Mandatory: Yes
    Quantity: Exactly one
    """

    def __init__(self):
        super(TrackHeaderBox, self).__init__()
        self.creation_time = None
        self.modification_time = None
        self.track_ID = None
        self.duration = None
        self.layer = None
        self.alternate_group = None
        self.volume = None
        self.matrix = None
        self.width = None
        self.height = None

    def parse(self, reader):
        super(TrackHeaderBox, self).parse(reader)

        if self.version == 1:
            self.creation_time = reader.read64()
            self.modification_time = reader.read64()
            self.track_ID = reader.read32()
            reader.read32()  # reserved
            self.duration = reader.read64()
        else:
            self.creation_time = reader.read32()
            self.modification_time = reader.read32()
            self.track_ID = reader.read32()
            reader.read32()  # reserved
            self.duration = reader.read32()

        reader.read32()  # reserved
        reader.read32()  # reserved

        self.layer = reader.read16()
        self.alternate_group = reader.read16()
        self.volume = reader.read16()

        reader.read16()  # reserved

        self.matrix = []
        for _ in range(9):
            self.matrix.append(reader.read32())

        self.width = reader.read32()
        self.height = reader.read32()

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(TrackHeaderBox, self).print_box()
        print("creation_time     :", self.creation_time)
        print("modification_time :", self.modification_time)
        print("track_ID          :", self.track_ID)
        print("duration          :", self.duration)
        print("layer             :", self.layer)
        print("alternate_group   :", self.alternate_group)
        print("volume            :", self.volume)
        print("matrix            :", self.matrix)
        print("width             :", self.width >> 16)
        print("height            :", self.height >> 16)

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass