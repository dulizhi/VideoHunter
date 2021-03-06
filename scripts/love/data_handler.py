# coding=utf-8
from PIL import Image
import numpy as np
import utils
import cv2
import os


def get_data(data_dir, name2index, file_num=None, im_width=128, im_height=128):
    utils.check_file(data_dir)
    depth = len(name2index)
    a = 0
    images, labels = [], []
    for subdir in os.listdir(data_dir):
        subdir_path = os.path.join(data_dir, subdir)
        role_type = name2index[subdir]
        for file in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, file)
            images.append(file_path)
            labels.append(role_type)

    package = np.vstack([images, labels]).transpose()
    np.random.shuffle(package)

    xs, ys = [], []
    for i, (x, y) in enumerate(package):
        if file_num is not None and i >= file_num:
            break
        im = Image.open(x).resize((im_width, im_height))
        im = np.array(im) / 255.
        xs.append(im)
        ys.append([(1 if j == int(y) else 0) for j in range(depth)])

    xs = np.array(xs)
    ys = np.array(ys)
    return xs, ys


PATH_ROLES = 'roles'

if __name__ == '__main__':
    names, index2name, name2index = utils.parse_name()
    print(names, index2name)

    x_data, y_data = get_data(PATH_ROLES, name2index, file_num=1000)
    print(len(x_data))
