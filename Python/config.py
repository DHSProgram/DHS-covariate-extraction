#!/usr/bin/env python3

import os

# Variables defining paths to points, buffers, and rasters
points_base_path =  r'C:\DHS-covariate-extraction\points'
buffers_base_path = r'C:\DHS-covariate-extraction\buffers'
rasters_base_path = r'C:\DHS-covariate-extraction\rasters'

points = {'clark_1866': os.path.join(points_base_path, 'clark1866.shp'),
          'evi_custom': os.path.join(points_base_path, 'evi_custom.shp'),
          'wgs84':      os.path.join(points_base_path, 'wgs84.shp'),
          'mollweide':  os.path.join(points_base_path, 'mollweide.shp')}

buffers = {'clark_1866': os.path.join(buffers_base_path, 'clark1866.shp'),
           'evi_custom': os.path.join(buffers_base_path, 'evi_custom.shp'),
           'wgs84':      os.path.join(buffers_base_path, 'wgs84.shp'),
           'mollweide':  os.path.join(buffers_base_path, 'mollweide.shp')}

rasters = {'clark_1866': os.path.join(rasters_base_path, 'clark_1866'),
           'evi_custom': os.path.join(rasters_base_path, 'evi_custom'),
           'wgs84':      os.path.join(rasters_base_path, 'wgs84'),
           'mollweide':  os.path.join(rasters_base_path, 'mollweide'),
           'regex': '/**/*.tif'}  # 'regex': '/**/*_landMasked.tif'

# Log file output locations
log_pth = os.path.join(os.path.split(buffers_base_path)[0], 'logs')

# CSV output locations
csv_pth = {'points':  os.path.join(os.path.split(points_base_path)[0], 'csvs_points'),
           'buffers': os.path.join(os.path.split(buffers_base_path)[0], 'csvs_buffers'),
           'combined':os.path.join(os.path.split(buffers_base_path)[0], 'csvs_combined')}

# Statistics for zonal stats
stats = "count sum mean majority nodata"  # count sum mean majority nodata -- See RasterStats for full list
