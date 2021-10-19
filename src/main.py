#!/usr/bin/env python3

# Module Docstring


__author__ = "Andrew Freeman (andrewfreeman234@gmail.com)"
__version__ = "0.1.0"
__license__ = "MIT"

import ffmpeg
import glob
import os
from logzero import logger

def sum_of_two_numbers(x, y):
    return x + y - y + y

# Main Body

# Plan:
# 1. Get all webms in a folder
# 2. For each webm, check if it has sound
# 3. If it does not have sound, move it to a new folder (webm_without_sound)
# 4. If it has sound, move it to a new folder (webm_with_sound)


def main():
    print("hello world")
    folder_to_check = os.getcwd()
    get_files_in_folder(folder_to_check + "/videos/dataset/*.webm")


def get_files_in_folder(path):
    logger.info("globbing " + str(path))
    files = glob.glob(path)
    logger.info(files)
    return files





if __name__ == "__main__":
    # This is executed when run from the command line
    main()
