#!/usr/bin/python

import urllib.request
import os, sys
from gmap_utils import *
import numpy as np

import time
import random
import pdb

def download_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite=True):
    print('download_tiles lat_start(%.7f) lat_stop(%.7f) lon_start(%.7f) lon_stop(%.7f)' % 
        (lat_start, lat_stop, lon_start, lon_stop))


    x1, y1 = latlon2xy(zoom, lat_start, lon_start)
    x2, y2 = latlon2xy(zoom, lat_stop, lon_stop)
    
    y_start = min(y1, y2)
    y_stop = max(y1, y2)

    x_start = min(x1, x2)
    x_stop = max(x1, x2)

    print("x range", start_x, stop_x)
    print("y range", start_y, stop_y)
    
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1'
    headers = { 'User-Agent' : user_agent }
    
    for x in range(start_x, stop_x):
        for y in range(start_y, stop_y):
            
            url = None
            filename = None
            
            if satellite:
                url = "https://khms1.googleapis.com/kh?v=904&hl=en-US&x=%d&y=%d&z=%d" % (x, y, zoom)
                filename = "%d_%d_%d_s.jpg" % (zoom, x, y)
            else:
                url = "http://mt1.google.com/vt/lyrs=h@162000000&hl=en&x=%d&s=&y=%d&z=%d" % (x, y, zoom)
                filename = "%d_%d_%d_r.png" % (zoom, x, y)
    
            if not os.path.exists(filename):
                req = urllib.request.Request(url, data=None, headers=headers)
                response = urllib.request.urlopen(req)
                response_text = response.read()
                
                if response_text.startswith(b"<html>"):
                    print("-- forbidden", filename)
                    sys.exit(1)
                
                print("-- saving", filename)
                
                f = open(filename,'wb')
                f.write(response_text)
                f.close()
                
                time.sleep(2 + random.random())

if __name__ == "__main__":
    zoom = 20

    #lat_start, lon_start = 30.49388, 103.57587
    #lat_stop, lon_stop = 30.49217, 103.57899

    download_tiles(zoom, lat_start, lat_stop, lon_start, lon_stop, satellite=True)
