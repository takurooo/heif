# -----------------------------------
# import
# -----------------------------------

# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------

# -----------------------------------
# class
# -----------------------------------


class Box:
    """
    ISO/IEC 14496-12
    """

    def __init__(self):
        self.start_pos = None
        self.size = None
        self.type = None
        self.largesize = None
        self.usertype = None

    # def write_box_header(self, writer):
    #     self.start_pos = writer.tell()
    #
    #     writer.write32(self.size)
    #     writer.write32(self.type, encode=True)
    #
    #     if self.size == 1:
    #         assert 0, 'not support'
    #         # writer.write64(self.largesize)
    #
    #     if self.type == 'uuid':
    #         assert 0, 'not support'
    #         # for usertype in self.usertype:
    #         #     writer.write8(usertype)
    #
    # def set_box_size(self, size):
    #     self.size = size
    #
    # def set_box_type(self, type):
    #     self.type = type

    def parse(self, reader):
        self.start_pos = reader.tell()
        # size is an integer that specifies the number of bytes in this box,
        # including all its fields and contained boxes;
        # if size is 1 then the actual size is in the field large size;
        # if size is 0, then this box is the last one in the file,
        # and its contents extend to the end of the file (normally only used for a Media Data Box)
        self.size = reader.read32('big')
        # type identifies the box type;
        # standard boxes use a compact type, which is normally four printable characters,
        # to permit ease of identification, and is shown so in the boxes below.
        # User extensions use an extended type; in this case, the type field is set to ‘uuid’.
        self.type = reader.read32('big', decode=True)

        if self.size == 1:
            self.largesize = reader.read64('big')
        elif self.size == 0:
            # box extends to end of file
            pass
        if self.type == 'uuid':
            self.usertype = [reader.read8('big') for _ in range(16)]

    def print_box(self):
        print('--------------------------')
        print('boxtype   :', self.type)
        print('boxsize   :', hex(self.size))
        print('largesize :', self.largesize)
        print('usertype  :', self.usertype)
        print('--------------------------')

    def get_box_size(self):
        if self.size == 1:
            return self.largesize
        else:
            return self.size

    def get_box_type(self):
        return self.type

    def get_box_start_pos(self):
        return self.start_pos

    def read_box_done(self, reader):
        read_size = reader.tell() - self.get_box_start_pos()
        if self.get_box_size() <= read_size:
            return True
        else:
            return False

    def to_box_end(self, reader):
        reader.seek(self.get_box_start_pos()+self.get_box_size())


class FullBox(Box):
    def __init__(self):
        super(FullBox, self).__init__()
        self.is_fullbox = True
        self.version = None
        self.flags = None

    # def write_full_box_header(self, writer):
    #     self.write_box_header(writer)
    #     writer.write8(self.version)
    #     writer.write24(self.flags)

    def parse(self, reader):
        super(FullBox, self).parse(reader)
        # v_flags = bitstream.read32('big')
        # self.version = (v_flags & 0xff000000) >> 24
        # self.flags = (v_flags & 0x00ffffff)
        self.version = reader.readbits(8)
        self.flags = reader.readbits(24)


    def print_box(self):
        super(FullBox, self).print_box()
        print('version :', self.version)
        print('flags   :', self.flags)


# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass