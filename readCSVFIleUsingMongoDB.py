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
        client = MongoClient("mongodb://localhost:30000/?retryWrites=false")
        db = client["DataMining"]
        collection = db["US_airPollution_PM25"]
        onlyfiles = [f for f in listdir(self.inputFolderName) if isfile(join(self.inputFolderName, f))]
        for file in onlyfiles:
            query=[]
            print(file)
            cnt=0
            file = self.inputFolderName +"/"+file
            csv_file = open(file, encoding="cp932", errors="",newline="")
            lines = csv.DictReader(csv_file, delimiter=',', skipinitialspace=True)
            #header = next(f)
            #print(header)
        # read database configuration
            for line in lines:
                for index in line:
                    if line[index] == '':
                        line[index] = '-1'
                query.append(line)
                if len(query)==100000:
                    cnt+=len(query)
                    collection.insert_many(query)
                    query=[]
            cnt+=len(query)
            print(cnt)
            collection.insert_many(query)
    # close communication with the database
        client.close()

if __name__ == '__main__':
    obj = readCSVFile('../../Data/US_airPollution_PM25')
    obj.run()
