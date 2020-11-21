import argparse
import os
from shutil import copyfile, rmtree

def split(input_dir):
    # Obtaining the training and test set sizes.
    total_size = len(os.listdir(input_dir))
    train_size = round(.8 * total_size)

    # Deleting and re-creating train/test directories.
    if os.path.exists(input_dir + "-train"):
        rmtree(input_dir + "-train")
    if os.path.exists(input_dir + "-test"):
        rmtree(input_dir + "-test")
    os.makedirs(input_dir + "-train")
    os.makedirs(input_dir + "-test")

    # Copying the file from the source to train/test directories.
    for index, file in enumerate(os.listdir(input_dir)):
        if index < train_size:
            copyfile(input_dir + "/" + file, input_dir + "-train/" + file)
        else:
            copyfile(input_dir + "/" + file, input_dir + "-test/" + file)

if __name__ == "__main__":
    # Reading the input arguments.
    ap = argparse.ArgumentParser()
    ap.add_argument("-data", "--data", required=True, help="Path to the dataset directory.")
    args = vars(ap.parse_args())

    split(str(args["data"]))