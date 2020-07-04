# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box, FullBox


# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------
class ItemProperty(Box):
    """
    ISO/IEC 23008-12
    """

    def __init__(self):
        super(ItemProperty, self).__init__()
        # self.skip_to_end(f)  # TODO

    def parse(self, reader):
        super(ItemProperty, self).parse(reader)

    def print_box(self):
        super(ItemProperty, self).print_box()


class ItemFullProperty(FullBox):
    """
    ISO/IEC 23008-12
    """

    def __init__(self):
        super(ItemFullProperty, self).__init__()

    def parse(self, reader):
        super(ItemFullProperty, self).parse(reader)

    def print_box(self):
        super(ItemFullProperty, self).print_box()


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
