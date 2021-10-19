#!/usr/bin/env python3

# Module Docstring


__author__ = "Andrew Freeman (andrewfreeman234@gmail.com)"
__version__ = "0.1.0"
__license__ = "MIT"

import ffmpeg
import glob
import os
from logzero import logger
import argparse


def sum_of_two_numbers(x, y):
    return x + y - y + y

# Main Body

# Plan:
# 1. Get all webms in a folder
# 2. For each webm, check if it has sound
# 3. If it does not have sound, move it to a new folder (webm_without_sound)
# 4. If it has sound, move it to a new folder (webm_with_sound)


def main(args):
    print("hello world")
    folder_to_check = os.getcwd()

    webms = get_webms_in_folder(args.path)
    current = 0
    while current < len(webms):
        current_has_sound = does_webm_have_sound(webms[current])
        current += 1


def get_files_in_folder(path):
    logger.info("globbing " + str(path))
    files = glob.glob(path)
    logger.info(files)
    return files


def get_webms_in_folder(path):
    files_path = os.path.join(path, "*.webm")
    logger.info("globbing " + str(files_path))
    files = glob.glob(files_path)
    logger.info(files)
    return files


# Returns boolean
def does_webm_have_sound(webm_path):
    has_audio = ffmpeg.probe(webm_path, select_streams='a');
    if has_audio['streams']:
        logger.info(webm_path + " has audio")
        return True
    else:
        logger.info(webm_path + " has no audio")
        return False




def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("path", help="Required positional argument", type=dir_path)

    # # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    # parser.add_argument(
    #     "-v",
    #     "--verbose",
    #     action="count",
    #     default=0,
    #     help="Verbosity (-v, -vv, etc)")

    args = parser.parse_args()
    main(args)
