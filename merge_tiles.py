from PIL import Image
import sys, os
from gmap_utils import *

def merge_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite=True):
    
    TYPE, ext = 'r', 'png'
    if satellite:
        TYPE, ext = 's', 'jpg'
    
    x1, y1 = latlon2xy(zoom, lat_start, lon_start)
    x2, y2 = latlon2xy(zoom, lat_stop, lon_stop)

    y_start = min(y1, y2)
    y_stop = max(y1, y2)

    x_start = min(x1, x2)
    x_stop = max(x1, x2)
    
    print("x range", x_start, x_stop)
    print("y range", y_start, y_stop)
    
    w = (x_stop - x_start) * 256
    h = (y_stop - y_start) * 256
    
    print("width:", w)
    print("height:", h)
    
    result = Image.new("RGBA", (w, h))
    
    for x in range(x_start, x_stop):
        for y in range(y_start, y_stop):
            
            filename = "%d_%d_%d_%s.%s" % (zoom, x, y, TYPE, ext)
            
            if not os.path.exists(filename):
                print("-- missing", filename)
                continue
                    
            x_paste = (x - x_start) * 256
            y_paste = h - (y_stop - y) * 256
            
            #try:
            i = Image.open(filename)
            #except Exception, e:
            #    print("-- %s, removing %s" % (e, filename))
            #    trash_dst = os.path.expanduser("~/.Trash/%s" % filename)
            #    os.rename(filename, trash_dst)
            #    continue
            
            result.paste(i, (x_paste, y_paste))
            
            del i
    
    result.save("map_%s.%s" % (TYPE, 'png'))

if __name__ == "__main__":
    
    #zoom = 15

    #lat_start, lon_start = 46.53, 6.6
    #lat_stop, lon_stop = 46.49, 6.7

    zoom = 20

    lat_start, lon_start = 30.49388, 103.57587
    lat_stop, lon_stop = 30.49217, 103.57899


    merge_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite=True)
