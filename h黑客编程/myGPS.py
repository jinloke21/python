import exifread
import re



def main(imagename):
    f = open(imagename,"rb")
    tags = exifread.process_file(f)
    #print(tags)
    GPS = {}
    for tag , value in tags.items():
        if "GPS GPSLatitude" in tag:
            GPS['纬度'] = str(tags['GPS GPSLatitude'])
        elif "GPS GPSLongitude" in tag:
            GPS['经度'] = str(value)
#            print(GPS['经度'])
        elif "Image DateTime" in tag:
            GPS['时间'] = str(value)
 #           print(GPS['时间'])
    print(GPS)
    
if __name__ == "__main__":
    main('/root/桌面/b.jpg')
