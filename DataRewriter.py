import os
from PIL import Image
import piexif
from datetime import datetime

filePath = 'C:/Users/mtemprano/Desktop/pytest/'


def createModifiedImage(targetFilePath, fileName, date):
    im = Image.open(filePath + fileName)
    exif_dict = piexif.load(im.info['exif'])
    newdatetime = datetime.strptime(date, '%Y/%m/%d %H:%M').strftime(
        '%Y:%m:%d %H:%M:%S')
    exif_dict['0th'][piexif.ImageIFD.DateTime] = newdatetime  # 306
    exif_dict['Exif'][36867] = newdatetime
    exif_dict['Exif'][36868] = newdatetime
    exif_bytes = piexif.dump(exif_dict)
    im.save(targetFilePath + fileName, 'jpeg', exif=exif_bytes, quality='keep', optimize=True)


# --Start of program--

# Get files from directory
filesList = os.listdir(filePath)

# Create new directory
targetFilePath = filePath + 'updated images/'
os.mkdir(targetFilePath)

# Iterate through files
for fileName in filesList:
    createModifiedImage(targetFilePath, fileName, '2001/12/25 12:32')

print('finish')
