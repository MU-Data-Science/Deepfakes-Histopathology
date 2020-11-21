import h5py
import numpy as np
import os
import random
import argparse
from scipy import ndimage, misc
from pathlib import Path

def store_hdf5(image_id, image_arr, image_arr_label, label_arr, label_arr_label, out_dir):
    # Defining the h5 file.
    file = h5py.File(Path(out_dir + "/") / f"{image_id}.h5", "w")

    # Create a dataset in the file
    file.create_dataset(image_arr_label, np.shape(image_arr), h5py.h5t.STD_U8BE, data=image_arr)
    file.create_dataset(label_arr_label, np.shape(label_arr), h5py.h5t.NATIVE_FLOAT, data=label_arr)
    file.close()

def get_image_arr(image_dir):
    ret_arr = []
    for file in os.listdir(image_dir):
        image = ndimage.imread(os.path.join(image_dir, file), mode="RGB")
        image_resized = misc.imresize(image, (224, 224))
        ret_arr.append(np.asarray(image_resized))

    return ret_arr

def get_label_arr(size):
    ret_arr = []

    for i in range(0, size):
        ret_arr.append([random.uniform(1, 20), random.randint(0, 1)])

    return ret_arr

if __name__ == "__main__":
    # Reading the input arguments.
    ap = argparse.ArgumentParser()
    ap.add_argument("-train", "--train", required=True, help="Path to the training dataset.")
    ap.add_argument("-test", "--test", required=True, help="Path to testing dataset.")
    ap.add_argument("-out", "--out", required=True, help="Path to output directory.")
    args = vars(ap.parse_args())

    train_input_dir = str(args["train"])
    test_input_dir = str(args["test"])
    out_dir = str(args["out"])

    # Creating the training h5.
    train_image_arr = get_image_arr(train_input_dir)
    train_label_arr = get_label_arr(len(train_image_arr))
    store_hdf5("hdf5_vgh_nki_he_train", train_image_arr, "train_img", train_label_arr, "train_labels", out_dir)

    # Creating the testing h5.
    test_image_arr = get_image_arr(test_input_dir)
    test_label_arr = get_label_arr(len(test_image_arr))
    store_hdf5("hdf5_vgh_nki_he_test", test_image_arr, "test_img", test_label_arr, "test_labels", out_dir)
