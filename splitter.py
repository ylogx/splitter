#!/usr/bin/env python3
import os
import sys

def init_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory:', directory)
        os.makedirs(directory)

def get_output_directory(file):
    extension = file.split('.')[-1]
    output_dir = None
    if (extension in ['jpg', 'jpeg', 'png', 'tiff', 'bmp']):
        output_dir = 'images'
    elif (extension == ['c', 'cpp', 'java', 'jar', 'py', 'sh']):
        output_dir = 'code'
    elif (extension in ['mp4', 'mkv', 'avi', 'flv', '3gp', 'mov']):
        output_dir = 'videos'
    return output_dir

def make_the_move(output_dir, filename):
    init_dir(output_dir)
    src = filename
    dest = os.path.join(output_dir, filename)
    os.rename(src, dest)
    print('Moved', src, 'to', dest)

def splitter(in1, in2):
    for (dirpath, dirnames, filenames) in os.walk(in1):
        if (dirpath == './images'
                or dirpath == './videos'
                or dirpath == './code'):
            print('Skipping ', dirpath)
            continue
        print(dirpath, dirnames, filenames)
        print('Working in', dirpath, ':\n',
                '  There are', len(filenames), 'files &',
                len(dirnames), 'directories in it')
        for file in filenames:
            filename = os.path.join(dirpath, file)
            output_dir = get_output_directory(file)
            if output_dir:
                print('Operating on', filename)
                make_the_move(output_dir, filename)
            else:
                print('Can\'t figure out type for', filename)

def main():
    argc = len(sys.argv)
    print('Argument len: ', argc)
    if argc < 2:
        print('Error: No arguments!')
        return
    in1 = sys.argv[1]
    if argc == 3:
        in2 = sys.argv[2]
    else:
        in2 = None
    splitter(in1, in2)

if __name__ == '__main__':
    main()
