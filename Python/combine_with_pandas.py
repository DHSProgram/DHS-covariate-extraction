import pandas as pd
import csv
import os
import glob
import time
from timeit import default_timer as timer
import utils as u

def main_code(buff_dir, pt_dir, combine_dir, log):
    u.verify_dir(combine_dir)
    start_all = timer()
    u.write_to_log('\nSTART COMBINE: {}'.format(time.strftime("%Y-%m-%d  %H:%M:%S")), log)
    buff_list = []
    for filename in glob.iglob(buff_dir+'/*.csv'):
        buff_list.append(filename)

    pt_list = []
    for filename in glob.iglob(pt_dir+'/*.csv'):
        pt_list.append(filename)

    match_count = 0
    for buff_csv in buff_list:
        buff_name = os.path.basename(buff_csv)
        process_buff = buff_csv
        for pt_csv in pt_list:
            pt_name = os.path.basename(pt_csv)
            if buff_name==pt_name:
                process_pt = pt_csv
                match_count+=1
                u.write_to_log('  {}) buffers: {}   points: {}'.format(match_count, buff_name, pt_name), log)

                #csv_name = os.path.basename(os.path.basename(buff_csv).replace('.csv', '_pandas.csv'))
                out_csv = os.path.join(combine_dir, buff_name)

                buff_df = pd.read_csv(buff_csv, dtype='object')
                pt_df = pd.read_csv(pt_csv, dtype='object')

                print('    buff shape: {}'.format(buff_df.shape))
                print('    pt shape:   {}'.format(pt_df.shape))
  
                merged = pd.merge(left=buff_df,right=pt_df, on='DHSID')
                print('    merge shape: {}'.format(merged.shape))

                for col in list(merged):
                    if col.endswith("_y"):
                        merged = merged.drop(str(col), 1)

                # These select columns by name and merge point values into them if 
                # the buffer analysis resulted in a blank value.
                try: merged.loc[merged['mean'].isnull(),'mean'] = merged['value']
                except: print('      no MEAN column')
                
                try: merged.loc[merged['sum'].isnull(),'sum'] = merged['value']
                except: print('      no SUM column')
                
                try: merged.loc[merged['majority'].isnull(),'majority'] = merged['value']
                except: print('      no MAJORITY column')

                try: merged = merged.drop('nodata', 1)
                except: print('      no NODATA column')
                merged = merged.drop('value', 1)

                merged.to_csv(out_csv, sep=',')
    
    u.write_to_log('FINISH COMBINE: {}\nELAPSED TIME: {} sec.'.format(time.strftime("%Y-%m-%d  %H:%M:%S"), round(timer()-start_all, 3)), log)
