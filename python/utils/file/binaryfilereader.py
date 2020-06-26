# -----------------------------------
# import
# -----------------------------------
import os
import struct

# -----------------------------------
# define
# -----------------------------------
BIG_LITTLE = {'little':'<', 'big':'>'}


# -----------------------------------
# function
# -----------------------------------


class BinaryFileReader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.f = open(file_path, 'rb')
        self.file_size = os.path.getsize(file_path)

        self.start_fp = self.f.tell()

        self.num_bits_left = 0
        self.bit_buffer = 0

    def close(self):
        if self.f:
            self.f.close()

    def num_bytes_left(self):
        return self.file_size - (self.f.tell() - self.start_fp)

    def seek_to_end(self):
        self.seek(self.file_size)

    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()

    def read_raw(self, size):
        return self.f.read(size)

    def read8(self, byteorder='big', signed=False, decode=False):
        if decode:
            return self.f.read(1).decode()
        else:
            if signed:
                format_char = 'b'
            else:
                format_char = 'B'
            return struct.unpack(BIG_LITTLE[byteorder] + format_char, self.f.read(1))[0]

    def read16(self, byteorder='big', signed=False, decode=False):
        if decode:
            return self.f.read(2).decode()
        else:
            if signed:
                format_char = 'h'
            else:
                format_char = 'H'
            return struct.unpack(BIG_LITTLE[byteorder] + format_char, self.f.read(2))[0]

    def read24(self, byteorder='big', signed=False, decode=False):
        filler = 0
        filler = filler.to_bytes(1, byteorder='big', signed=True)
        a = self.f.read(1)
        b = self.f.read(1)
        c = self.f.read(1)
        if byteorder == 'big':
            bin24 = a + b + c
        elif byteorder == 'little':
            bin24 = c + b + a
        else:
            raise ValueError(f'Invalid byteorder {byteorder}')

        if decode:
            return bin24.decode()
        else:
            bin32 = bin24 + filler  # to 32bit
            if signed:
                format_char = 'l'
            else:
                format_char = 'L'
            ret24 = struct.unpack(BIG_LITTLE[byteorder] + format_char, bin32)[0] >> 8
            return ret24


    def read32(self, byteorder='big', signed=False, decode=False):
        if decode:
            return self.f.read(4).decode()
        else:
            if signed:
                format_char = 'l'
            else:
                format_char = 'L'
            return struct.unpack(BIG_LITTLE[byteorder] + format_char, self.f.read(4))[0]

    def read64(self, byteorder='big', signed=False, decode=False):
        if decode:
            return self.f.read(8).decode()
        else:
            if signed:
                format_char = 'q'
            else:
                format_char = 'Q'
            return struct.unpack(BIG_LITTLE[byteorder] + format_char, self.f.read(8))[0]

    def readn(self, size_bits, byteorder='big', signed=False, decode=False):

        if size_bits == 0:
            return 0

        if size_bits == 64:
            data = self.read64(byteorder, signed, decode)
        elif size_bits == 32:
            data = self.read32(byteorder, signed, decode)
        elif size_bits == 24:
            data = self.read24(byteorder, signed, decode)
        elif size_bits == 16:
            data = self.read16(byteorder, signed, decode)
        elif size_bits == 8:
            data = self.read8(byteorder, signed, decode)
        else:
            raise ValueError()

        return data

    def is_byte_aligned(self):
        return self.num_bits_left == 0

    def readbits(self, len):
        # big endian only

        if len == 0:
            return 0

        if len > 8:
            return_bits = self.read8() << (len - 8)
            return_bits |= self.readbits(len - 8)
            return return_bits

        if self.num_bits_left >= len:
            return_bits = self.bit_buffer >> (8 - len)
            self.bit_buffer = (self.bit_buffer << len) & 0xFF
            self.num_bits_left -= len

        else:
            read_bits = self.read8()
            self.bit_buffer = (self.bit_buffer << self.num_bits_left) | read_bits
            self.num_bits_left += 8
            return_bits = self.bit_buffer >> (self.num_bits_left - len)
            self.bit_buffer = ((self.bit_buffer << (8 - (self.num_bits_left - len))) & 0xFF)
            self.num_bits_left -= len

        return return_bits

    def read_null_terminated(self):
        null = b'\x00'
        s = ''
        while True:
            c = self.read8('big', decode=True)
            s += c
            if c.encode() == null:
                break
        return s

    def write8(self, v, order='big', encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            self.f.write(struct.pack(BIG_LITTLE[order] + 'B', v))

    def write16(self, v, order='big', encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            self.f.write(struct.pack(BIG_LITTLE[order] + 'H', v))

    def write24(self, v, order='big', encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            b = []
            if order == 'big':
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

    def write32(self, v, order='big', encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            self.f.write(struct.pack(BIG_LITTLE[order] + 'L', v))

    def write64(self, v, order='big', encode=False):
        if encode:
            self.f.write(v.encode('utf-8'))
        else:
            self.f.write(struct.pack(BIG_LITTLE[order] + 'Q', v))

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
