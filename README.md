# DHS Covariate Extraction

Python code for the extraction of covariates from other sources for DHS clusters. For the results of this kind of processing, please see our publicly available [Geospatial Covariates (GC) files](https://spatialdata.dhsprogram.com/covariates/).

## Background and process
There are an increasing number of rasters

For a more detailed overview of how the extraction process works and information about the rasters that we use for our covariate (GC) files, please see:

Mayala, Benjamin, Thomas D. Fish, David Eitelberg, and Trinadh Dontamsetti. 2018. [The DHS Program Geospatial Covariate Datasets Manual (Second Edition)](https://spatialdata.dhsprogram.com/references/DHS%20Covariates%20Extract%20Data%20Description%202.pdf). Rockville, Maryland, USA: ICF.

## Python version warning
This repository breaks best practices and has both Python 2 and Python 3 code. All of the code in the [/dependency/buffer/](/dependency/buffer/) folder uses Python 2 and all of the files in the [/Python/](/Python/) folder uses Python 3. [Hashbang](https://en.wikipedia.org/wiki/Shebang_(Unix)) such as `#!/usr/bin/env python3` are at the beginning of each file as an attempt to minimize confusion.

ESRI ArcMap 10.X still uses Python 2, sorry.

## Setup
### Initial Setup

1. Edit the base paths in [/Python/config.py](/Python/config.py) to the paths of the points, buffers, and rasters folders on your local machine. Save that file.
2. Populate the [/raster/](/raster/) folder structure with the raster data that you would like to extract values from. Example folders were added as an attempt to help you figure out the data management. For more information about the data management see [the rasters section](#rasters)
3. (If you are going to use ESRI ArcMap to make the buffers) Edit the paths in the [/dependency/buffer/buffer.py](/dependency/buffer/buffer.py) to reflect the paths to the mxd, shp, and buffers folders on your computer.
4. You may want to delete the `.gitignore` files found throughout the folder structure to prevent a script from tripping.

#### Dependencies
  A full list of the dependencies needed to run the extraction code ([/Python/](/Python/)) can be found [here](/Python/conda_environment.yml). We utilize a conda environment to sandbox dependencies of different processes. GDAL, RasterIO, and Fiona are all testy to install in Windows. Check with each package for the best practices for installing it.

### Per Dataset Setup
1. Download your points from the from [The DHS Program](https://dhsprogram.com/data/available-datasets.cfm) website.
2. Open the points in you favorite GIS program and save them as
3. (If you are going to use ESRI ArcMap to make the buffers) Open each ArcMap document and add the points that you added in the points folder.

## Folder Structure
### /buffers/
Your 2 km and 10km buffers go in this folder. We use these file names for the following projections

* clark1866.shp
* evi_custom.shp
* mollweide.shp
* wgs84.shp

Python code to generate the buffers from the points in the points folder can be found in [/dependency/buffer/buffer.py](/dependency/buffer/buffer.py)

### /csvs_buffers/
The output from the first attempt to extract values using the buffers.

### /csvs_combined/
The final output of the extraction process.

### /csvs_points/
The output from the second attempt to extract values using the points.

### /dependency/
Three of the covariate rasters that we extract from use an offbeat projection that isn't found ESRI ArcMap (we call it evi_custom in the folder structure)

#### /dependency/buffer/
Several map documents and a Python 2 script for creating the buffers.

### /logs/

### /points/
Your points from [The DHS Program](https://dhsprogram.com/data/available-datasets.cfm). For more information about accessing the GPS data, please [see this post](https://userforum.dhsprogram.com/index.php?t=msg&th=6448&start=0&) in our [user forum](https://userforum.dhsprogram.com/). We use these file names for the following projections

* clark1866.shp
* evi_custom.shp
* mollweide.shp
* wgs84.shp

### /rasters/
The raster files that you want to get extractions from broken down by projection and then further broken down by source.

## Questions

For questions please email: gpsrequests@dhsprogram.com
