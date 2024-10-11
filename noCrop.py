# import sys, os
# sys.path.append(os.path.abspath(r'F:\project\NAFNet'))

from basicsr.utils.create_lmdb import create_lmdb_for_gopro, create_lmdb_for_val

def main():
    opt = {}
    opt['compression_level'] = 3

    opt['save_folder'] = './datasets/Sim/train/blur_crops'
    opt['save_folder'] = './datasets/Sim/train/sharp_crops'
    opt['crop_size'] = 512


    create_lmdb_for_gopro()
    create_lmdb_for_val()

if __name__ == '__main__':
    main()