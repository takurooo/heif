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
class EditListEntry:

    def __init__(self):
        self.segment_duration = None
        self.media_time = None
        self.media_rate_integer = None
        self.media_rate_fraction = None

class EditListBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘elst’
    Container:   Movie Box (‘trak’)
    Mandatory:   No
    Quantity:   Zero or one
    """

    def __init__(self):
        super(EditListBox, self).__init__()
        self.entry_count = None
        self.entries = None


    def parse(self, reader):
        super(EditListBox, self).parse(reader)

        self.entry_count = reader.read32()
        self.entries = []
        for _ in range(self.entry_count):
            elst_entry = EditListEntry()
            if self.version == 1:
                elst_entry.segment_duration = reader.read64()
                elst_entry.media_time = reader.read64()
            else:
                elst_entry.segment_duration = reader.read32()
                elst_entry.media_time = reader.read32()

            elst_entry.media_rate_integer = reader.read16()
            elst_entry.media_rate_fraction = reader.read16()

            self.entries.append(elst_entry)

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(EditListBox, self).print_box()

        for i, entry in enumerate(self.entries):
            print('entry no.{} segment_duration {} media_time {} media_rate_integer {} media_rate_fraction {}'.format(
                i, entry.segment_duration, entry.media_time, entry.media_rate_integer, entry.media_rate_fraction))
            # print('segment_duration :', entry.segment_duration)
            # print('media_time :', entry.media_time)
            # print('media_rate_integer :', entry.media_rate_integer)
            # print('media_rate_fraction :', entry.media_rate_fraction)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
