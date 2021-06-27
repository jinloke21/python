from PIL import Image
from PIL.ExifTags import TAGS


def testimage(imagename):
    try:
        exifData = {}
        imagefile = Image.open(imagename)
        info = imagefile._getexif()
        if info:
            for (tag,value) in info.items():
                decode = TAGS.get(tag,tag)
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print(imagename+' GPS')
    except:
        pass


testimage('/newFS/py/pachong/two/pic/1.jpg')

