# -----------------------------------
# import
# -----------------------------------
from collections import OrderedDict

from utils.box import boxutils
from utils.box.basebox import Box, FullBox
from utils.box.colrbox import ColourInformationBox
from utils.box.hvccbox import HEVCConfigurationBox


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


# class SampleEntry(Box):
#
#     def __init__(self, f):
#         super(SampleEntry, self).__init__(f)
#         self.data_reference_index
#         self.parse(f)
#
#     def parse(self, f):
#         for _ in range(8):
#             _ = futils.read8(f, 'big')
#         self.data_reference_index  =futils.read16(f, 'big')
#
#     def print_box(self):
#         super(SampleEntry, self).print_box()
#         print("data_reference_index :",  self.data_reference_index)
#
# class VisualSampleEntry(SampleEntry):
#
#     def __init__(self, f):
#         super(VisualSampleEntry, self).__init__(f)
#
#     def parse(self, f):
#         pass
#
#     def print_box(self):
#         super(VisualSampleEntry, self).print_box()


class ItemRotation(ItemProperty):
    """
    ISO/IEC 23008-12
    Box Type: ‘irot’
    """

    def __init__(self):
        super(ItemRotation, self).__init__()
        self.angle = None

    def parse(self, reader):
        super(ItemRotation, self).parse(reader)

        tmp = reader.read8('big')
        self.angle = (tmp & 0x3)
        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(ItemRotation, self).print_box()
        print("angle :", self.angle)


class PixelInformationProperty(ItemFullProperty):
    """
    ISO/IEC 23008-12
    Box Type: ‘pixi’
    """
    def __init__(self):
        super(PixelInformationProperty, self).__init__()
        self.num_channels = None
        self.bits_per_channel = []

    def parse(self, reader):
        super(PixelInformationProperty, self).parse(reader)
        self.num_channels = reader.read8('big')
        for i in range(self.num_channels):
            self.bits_per_channel.append(reader.read8('big'))
        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(PixelInformationProperty, self).print_box()
        print("image_width :", self.num_channels)
        print("image_height :", self.bits_per_channel)

class ImageSpatialExtentsProperty(ItemFullProperty):
    """
    ISO/IEC 23008-12
    Box Type: ‘ispe’
    """

    def __init__(self):
        super(ImageSpatialExtentsProperty, self).__init__()
        self.image_width = None
        self.image_height = None

    def parse(self, reader):
        super(ImageSpatialExtentsProperty, self).parse(reader)

        self.image_width = reader.read32('big')
        self.image_height = reader.read32('big')
        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(ImageSpatialExtentsProperty, self).print_box()
        print("image_width :", self.image_width)
        print("image_height :", self.image_height)


class ItemPropertyContainerBox(Box):
    """
    ISO/IEC 23008-12
    Box Type: ‘ipco’
    """

    def __init__(self):
        super(ItemPropertyContainerBox, self).__init__()
        self.item_properties = None

    def parse(self, reader):
        super(ItemPropertyContainerBox, self).parse(reader)

        self.item_properties = []
        while not self.read_box_done(reader):
            box_size, box_type = boxutils.read_box_header(reader)

            item_property = None
            if box_type == 'irot':
                item_property = ItemRotation()
            elif box_type == 'colr':
                item_property = ColourInformationBox()
            elif box_type == 'hvcC':
                item_property = HEVCConfigurationBox()
            elif box_type == 'ispe':
                item_property = ImageSpatialExtentsProperty()
            elif box_type == 'pixi':
                item_property = PixelInformationProperty()
            else:
                reader.seek(box_size, 1)

            if item_property is not None:
                item_property.parse(reader)
                self.item_properties.append(item_property)

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(ItemPropertyContainerBox, self).print_box()
        for item_property in self.item_properties:
            item_property.print_box()

    def get_item_properties(self):
        return self.item_properties


class Association:
    def __init__(self):
        self.item_ID = None
        self.essential = []
        self.property_index = []


class ItemPropertyAssociation(FullBox):
    """
    ISO/IEC 23008-12
    Box Type: ‘ipma’
    """

    def __init__(self):
        super(ItemPropertyAssociation, self).__init__()
        self.entry_cout = None
        self.association_count = None
        # self.item_ID = None
        # self.essential = None
        # self.property_index = None
        self.association_list = []

    def parse(self, reader):
        super(ItemPropertyAssociation, self).parse(reader)

        self.entry_cout = reader.read32('big')

        self.association_list = []
        # self.item_ID = []
        # self.association_count = []
        # self.essential = [[] for _ in range(self.entry_cout)]
        # self.property_index = [[] for _ in range(self.entry_cout)]
        for i in range(self.entry_cout):
            association = Association()

            if self.version < 1:
                # self.item_ID.append(reader.read16('big'))
                association.item_ID = reader.read16('big')
            else:
                # self.item_ID.append(reader.read32('big'))
                association.item_ID = reader.read32('big')

            association_count = reader.read8('big')
            for _ in range(association_count):
                if self.flags & 1:
                    tmp = reader.read16('big')
                    # self.essential[i].append((tmp & 0x8000) >> 15)
                    # self.property_index[i].append(tmp & 0x7fff)
                    association.essential.append((tmp & 0x8000) >> 15)
                    association.property_index.append(tmp & 0x7fff)
                else:
                    tmp = reader.read8('big')
                    # self.essential[i].append((tmp & 0x80) >> 7)
                    # self.property_index[i].append(tmp & 0x7f)
                    association.essential.append((tmp & 0x80) >> 7)
                    association.property_index.append(tmp & 0x7f)
            self.association_list.append(association)
        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def get_item_property_association(self):
        return self.association_list

    def print_box(self):
        super(ItemPropertyAssociation, self).print_box()
        print("entry_cout :", self.entry_cout)
        print("association_count :", len(self.association_list))

        for association in self.association_list:
            print("item_ID        :", association.item_ID)
            print("essential      :", association.essential)
            print("property_index :", association.property_index)


class ItemPropertiesBox(Box):
    """
    ISO/IEC 23008-12
    Box Type: ‘iprp’
    Container: Meta box (‘meta’)
    Mandatory: No
    Quantity: Zero or one
    """

    def __init__(self):
        super(ItemPropertiesBox, self).__init__()
        self.property_container = None
        self.ipco = None
        self.ipma = None

    def parse(self, reader):
        super(ItemPropertiesBox, self).parse(reader)

        while not self.read_box_done(reader):
            box_size, box_type = boxutils.read_box_header(reader)

            if box_type == 'ipco':
                self.ipco = ItemPropertyContainerBox()
                self.ipco.parse(reader)
            elif box_type == 'ipma':
                self.ipma = ItemPropertyAssociation()
                self.ipma.parse(reader)
            else:
                reader.seek(box_size, 1)

        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(ItemPropertiesBox, self).print_box()
        if self.ipco is not None:
            self.ipco.print_box()
        if self.ipma is not None:
            self.ipma.print_box()


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
