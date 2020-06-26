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
class SampleToChunkBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘stsc’
    Container:   Sample Table Box (‘stbl’)
    Mandatory:   Yes
    Quantity:   Exactly One
    """

    def __init__(self):
        super(SampleToChunkBox, self).__init__()
        self.entry_count = None
        self.first_chunk = []
        self.samples_per_chunk = []
        self.sample_description_index = []

    def parse(self, reader):
        super(SampleToChunkBox, self).parse(reader)

        self.entry_count = reader.read32()

        for _ in range(self.entry_count):
            self.first_chunk.append(reader.read32())
            self.samples_per_chunk.append(reader.read32())
            self.sample_description_index.append(reader.read32())

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(SampleToChunkBox, self).print_box()
        print("entry_count              :", self.entry_count)
        print("first_chunk              :", self.first_chunk)
        print("samples_per_chunk        :", self.samples_per_chunk)
        print("sample_description_index :", self.sample_description_index)

    def get_samples_per_chunk(self, chunk_idx):
        chunk_no = chunk_idx + 1
        for i in range(self.entry_count):
            if chunk_no < self.first_chunk[i]:
                samples_per_chunk = self.samples_per_chunk[i - 1]
                break
        else:
            samples_per_chunk = self.samples_per_chunk[-1]

        return samples_per_chunk
# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
