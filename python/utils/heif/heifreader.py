# -----------------------------------
# import
# -----------------------------------
from utils.file.binaryfilereader import BinaryFileReader
from utils.box.ftypebox import FileTypeBox
from utils.box.metabox import MetaBox
from utils.box.mdatbox import MediaDataBox
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


class ITEM_TYPE:
    HVC1 = 'hvc1'
    GRID = 'grid'
    EXIF = 'Exif'
    XMP = 'mime'


class HeifReader:

    def __init__(self, img_path):
        self.img_path = img_path

        self.ftyp = None
        self.meta = None
        self.mdat = None
        self.item_properties = {}

        self.reader = BinaryFileReader(img_path)
        self._read_boxes(self.reader)
        self._associate_item_property()
        self.reader.seek(0)

    def _associate_item_property(self):
        ipma = self.meta.iprp.ipma
        ipco = self.meta.iprp.ipco

        prop_list = ipco.get_item_properties()
        for association in ipma.get_item_property_association():
            self.item_properties[association.item_ID] = []
            for prop_idx in association.property_index:
                prop = prop_list[prop_idx-1]
                self.item_properties[association.item_ID].append(prop)

    def _read_boxes(self, reader):
        reader.seek(0)

        while reader.num_bytes_left():
            box_size, box_type = boxutils.read_box_header(reader)
            # print(box_type)

            if box_type == 'ftyp':
                self.ftyp = FileTypeBox()
                self.ftyp.parse(reader)
            elif box_type == 'meta':
                self.meta = MetaBox()
                self.meta.parse(reader)
            elif box_type == 'mdat':
                self.mdat = MediaDataBox()
                self.mdat.parse(reader)
            else:
                reader.seek(box_size, 1)

    def __del__(self):
        self.reader.close()

    def print_boxes(self):
        if self.ftyp is not None:
            self.ftyp.print_box()
        if self.meta is not None:
            self.meta.print_box()

    # def get_boxtype_list(self):
    #     return self.boxtype_list

    # def get_box(self, boxtype):
    #     return self.box_reader.get_box(boxtype)

    def get_primary_item_id(self):
        return self.meta.pitm.get_primary_item_id()

    def get_item_properties(self, item_ID):
        return self.item_properties[item_ID]

    def get_item_type(self, item_ID):
        return self.meta.iinf.get_item_type(item_ID)

    def get_item_id_list(self):
        return self.meta.iinf.get_item_id_list()

    def get_item_offset_size(self, item_ID):
        iloc = self.meta.iloc
        assert iloc is not None, 'iloc not found.'
        assert iloc.has_item_id_entry(item_ID), 'invali item id {}'.format(item_ID)

        item_loc = iloc.get_item_loc(item_ID)

        construction_method = item_loc.get_construction_method()
        base_offset = item_loc.get_base_offset()
        item_loc_ext_list = item_loc.get_extent_list()

        # TODO idat_offset と item_offset は未対応
        assert construction_method == item_loc.CONSTRUCTION_METHOD_FILE_OFFSET, 'constructionmethod not filetop {}.'.format(
            construction_method)

        item_offset_list = []
        item_size_list = []
        for item_loc_ext in item_loc_ext_list:
            item_offset = base_offset + item_loc_ext.get_extent_offset()
            item_size = item_loc_ext.get_extent_length()

            item_offset_list.append(item_offset)
            item_size_list.append(item_size)

        return item_offset_list, item_size_list

    def read_item(self, item_ID):
        item_offset_list, item_size_list = self.get_item_offset_size(item_ID)

        item_data = b''
        for item_offset, item_size in zip(item_offset_list, item_size_list):
            self.reader.seek(item_offset)
            item_data += self.reader.read_raw(item_size)

        return item_data


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
