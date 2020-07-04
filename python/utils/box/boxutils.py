# -----------------------------------
# import
# -----------------------------------


# -----------------------------------
# define
# -----------------------------------

# -----------------------------------
# function
# -----------------------------------
def read_box_header(reader):
    box_size = reader.read32()
    box_type = reader.read32(decode=True)
    reader.seek(-8, 1)
    return box_size, box_type


# -----------------------------------
# class
# -----------------------------------

# -----------------------------------
# main
# -----------------------------------
if __name__ == '__main__':
    pass
