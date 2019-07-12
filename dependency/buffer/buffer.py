#!/usr/bin/env python2

#########################################################
# Turns a points layer into urban/rural buffers
# By Tom Fish
#########################################################

import arcpy
import os
import shutil

BASE_MXD_PATH = r"C:\DHS-covariate-extraction\dependency\buffer\mxd"
BASE_SHP_PATH = r"C:\DHS-covariate-extraction\dependency\buffer\shp"
BR_BUFFER_PATH = r"C:\DHS-covariate-extraction\buffers"

files = os.listdir(BASE_MXD_PATH)

for entry in files:
    print entry
    mxd = arcpy.mapping.MapDocument(BASE_MXD_PATH + "\\" + entry)
    lyrs = arcpy.mapping.ListLayers(mxd)
    lyr = lyrs[0]

    lyr.definitionQuery = """ "URBAN_RURA" = 'U' """
    arcpy.Buffer_analysis(lyr, BASE_SHP_PATH + r"\U.shp", "2 Kilometers")

    lyr.definitionQuery = """ "URBAN_RURA" = 'R' """
    arcpy.Buffer_analysis(lyr, BASE_SHP_PATH + r"\R.shp", "10 Kilometers")

    arcpy.Merge_management([BASE_SHP_PATH + r"\U.shp", BASE_SHP_PATH + r"\R.shp"], BR_BUFFER_PATH + "\\" + entry.split(".")[0] + ".shp")

    # Clean up
    torm = os.listdir(BASE_SHP_PATH)
    for thing in torm:
        os.remove(BASE_SHP_PATH + "//" + thing)
