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
class MediaHeaderBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘mdhd’
    Container:   Media Box (‘mdia’)
    Mandatory:   Yes
    Quantity:   Exactly One
    """

    def __init__(self):
        super(MediaHeaderBox, self).__init__()
        self.creation_time = None
        self.modification_time = None
        self.timescale = None
        self.duration = None
        self.pad = None
        self.language = []
        self.pre_defined = None

    def parse(self, reader):
        super(MediaHeaderBox, self).parse(reader)

        if self.get_version() == 1:
            self.creation_time = reader.read64()
            self.modification_time = reader.read64()
            self.timescale = reader.read32()
            self.duration = reader.read64()
        else:
            self.creation_time = reader.read32()
            self.modification_time = reader.read32()
            self.timescale = reader.read32()
            self.duration = reader.read32()

        self.pad = reader.readbits(1)
        for _ in range(3):
            self.language.append(reader.readbits(5))
        self.pre_defined = reader.read16()

        assert self.read_complete(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(MediaHeaderBox, self).print_box()
        print("creation_time     :", self.creation_time)
        print("modification_time :", self.modification_time)
        print("timescale         :", self.timescale)
        print("duration          :", self.duration)
        print("pad               :", self.pad)
        print("language          :", self.language)
        print("pre_defined       :", self.pre_defined)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
