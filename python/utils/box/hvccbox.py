# -----------------------------------
# import
# -----------------------------------
from utils.box.basebox import Box


# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------

class HEVCDecoderConfigurationRecord:
    """
    ISO/IEC 14496-15
    """

    def __init__(self, reader):
        self.configurationVersion = None
        self.genera_profile_space = None
        self.general_tier_flag = None
        self.general_profile_idc = None
        self.general_profile_compatibility_flags = None
        self.general_constraint_indicator_flags = None
        self.general_level_idc = None
        self.min_spatial_segmentation_idc = None
        self.parallelismType = None
        self.chroma_format_idc = None
        self.bit_depth_luma_minus8 = None
        self.bit_depth_chroma_minus8 = None
        self.avgFrameRate = None
        self.constantFrameRate = None
        self.numTemporalLayers = None
        self.temporalIdNested = None
        self.lengthSizeMinus = None
        self.numOfArrays = None
        self.nalUnits = None
        self.array_completeness = None
        self.NAL_unit_type = None
        self.numNalus = None
        self.nalUnitLength = None
        self.parse(reader)

    def parse(self, reader):
        self.configurationVersion = reader.read8('big')
        tmp = reader.read8('big')
        self.genera_profile_space = (tmp & 0xc0) >> 6
        self.general_tier_flag = (tmp & 0x20) >> 5
        self.general_profile_idc = tmp & 0x1f
        self.general_profile_compatibility_flags = reader.read32('big')
        self.general_constraint_indicator_flags = (reader.read8('big') << 40) \
                                                  | (reader.read8('big') << 32) \
                                                  | (reader.read8('big') << 24) \
                                                  | (reader.read8('big') << 16) \
                                                  | (reader.read8('big') << 8) \
                                                  | (reader.read8('big') << 0)
        self.general_level_idc = reader.read8('big')

        self.min_spatial_segmentation_idc = reader.read16('big') & 0x0fff
        self.parallelismType = reader.read8('big') & 0b00000011
        self.chroma_format_idc = reader.read8('big') & 0b00000011
        self.bit_depth_luma_minus8 = reader.read8('big') & 0b00000111
        self.bit_depth_chroma_minus8 = reader.read8('big') & 0b00000111
        self.avgFrameRate = reader.read16('big')

        tmp = reader.read8('big')
        self.constantFrameRate = (tmp & 0b11000000) >> 6
        self.numTemporalLayers = (tmp & 0b00111000) >> 3
        self.temporalIdNested = (tmp & 0b00000100) >> 2
        self.lengthSizeMinus = tmp & 0b00000011
        self.numOfArrays = reader.read8('big')

        self.nalUnits = []
        for j in range(self.numOfArrays):
            tmp = reader.read8('big')
            self.array_completeness = (tmp & 0b10000000) >> 7
            self.NAL_unit_type = tmp & 0b00111111
            self.numNalus = reader.read16('big')

            nalUnit = []
            for i in range(self.numNalus):
                self.nalUnitLength = reader.read16('big')
                for _ in range(self.nalUnitLength):
                    nalUnit.append(reader.read8('big'))
                self.nalUnits.append(nalUnit)


class HEVCConfigurationBox(Box):
    """
    ISO/IEC 14496-15
    for hvcC
    """

    def __init__(self):
        super(HEVCConfigurationBox, self).__init__()
        self.HEVCConfig = None

    def parse(self, reader):
        super(HEVCConfigurationBox, self).parse(reader)

        self.HEVCConfig = HEVCDecoderConfigurationRecord(reader)
        assert self.read_box_done(reader), '{} num bytes left not 0.'.format(self.type)

    def print_box(self):
        super(HEVCConfigurationBox, self).print_box()
        print('configurationVersion : ', self.HEVCConfig.configurationVersion)
        print('genera_profile_space : ', self.HEVCConfig.genera_profile_space)
        print('general_tier_flag : ', self.HEVCConfig.general_tier_flag)
        print('general_profile_idc : ', self.HEVCConfig.general_profile_idc)
        print('general_profile_compatibility_flags : 0x{:X}'.format(
            self.HEVCConfig.general_profile_compatibility_flags))
        print('general_constraint_indicator_flags : 0x{:X}'.format(self.HEVCConfig.general_constraint_indicator_flags))
        print('general_level_idc : ', self.HEVCConfig.general_level_idc)
        print('min_spatial_segmentation_idc : ', self.HEVCConfig.min_spatial_segmentation_idc)
        print('parallelismType : ', self.HEVCConfig.parallelismType)
        print('chroma_format_idc : ', self.HEVCConfig.chroma_format_idc)
        print('bit_depth_luma_minus8 : ', self.HEVCConfig.bit_depth_luma_minus8)
        print('bit_depth_chroma_minus8 : ', self.HEVCConfig.bit_depth_chroma_minus8)
        print('avgFrameRate : ', self.HEVCConfig.avgFrameRate)
        print('constantFrameRate : ', self.HEVCConfig.constantFrameRate)
        print('numTemporalLayers : ', self.HEVCConfig.numTemporalLayers)
        print('temporalIdNested : ', self.HEVCConfig.temporalIdNested)
        print('lengthSizeMinus : ', self.HEVCConfig.lengthSizeMinus)
        print('numOfArrays : ', self.HEVCConfig.numOfArrays)
        print('nalUnits : ', self.HEVCConfig.nalUnits)
        print('array_completeness : ', self.HEVCConfig.array_completeness)
        print('NAL_unit_type : ', self.HEVCConfig.NAL_unit_type)
        print('numNalus : ', self.HEVCConfig.numNalus)
        print('nalUnitLength : ', self.HEVCConfig.nalUnitLength)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
