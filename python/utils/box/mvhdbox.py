# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box
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
class MovieHeaderBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘mvhd’
    Container:   Movie Box (‘moov’)
    Mandatory:   Yes
    Quantity:   Exactly One
    """

    def __init__(self):
        super(MovieHeaderBox, self).__init__()
        self.creation_time = None
        self.modification_time = None
        self.timescale = None
        self.duration = None
        self.rate = None
        self.volume = None
        self.matrix = None
        self.predefined = None
        self.next_track_ID = None

    def parse(self, reader):
        super(MovieHeaderBox, self).parse(reader)

        if self.version == 1:
            self.creation_time = reader.read64()
            self.modification_time = reader.read64()
            self.timescale = reader.read32()
            self.duration = reader.read64()
        else:
            self.creation_time = reader.read32()
            self.modification_time = reader.read32()
            self.timescale = reader.read32()
            self.duration = reader.read32()

        self.rate = reader.read32()
        self.volume = reader.read16()

        reader.read16()  # reserved
        reader.read32()  # reserved
        reader.read32()  # reserved

        self.matrix = []
        for _ in range(9):
            self.matrix.append(reader.read32())

        self.predefined = []
        for _ in range(6):
            self.predefined.append(reader.read32())

        self.next_track_ID = reader.read32()

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)


    def print_box(self):
        super(MovieHeaderBox, self).print_box()
        print("creation_time :", self.creation_time)
        print("modification_time :", self.modification_time)
        print("timescale :", self.timescale)
        print("duration :", self.duration)
        print("rate :", self.rate)
        print("volume :", self.volume)
        print("matrix :", self.matrix)
        print("predefined :", self.predefined)
        print("next_track_ID :", self.next_track_ID)

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass