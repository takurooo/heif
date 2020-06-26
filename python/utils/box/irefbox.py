# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box, FullBox
from utils.box import boxutils


# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------


class SingleItemTypeReferenceBox(Box):
    def __init__(self):
        super(SingleItemTypeReferenceBox, self).__init__()
        self.from_item_ID = None
        self.reference_count = None
        self.to_item_ID = None

    def parse(self, reader):
        super(SingleItemTypeReferenceBox, self).parse(reader)

        self.from_item_ID = reader.read16('big')
        self.reference_count = reader.read16('big')
        self.to_item_ID = []
        for _ in range(self.reference_count):
            self.to_item_ID.append(reader.read16('big'))

    def print_box(self):
        super(SingleItemTypeReferenceBox, self).print_box()
        print("from_item_ID :", self.from_item_ID)
        print("reference_count :", self.reference_count)
        print("to_item_ID :", self.to_item_ID)


class SingleItemTypeReferenceBoxLarge(Box):
    def __init__(self):
        super(SingleItemTypeReferenceBoxLarge, self).__init__()
        self.from_item_ID = None
        self.reference_count = None
        self.to_item_ID = None

    def parse(self, reader):
        super(SingleItemTypeReferenceBoxLarge, self).parse(reader)

        self.from_item_ID = reader.read32('big')
        self.reference_count = reader.read16('big')
        self.to_item_ID = []
        for _ in range(self.reference_count):
            self.to_item_ID.append(reader.read32('big'))

    def print_box(self):
        super(SingleItemTypeReferenceBoxLarge, self).print_box()
        print("from_item_ID :", self.from_item_ID)
        print("reference_count :", self.reference_count)
        print("to_item_ID :", self.to_item_ID)


class ItemReferenceBox(FullBox):
    """
    ISO/IEC 14496-12
    Box	Type:   ‘iref’
    Container:  Metadata	box	(‘meta’)
    Mandatory:  No
    Quantity:   Zero	or	one
    """

    def __init__(self):
        super(ItemReferenceBox, self).__init__()
        self.item_reference_list = None

    def parse(self, reader):
        super(ItemReferenceBox, self).parse(reader)

        self.item_reference_list = []
        if self.version == 0:
            item_ref_box_class = SingleItemTypeReferenceBox
        else:
            item_ref_box_class = SingleItemTypeReferenceBoxLarge

        while not self.read_box_done(reader):
            box_size, box_type = boxutils.read_box_header(reader)

            item_ref_box = item_ref_box_class()
            item_ref_box.parse(reader)
            self.item_reference_list.append(item_ref_box)

    def print_box(self):
        super(ItemReferenceBox, self).print_box()
        for item_reference in self.item_reference_list:
            item_reference.print_box()


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
