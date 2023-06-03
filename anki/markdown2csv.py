import os
import argparse
import sys
import json
import csv
import tqdm
import glob
import copy
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import re
import pdb

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("i", help="input dir with md files")
    parser.add_argument("-o", help="out csv")
    args = parser.parse_args()
    if args.o is None:
        fullpath = os.path.abspath(os.path.realpath(args.i))
        input_dir_name = os.path.basename(fullpath)
        args.o = f'{input_dir_name}anki-notes.csv'
        print(f'export to csv: {args.o}')
    return args

def is_title(line):
    line = line.strip('\r\n ')
    if line.startswith('#'):
        return True
    return False

def convert(inpath):
    result = []
    with open(inpath, 'r') as fin:
        qapair = ['[Blank]', '[Blank]']
        for line in fin:
            line = line.strip('\r\n ')
            if is_title(line):
                if qapair[0] != '[Blank]':
                    result.append(copy.deepcopy(qapair))
                qapair[0] = line
                qapair[1] = ''
            else:
                qapair[1] += line + '\n'

        if qapair[0] != '[Blank]':
            result.append(copy.deepcopy(qapair))
        
    return result
            
def main():
    args = parse_args()
    print(os.path.basename(args.i))
    files = glob.glob(args.i + '/*.md')
    all_notes = []
    for p in tqdm.tqdm(files):
        res = convert(p)
        all_notes.extend(res)

    with open(args.o, 'w') as fout:
        wt = csv.writer(fout)
        wt.writerows(all_notes)
        
    print('done.')

if __name__ == '__main__':
    main()