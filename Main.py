import readCSVFileUsingPostgresql
import decompressZipFile
import downloadZipFileFromURL

import sys
class Main:
    if __name__ == '__main__':
        for year in [2019,2020]:
            for month in range(1,13):
                obj = None
                if month < 10:
                    obj = downloadZipFileFromURL.DownloadZipFileFromURL('https://soramame.env.go.jp/DownLoad/' + str(year)+ '0' + str(month) + '/' + str(year)+ '0' + str(month) + '_00.zip')

                else:
                    obj = downloadZipFileFromURL.DownloadZipFileFromURL(
                        'https://soramame.env.go.jp/DownLoad/' + str(year) + str(month) + '/' + str(
                            year) + str(month) + '_00.zip')
                obj.run()
                obj1 = decompressZipFile.decompressZipFile(obj.fileName,sys.argv[2])
                obj1.run()
                readCSVFileUsingPostgresql.readCSVFile(sys.argv[1]).run()
                obj1.remove_glob('0[1-9]')
                obj1.remove_glob('[1-3][0-9]')
                obj1.remove_glob('4[0-7]')
                obj1.remove_glob('pollution')
                obj1.remove_glob('pollutionData')
                obj1.remove_glob('*.zip')








                #onlyfiles = [f for f in listdir(obj1.getOutputFolder()) if isfile(join(obj1.getOutputFolder(), f))]
                #for fileName in onlyfiles: