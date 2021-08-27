import DownloadZipfileFromURL
import zipfile
import os
from glob import glob
import shutil
import subprocess


class decompressZipFile:
    def __init__(self,inputFile,outputFolder):
        self.inputFile = inputFile
        self.outputFolder = outputFolder

    def getOutputFolder(self):
        return self.outputFolder

    def run(self):
        with zipfile.ZipFile(self.inputFile, 'r') as zip_ref:
            zip_ref.extractall(self.outputFolder)
            zFiles = glob(os.path.join(self.outputFolder, '*.zip'))
            for zFile in zFiles:
                subprocess.run(['unzip', zFile])

    '''Delete the extracted files and directories.'''
    def remove_glob(self,pathname,recursive=True):
        for p in glob(pathname, recursive=recursive):
            if os.path.isfile(p):
                os.remove(p)
            if os.path.isdir(p):
                shutil.rmtree(p)
if __name__ == '__main__':
    obj = decompressZipFile(DownloadZipfileFromURL.obj.getFileName())
    obj.run()