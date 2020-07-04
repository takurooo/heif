# -----------------------------------
# import
# -----------------------------------
import os
import argparse
from utils.heif.heifreader import HeifReader, ItemType
from utils.com.listutils import list_from_dir

# -----------------------------------
# define
# -----------------------------------
CUR_PATH = os.path.join(os.path.dirname(__file__))


# -----------------------------------
# function
# -----------------------------------
def get_args():
    parser = argparse.ArgumentParser(description="Demux HEIF file.")
    parser.add_argument("path", type=str, help="path2your_file or dir", default=None)
    return parser.parse_args()


def demux(img_path):
    heif_reader = HeifReader(img_path)
    item_id_list = heif_reader.get_item_id_list()

    basename, _ = os.path.splitext(img_path)

    for i, item_id in enumerate(item_id_list):
        item_type = heif_reader.get_item_type(item_id)
        if item_type == ItemType.GRID:
            continue

        ext = '.bin'
        if item_type == ItemType.XMP:
            ext = '.xml'

        out_path = '{}_item_{}_{}{}'.format(basename, str(item_id), item_type, ext)
        with open(out_path, 'wb') as wf:
            item = heif_reader.read_item(item_id)
            wf.write(item)

            print()
            print("item_ID     : {}".format(item_id))
            print("item_type   : {}".format(item_type))
            print("save :", out_path)

    return


# -----------------------------------
# main
# -----------------------------------
def main(args):
    in_path = args.path

    file_paths = []
    if os.path.isfile(in_path):
        file_paths = [in_path]
    elif os.path.isdir(in_path):
        # フォルダが指定された場合はフォルダ内のfileを全て変換対象とする.
        file_paths = list_from_dir(in_path)

    for img_path in file_paths:
        demux(img_path)

    # print("Press any key...", end='')
    # input()


if __name__ == '__main__':
    main(get_args())
