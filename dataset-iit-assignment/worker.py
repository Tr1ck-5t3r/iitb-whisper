import pandas as pd
import numpy as np
import os
import sys
import shutil


# normalise the dataset by removing unwanted spaces


def normalise_text(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print("Normalisation completed.")
    return


def add_commas_instead_of_space(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.strip().split(" ") for line in lines]
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + ",")
    print("Commas added.")
    return


# convert text and mp3.scp files to csv


def convert_text_to_csv(text_file, csv_file):
    df = pd.DataFrame(lines, columns=["utt_id", "transcript"])
    df.to_csv(csv_file, index=False)


def convert_mp3scp_to_csv(mp3scp_file, csv_file):
    with open(mp3scp_file, "r", encoding="utf-8") as f:  # Specify encoding as utf-8
        lines = f.readlines()
    lines = [line.strip().split(" ") for line in lines]
    df = pd.DataFrame(lines, columns=["utt_id", "path"])
    df.to_csv(csv_file, index=False)


def main():
    data_dir = r"E:/iitb/GV_Eval_3h/dataset/"
    text_file = os.path.join(data_dir, "text")
    mp3scp_file = os.path.join(data_dir, "mp3.scp")
    text_csv_file = os.path.join(data_dir, "text.csv")
    mp3scp_csv_file = os.path.join(data_dir, "mp3.csv")

    normalise_text(text_file)
    normalise_text(mp3scp_file)

    """ print(text_file)
    print(mp3scp_file)
    print(text_csv_file)
    print(mp3scp_csv_file)

    convert_text_to_csv(text_file, text_csv_file)

    convert_mp3scp_to_csv(mp3scp_file, mp3scp_csv_file) """

    print("Conversion completed.")


if __name__ == "__main__":
    data_dir = r"E:/iitb/GV_Eval_3h/dataset/"
    text_file = os.path.join(data_dir, "text")
    mp3scp_file = os.path.join(data_dir, "mp3.scp")
    text_csv_file = os.path.join(data_dir, "text.csv")
    mp3scp_csv_file = os.path.join(data_dir, "mp3.csv")

    convert_text_to_csv(text_file, text_csv_file)

    convert_mp3scp_to_csv(mp3scp_file, mp3scp_csv_file)
