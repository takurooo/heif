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


class HintMediaHeaderBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘hmhd’
    Container:   Media Information Box (‘minf’)
    Mandatory:   Yes
    Quantity:   Exactly one specific media header shall be present
    """

    def __init__(self):
        super(HintMediaHeaderBox, self).__init__()
        self.maxPDUsize = None
        self.avgPDUsize = None
        self.maxbitrate = None
        self.avgbitrate = None

    def parse(self, reader):
        super(HintMediaHeaderBox, self).parse(reader)

        self.maxPDUsize = reader.read16()
        self.avgPDUsize = reader.read16()
        self.maxbitrate = reader.read16()
        self.avgbitrate = reader.read16()
        _ = reader.read32()  # reserved = 0

        assert self.read_complete(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(HintMediaHeaderBox, self).print_box()
        print("maxPDUsize :", self.maxPDUsize)
        print("avgPDUsize :", self.avgPDUsize)
        print("maxbitrate :", self.maxbitrate)
        print("avgbitrate :", self.avgbitrate)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
