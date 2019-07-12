#!/usr/bin/env python3

import os
import config as c

def write_to_log(string, log):
    print(string)
  
    with open(log, 'a') as l:
        l.write('\n' + string)

def verify_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        print('created dir: {}'.format(path))

def assert_valid_user_input(user_input):
    assert user_input in c.points, 'ERROR: \'{}\' projection group not in config.points'.format(user_input)
    assert user_input in c.buffers, 'ERROR: \'{}\' projection group not in config.buffers'.format(user_input)
    assert user_input in c.rasters, 'ERROR: \'{}\' projection group not in config.rasters'.format(user_input)
