import os, sys


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, default="/mnt/sdb/SIGNATE_DATA/liver-disease-detection/")
parser.add_argument("--input", type=str, default="./input/")
parser.add_argument("--output", type=str, default="./output/")

args, unknown = parser.parse_known_args()


# debug --
if __name__ == "__main__":
    print(args)

    print("====")
    print(unknown)