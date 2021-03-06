#!/usr/bin/env python3

from rasterstats import point_query
import csv
from timeit import default_timer as timer
import time
import os
import sys
import glob
from osgeo import gdal, ogr, osr
import utils as u

def do_point_query(points, raster, csv_pth, num, log_out):
    try:
        u.verify_dir(csv_pth)
        dataset = raster.split('\\')[-2].replace(' ', '_')
        raster_name_to_csv = os.path.basename(raster).replace('.tif', '.csv')
        csv_name = '__'.join([dataset, raster_name_to_csv])
        csv_out = os.path.join(csv_pth, csv_name)
        
        start = timer()
        u.write_to_log('  {}) Raster: {}'.format(num, os.path.basename(raster)), log_out)
        
        stats = point_query(points, raster, interpolate='nearest', geojson_out=True)
        print('    point_query... ({} sec.)'.format(round(timer()-start, 2)))

        start = timer()
        attributes = []
        for item in stats:
            #print ('{}'.format(item['properties']))
            attributes.append(item['properties'])
        print('    append dicts... ({} sec.)'.format(round(timer()-start, 2)))

        start = timer()
        with open(csv_out, 'w', newline='') as outfile:
            fp = csv.DictWriter(outfile, attributes[0].keys())
            fp.writeheader()
            fp.writerows(attributes)
        print('    write to csv... ({} sec.)'.format(round(timer()-start, 2)))
        u.write_to_log('    CSV file: {}'.format(csv_out), log_out)
        u.write_to_log('    Log file: {}'.format(log_out), log_out)
        
    except Exception as e:
        u.write_to_log(str(e), log_out)
        u.write_to_log('FINISH POINTS: {}'.format(time.strftime("%Y-%m-%d  %H:%M:%S")), log_out)


def main_code(raster_dir, pts, csv_path, log, raster_regex,):
    # Main stuff
    start_all = timer()
    u.write_to_log('\nSTART POINTS: {}'.format(time.strftime("%Y-%m-%d  %H:%M:%S")), log)
    raster_list = []
    for filename in glob.iglob(raster_dir+raster_regex, recursive=True):
        raster_list.append(filename)
        
    count = 0
    for tif in raster_list:
        count+=1
        try:
            do_point_query(pts, tif, csv_path, count, log)
        except Exception as e:
            print(e)

    u.write_to_log('FINISH POINTS: {}\nELAPSED TIME: ({} sec.)'.format(time.strftime("%Y-%m-%d  %H:%M:%S"), round(timer()-start_all, 2)), log)
