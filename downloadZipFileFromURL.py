import requests
import zipfile
import os
from glob import glob
import sys
import shutil
import subprocess
import csv

class DownloadZipFileFromURL:
    def __init__(self,url):
        self.url = url
        self.fileName = self.url.split('/')[-1]

    def run(self):
        r = requests.get(self.url, stream=True)
        with open(self.fileName, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        return False

    def getFileName(self):
        return self.fileName


if __name__ == '__main__':
    if len(sys.argv) == 4:
        ym = sys.argv[2] + sys.argv[3]
        obj = DownloadZipFileFromURL('http://soramame.taiki.go.jp/DownLoad/'+ ym +'/' + ym + '_00.zip')
    else:
        print('Please provide 3 input patersm...')