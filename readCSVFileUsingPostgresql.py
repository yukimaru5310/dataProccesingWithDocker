import os
from glob import glob
import shutil
import csv
from os import listdir
from os.path import isfile, join
from config import config
import psycopg2


class readCSVFile:
    def __init__(self, inputFolderName):
        self.inputFolderName = inputFolderName
    def run(self):
        try:
            conn = None
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()

            self.enterDir(self.inputFolderName)
            onlyfiles = [f for f in listdir(self.inputFolderName) if isfile(join(self.inputFolderName, f))]
            for file in onlyfiles:
                file = self.inputFolderName +"/"+file
                csv_file = open(file, encoding="cp932", errors="",
                                 newline="")
                f = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator="\r\n", quotechar='"',
                               skipinitialspace=True)

            #header = next(f)
            #print(header)
            # read database configuration
                for row in f:
                    for i in range(len(row)):
                        if row[i] == '':
                            row[i] = '-1'

                    query = 'insert into  sensorData values(' + row[0] + ',\'' + row[1] + '\'' + ',' +'\'' + row[2] + ':00:00\'' + ',' + \
                            row[3] + ',' + row[4] + ',' + row[5] + ',' \
                            + row[6] + ',' + row[7] + ',' + row[8] + ',' + row[9] + ',' + row[10] + ',' + row[11] + ',' + \
                            row[12] + ',' + row[13] + ',' + row[14] + ',-1' + ',' + row[16] + ',' + row[17] + ',' + row[18] + ")"
                    print(query)
                    cur.execute(query)

                conn.commit()
            #close communication with the database
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


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
    obj = readCSVFile('.csv')
    obj.run()