# -----------------------------------
# import
# -----------------------------------
import struct

# -----------------------------------
# define
# -----------------------------------
BIG_LITTLE = {'little':'<', 'big':'>'}


# -----------------------------------
# function
# -----------------------------------


class BinaryFileWriter:

    def __init__(self, file_path):
        self.file_path = file_path
        self.f = open(file_path, 'wb')
        self.byteorder = 'big'

    def set_byteorder(self, byteorder):
        self.byteorder = byteorder

    def close(self):
        if self.f:
            self.f.close()

    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

    def write8(self, v, encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            self.f.write(struct.pack(BIG_LITTLE[self.byteorder] + 'B', v))

    def write16(self, v, encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            self.f.write(struct.pack(BIG_LITTLE[self.byteorder] + 'H', v))

    def write24(self, v, encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            b = []
            if self.byteorder == 'big':
                c = (v >> 16) & 0xff
                self.write8(c)
                c = (v >> 8) & 0xff
                self.write8(c)
                c = (v >> 0) & 0xff
                self.write8(c)
            else:
                c = (v >> 0) & 0xff
                self.write8(c)
                c = (v >> 8) & 0xff
                self.write8(c)
                c = (v >> 16) & 0xff
                self.write8(c)

    def write32(self, v, encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            self.f.write(struct.pack(BIG_LITTLE[self.byteorder] + 'L', v))

    def write64(self, v, encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            self.f.write(struct.pack(BIG_LITTLE[self.byteorder] + 'Q', v))

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
