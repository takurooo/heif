# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import FullBox
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
class ItemInfoExtension:
    def __init__(self, extension_type):
        pass


class ItemInfoEntry(FullBox):
    """
    ISO/IEC 14496-12
    Box Type: ‘infe’
    """
    def __init__(self):
        super(ItemInfoEntry, self).__init__()
        self.item_ID = None
        self.item_protection_index = None
        self.item_name = None
        self.item_type = None
        self.item_uri_type = None
        self.content_type = None
        self.content_encoding = None
        self.extension_type = None
        self.iteminfoext = None

    def parse(self, reader):
        super(ItemInfoEntry, self).parse(reader)

        if self.version == 0 or self.version == 1:
            self.item_ID = reader.read16('big')
            self.item_protection_index = reader.read16('big')
            self.item_name = reader.read_null_terminated()
            self.content_type = reader.read_null_terminated()
            if not self.read_box_done(reader):
                self.content_encoding = reader.read_null_terminated()  # optional

            if self.version == 1 and 0 < reader.num_bytes_left():
                self.extension_type = reader.read32('big')  # optional
                self.iteminfoext = ItemInfoExtension(self.extension_type)  # optional

        if self.version >= 2:
            if self.version == 2:
                self.item_ID = reader.read16('big')
            elif self.version == 3:
                self.item_ID = reader.read32('big')

            self.item_protection_index = reader.read16('big')
            self.item_type = reader.read32('big', decode=True)

            self.item_name = reader.read_null_terminated()

            if self.item_type == 'mime':
                self.content_type = reader.read_null_terminated()
                if not self.read_box_done(reader):
                    self.content_encoding = reader.read_null_terminated() # optional
            elif self.item_type == 'uri ':
                self.item_uri_type = reader.read_null_terminated()

    def print_box(self):
        super(ItemInfoEntry, self).print_box()
        print("item_ID :", self.item_ID)
        print("item_protection_index :", self.item_protection_index)
        print("item_name :", self.item_name)
        print("item_type :", self.item_type)
        print("item_uri_type :", self.item_uri_type)
        print("content_type :", self.content_type)
        print("content_encoding :", self.content_encoding)
        print("extension_type :", self.extension_type)


class ItemInformationBox(FullBox):
    """
    ISO/IEC 14496-12
    Box Type: ‘iinf’
    Container: Meta Box (‘meta’)
    Mandatory: No
    Quantity: Zero or one
    """

    def __init__(self):
        super(ItemInformationBox, self).__init__()
        self.infe_list = None
        self.item_id_list = None  # 後で使う用

    def parse(self, reader):
        super(ItemInformationBox, self).parse(reader)

        if self.version == 0:
            entry_count = reader.read16('big')
        else:
            entry_count = reader.read32('big')

        self.infe_list = []
        self.item_id_list = []
        for _ in range(entry_count):
            box_size, box_type = boxutils.read_box_header(reader)
            if box_type == 'infe':
                infe = ItemInfoEntry()
                infe.parse(reader)

                self.item_id_list.append(infe.item_ID)  # 後で使う用
                self.infe_list.append(infe)

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(ItemInformationBox, self).print_box()
        print("entry_count :", len(self.infe_list))
        for infe in self.infe_list:
            infe.print_box()

    def get_item_id_list(self):
        return self.item_id_list

    def get_item_type(self, item_ID):
        assert item_ID in self.item_id_list, 'invalid item id'
        for infe in self.infe_list:
            if infe.item_ID == item_ID:
                return infe.item_type

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass