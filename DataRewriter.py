import os
from PIL import Image
import piexif
from datetime import datetime

filePath = 'C:/Users/mtemprano/Desktop/pytest/'


def removeExtensions(fileName):
    return fileName.rsplit('.', 1)[0]


def createModifiedImage(fileName, date):
    im = Image.open(filePath + fileName)
    exif_dict = piexif.load(im.info['exif'])
    newdatetime = datetime.strptime(date, '%Y/%m/%d %H:%M').strftime(
        '%Y:%m:%d %H:%M:%S')
    exif_dict['0th'][piexif.ImageIFD.DateTime] = newdatetime
    exif_dict['Exif'][36867] = newdatetime
    exif_dict['Exif'][36868] = newdatetime
    exif_bytes = piexif.dump(exif_dict)
    im.save(filePath + 'patata' + '-v2-.jpeg', 'jpeg', exif=exif_bytes, quality='keep', optimize=True)


# --Start of program--
# Get files from directory
filesList = os.listdir(filePath)
# Format date from file name to be consumed later on
formattedDateList = list(map(removeExtensions, filesList))
for fileName in filesList:
    createModifiedImage(fileName, '2001/12/25 12:32')
print('finish')
