#!/usr/bin/env python3


"""
    A utility module for misc operations
"""

import os
import re
import shutil
import subprocess
import sys
import time

import urllib.request
import requests

def exe(command):
    command = command.strip()
    c = command.split()
    output, error = subprocess.Popen(c,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE).communicate()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    return (output, error)

def run_cvlc(stream_url):
    print("Playing using vlc command line...")
    cli = "cvlc '{}'".format(stream_url)
    os.system(cli)

def download(url, filename='test'):
    # download the song here
    print(url)
    print("... download in progress... :D ")
    try:
        urllib.request.urlretrieve(url, filename+'.mp3')
    except KeyboardInterrupt:
        print(" -_- why y no wait for completion -_-")
        return False
    print("... downloaded 100%, perhaps ... :P")
    return True

def download2(url, filename="test"):
    print(url)
    data = requests.get(url).content
    with open(filename+".mp3", "wb") as f:
        f.write(data)

def convert_to_mp3(filename):
    print("Converting to mp3...Have patience...")
    directory = os.path.dirname(filename)
    filename_base = os.path.basename(filename)
    new_file = directory + "/" + str(time.time()) + filename_base
    cli = "ffmpeg -i {0} {1}".format(filename, new_file)
    #cli = "ffmpeg -i {0} -map 0:a:0 -b:a 96k {1}".format(filename, new_file)
    output, error = exe(cli)
    shutil.move(new_file, filename)

def remove_multiple_spaces(string):
    return re.sub(r'\s+', ' ', string)

def replace_space(string, replacer):
    return re.sub(r"\s", replacer, string)

def replace_character(string, character, replacer):
    return re.sub(r"{}".format(character), replacer, string)

def main():
    pass

if __name__ == "__main__":
    main()

