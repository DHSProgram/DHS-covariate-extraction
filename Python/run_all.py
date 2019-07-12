#!/usr/bin/env python3

import os
import sys
import time
import config as c
import spatial_covariates_buffer_extraction as run_buff
import spatial_covariates_point_extraction as run_pts
import combine_with_pandas as combine
import utils as u

try:
	# User input - should correspond to a value in config points, buffers, and rasters
	# to run, in command prompt, for example, python run_all.py clark_1866
	projection_group = sys.argv[1]
	u.assert_valid_user_input(projection_group)

	# Initialize log file
	u.verify_dir(c.log_pth)
	log_name = 'log_{}.txt'.format(time.strftime("%Y-%m-%d_%H-%M-%S"))
	log_out = os.path.join(c.log_pth, log_name)

	print('START')
	# Do zonal stats with buffers
	run_buff.main_code(c.rasters[projection_group],
	                   c.buffers[projection_group],
	                   c.csv_pth['buffers'],
	                   log_out,
	                   c.rasters['regex'],
	                   c.stats)

	# Assign raster value to points
	run_pts.main_code(c.rasters[projection_group],
	                  c.points[projection_group],
	                  c.csv_pth['points'],
	                  log_out,
	                  c.rasters['regex'])

	# Combine csv files. Where zonal stats is blank, assign point value.
	combine.main_code(c.csv_pth['buffers'], c.csv_pth['points'], c.csv_pth['combined'], log_out)

	print('FINISH')

except Exception as e:
	print('ERROR in run_all.py \n{}'.format(e))
