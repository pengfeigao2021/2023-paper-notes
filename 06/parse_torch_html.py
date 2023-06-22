import os
import csv
import argparse
import glob
import tqdm
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import re
from bs4 import BeautifulSoup
import pdb

def parse_args():
    parser = argparse.ArgumentParser()
    return parser.parse_args()

def readone(path):
    content = open(path, 'r').read()
    print('len content:', len(content))
    soup = BeautifulSoup(content,"lxml")
    title = soup.find('title').text
    print(title)
    # text = '<br>\n'.join(v.find('p').text for v in soup.findAll('dd'))
    section = soup.find('section')
    row = (title, str(section).replace("\n", ""))
    return row

def writecsv(outpath, rows):
    with open(outpath, 'w') as fout:
        wt = csv.writer(fout)
        for row in rows:
            wt.writerow(row)
    

def cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str)
    parser.add_argument('-o', type=str,
                        default="/Users/AlexG/Downloads/tmp.csv")
    args = parser.parse_args()
    return args

def main():
    args = cmd()
    files = glob.glob(os.path.join(args.i, '*.html'))
    data = []
    for p in tqdm.tqdm(files):
        row = readone(p)
        data.append(row)

    writecsv(args.o, data)
    
    print('done.')

if __name__ == '__main__':
    main()