# -----------------------------------
# import
# -----------------------------------
import os
from collections import OrderedDict
from utils.file.binaryfilereader import BinaryFileReader

from utils.box.basebox import Box
from utils.box.ftypebox import FileTypeBox
from utils.box.metabox import MetaBox
from utils.box.hdlrbox import HandlerReferenceBox
from utils.box.ilocbox import ItemLocationBox
from utils.box.iinfbox import ItemInformationBox
from utils.box.pitmbox import PrimaryItemBox
from utils.box.mdatbox import MediaDataBox
from utils.box.iprpbox import ItemPropertiesBox
from utils.box.irefbox import ItemReferenceBox

# -----------------------------------
# define
# -----------------------------------
BOX_HEADER_SIZE = 8


# -----------------------------------
# function
# -----------------------------------


# -----------------------------------
# class
# -----------------------------------
class BoxInfoDeployer:
    """
    BoxInfoDeployer for HEIF
    """

    def __init__(self):
        self._boxinfo = {
            'ftyp':{'child':False, 'fullbox':False, 'class':FileTypeBox},
            'meta':{'child':True, 'fullbox':True, 'class':MetaBox},
            'hdlr':{'child':False, 'fullbox':True, 'class':HandlerReferenceBox},
            'iloc':{'child':False, 'fullbox':True, 'class':ItemLocationBox},
            'iinf':{'child':False, 'fullbox':True, 'class':ItemInformationBox},
            'pitm':{'child':False, 'fullbox':True, 'class':PrimaryItemBox},
            'iprp':{'child':False, 'fullbox':False, 'class':ItemPropertiesBox},
            'iref':{'child':False, 'fullbox':True, 'class':ItemReferenceBox},
            'mdat':{'child':False, 'fullbox':False, 'class':MediaDataBox},
        }

    def has_child(self, boxtype):
        target_box_info = self._boxinfo.get(boxtype, None)
        if target_box_info is not None:
            return target_box_info['child']
        else:
            return False

    def is_fullbox(self, boxtype):
        target_box_info = self._boxinfo.get(boxtype, None)
        if target_box_info is not None:
            return target_box_info['fullbox']
        else:
            return False

    def get_box_class(self, boxtype):
        target_box_info = self._boxinfo.get(boxtype, None)
        if target_box_info is not None:
            return target_box_info.get('class', None)
        else:
            return None


class BoxReader:
    """
    Box reader
    """

    def __init__(self, path):
        self.file_size = os.path.getsize(path)
        self.reader = BinaryFileReader(path)
        self.box_pos = OrderedDict()
        self.boxinfo_deployer = BoxInfoDeployer()

    def __del__(self):
        pass

    def read_boxes(self):
        self.reader.seek(0)

        total_file_size = self.file_size
        while 0 < total_file_size:
            boxsize = self._read_box(self.reader)
            total_file_size -= boxsize

        return tuple(self.box_pos.keys())

    def _read_box(self, reader):
        box = Box()
        box.parse(reader)
        self.box_pos[box.type] = {'size':box.get_box_size(), 'fp':box.get_box_start_pos()}
        data_size = box.size - BOX_HEADER_SIZE

        if self._has_child(box.type):

            children_size = data_size
            if self._is_fullbox(box.type):
                # FullBox: unsigned int(8) version; bit(24) flags;
                fullbox_info_size = 4
                reader.seek(fullbox_info_size, 1)  # f.seek(offset, whence)
                children_size -= fullbox_info_size

            while 0 < children_size:
                child_size = self._read_box(reader)
                children_size -= child_size

        else:
            reader.seek(data_size, 1)

        return box.size

    def _has_child(self, boxtype):
        return self.boxinfo_deployer.has_child(boxtype)

    def _is_fullbox(self, boxtype):
        return self.boxinfo_deployer.is_fullbox(boxtype)

    def _get_box_class(self, boxtype):
        return self.boxinfo_deployer.get_box_class(boxtype)

    def get_box(self, boxtype):
        target_box_pos = self.box_pos.get(boxtype, None)

        if target_box_pos is None:
            return None

        target_box = self._get_box_class(boxtype)
        if target_box is not None:
            self.reader.seek(target_box_pos['fp'])
            try:
                box = target_box()
                box.parse(self.reader)
            except:
                import traceback
                traceback.print_exc()
                assert 0, ""
            return box
        else:
            return None


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
