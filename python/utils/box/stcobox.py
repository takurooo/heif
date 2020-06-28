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
class ChunkOffsetBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘stco’
    Container:   Sample Table Box (‘stbl’)
    Mandatory:   Yes
    Quantity:   Exactly One variant must be present
    """

    def __init__(self):
        super(ChunkOffsetBox, self).__init__()
        self.entry_count = None
        self.chunk_offset = []

    def parse(self, reader):
        super(ChunkOffsetBox, self).parse(reader)

        self.entry_count = reader.read32()

        if self.get_box_type() == 'stco':
            for i in range(self.entry_count):
                self.chunk_offset.append(reader.read32())
        else:
            # co64
            for i in range(self.entry_count):
                self.chunk_offset.append(reader.read64())

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)


    def print_box(self):
        super(ChunkOffsetBox, self).print_box()
        print("entry_count  :", self.entry_count)
        print("chunk_offset :", self.chunk_offset)

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass