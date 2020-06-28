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
class CompositionTimeToSample(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘ctts’
    Container:   Sample Table Box (‘stbl’)
    Mandatory:   Yes
    Quantity:   Zero or one
    """

    def __init__(self):
        super(CompositionTimeToSample, self).__init__()
        self.entry_count = None
        self.sample_count = []
        self.sample_offset = []

    def parse(self, reader):
        super(CompositionTimeToSample, self).parse(reader)

        self.entry_count = reader.read32()

        if self.version == 0:
            for _ in range(self.entry_count):
                self.sample_count.append(reader.read32())
                self.sample_offset.append(reader.read32())
        elif self.version == 1:
            for _ in range(self.entry_count):
                self.sample_count.append(reader.read32())
                self.sample_offset.append(reader.read32(signed=True))

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)


    def print_box(self):
        super(CompositionTimeToSample, self).print_box()
        print("entry_count   :", self.entry_count)
        print("sample_count  :", self.sample_count)
        print("sample_offset :", self.sample_offset)

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass