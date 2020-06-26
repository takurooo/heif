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


class HandlerReferenceBox(FullBox):
    """
    ISO/IEC 14496-12
    Box Type: ‘hdlr’
    Container: Media Box (‘mdia’) or Meta Box (‘meta’)
    Mandatory: Yes
    Quantity: Exactly one
    """

    def __init__(self):
        super(HandlerReferenceBox, self).__init__()
        self.pre_defined = None
        self.handler_type = None
        self.name = None

    def parse(self, reader):
        super(HandlerReferenceBox, self).parse(reader)

        self.pre_defined = reader.read32()
        self.handler_type = reader.read32(decode=True)
        for _ in range(3):
            _ = reader.read32()  # reserved

        self.name = None
        if not self.read_box_done(reader):
            self.name = reader.read_null_terminated()
            pass

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(HandlerReferenceBox, self).print_box()
        print("pre_defined  :", self.pre_defined)
        print("handler_type :", self.handler_type)
        print("name         :", self.name)

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass