import json
import numpy as np
import pdb

from download_tiles import download_tiles
from merge_tiles import merge_tiles

# set http_proxy=http://127.0.0.1:8580
# set https_proxy=http://127.0.0.1:8580

ZOOM = 20

def read_lixiang_gps_boundary(case_id):
    FILE_NAME = '\\\\10.66.9.58\\share\\lixiang\\nihongjie\\data_20210318\\gps\\%s.gps' % case_id
    with open(FILE_NAME, 'r') as f:
        data = json.load(f)
        info = {}

        for i in data:   
            info[i['signalName']] = i['dps']

        lat_list = np.array([lat for _, lat in info['Location_lat'].items()])
        lon_list = np.array([lon for _, lon in info['Location_lon'].items()])

        min_lat, max_lat = lat_list.min(), lat_list.max()
        min_lon, max_lon = lon_list.min(), lon_list.max()

        #pdb.set_trace()

        return min_lat, min_lon, max_lat, max_lon

delta_lon = 0.0005
delta_lat = 0.0004

case_id = 'LW433B10XL1017477001100011609130926920'
min_lat, min_lon, max_lat, max_lon = read_lixiang_gps_boundary(case_id)

# min_lat -= delta_lat
# max_lat += delta_lat
# min_lon -= delta_lon
# max_lon += delta_lon

#download_tiles(ZOOM, min_lat, max_lat, min_lon, max_lon, satellite=True)
merge_tiles(ZOOM, min_lat, max_lat, min_lon, max_lon, satellite=True)
