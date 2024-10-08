from basicsr.utils.create_lmdb import create_lmdb_for_gopro

def main():
    opt = {}

    opt['save_folder'] = './datasets/Sim/train/blur_crops'
    opt['save_folder'] = './datasets/Sim/train/sharp_crops'
    opt['crop_size'] = 512


    create_lmdb_for_gopro()

if __name__ == '__main__':
    main()