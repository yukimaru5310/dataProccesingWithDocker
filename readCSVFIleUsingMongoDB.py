import os
from glob import glob
import shutil
import csv
from os import listdir
from os.path import isfile, join
from pymongo import MongoClient


class readCSVFile:
    def __init__(self, inputFolderName):
        self.inputFolderName = inputFolderName
    def run(self):
        client = MongoClient('163.143.165.128',27017)
        db = client["airPollution"]
        collection = db["sensorData"]

        self.enterDir(self.inputFolderName)
        onlyfiles = [f for f in listdir(self.inputFolderName) if isfile(join(self.inputFolderName, f))]
        for file in onlyfiles:
            file = self.inputFolderName +"/"+file

            f = csv.reader(file, delimiter=',', doublequote=True, lineterminator="\r\n", quotechar='"',
                           skipinitialspace=True)
        #header = next(f)
        #print(header)
        # read database configuration

            for row in f:
                for i in range(len(row)):
                    if row[i] == '':
                        row[i] = '-1'
                query = {'sensorID': row[0],
                         'date': row[1],
                         'time': '\'' + row[2] + '\'' + ':00:00',
                         'SO2': row[3],
                         'NO': row[4],
                         'NO2': row[5],
                         'NOx': row[6],
                         'CO': row[7],
                         'Ox': row[8],
                         'NMHC': row[9],
                         'CH4': row[10],
                         'THC': row[11],
                         'SPN': row[12],
                         'PM2.5': row[13],
                         'SP': row[14],
                         'WD': '-1',
                         'WS': row[16],
                         'TEMP': row[17],
                         'HUM': row[18]
                         }

                collection.insert_one(query)

    # close communication with the database
        client.close()



    '''If the desired csv file already exists, load the CSV file as is and exit.
    Otherwise, it will create a directory on the received path and move the csv file to it.'''
    def enterDir(self,path):
        if not os.path.exists(path):
            os.makedirs(path)
            for p in range(1,48):
                if p < 10:
                    for f in glob('0'+str(p)+'/*.csv', recursive=True):
                        shutil.move(f, path)
                else:
                    for f in glob(str(p)+'/*.csv',recursive=True):
                        shutil.move(f, path)


if __name__ == '__main__':
    obj = readCSVFile('station_info.csv')
    obj.run()
