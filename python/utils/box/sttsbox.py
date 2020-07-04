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
class DecodingTimeToSampleBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘stts’
    Container:   Sample Table Box (‘stbl’)
    Mandatory:   Yes
    Quantity:   Exactly one
    """

    def __init__(self):
        super(DecodingTimeToSampleBox, self).__init__()
        self.entry_count = None
        self.sample_count = []
        self.sample_delta = []

    def parse(self, reader):
        super(DecodingTimeToSampleBox, self).parse(reader)

        self.entry_count = reader.read32()

        for _ in range(self.entry_count):
            self.sample_count.append(reader.read32())
            self.sample_delta.append(reader.read32())

        assert self.read_complete(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(DecodingTimeToSampleBox, self).print_box()
        print("entry_count   :", self.entry_count)
        print("sample_count  :", self.sample_count)
        print("sample_delta  :", self.sample_delta)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
