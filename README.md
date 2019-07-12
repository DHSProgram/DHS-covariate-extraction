# DHS Covariate Extraction

Python code for the extraction of covariates from other sources for DHS clusters. For the results of this kind of processing, please see our publicly available [Geospatial Covariates (GC) files](https://spatialdata.dhsprogram.com/covariates/).

## Background and process
For a more detailed overview of how the extraction process works and information about the rasters that we use for our covariate (GC) files, please see:

Mayala, Benjamin, Thomas D. Fish, David Eitelberg, and Trinadh Dontamsetti. 2018. [The DHS Program Geospatial Covariate Datasets Manual (Second Edition)](https://spatialdata.dhsprogram.com/references/DHS%20Covariates%20Extract%20Data%20Description%202.pdf). Rockville, Maryland, USA: ICF.

## Python notes
This repository breaks best practices and has both Python 2 and Python 3 code. All of the code in the [/Python/](/Python/) folder

## Setup
### Initial Setup

### Per Dataset Setup


## Folder Structure
### /buffers/
Your 2 km and 10km buffers go in this folder. We use these file names for the following projections

* clark1866.shp
* evi_custom.shp
* mollweide.shp
* wgs84.shp

Python code to generate the buffers from the points in the points folder can be found in `/dependency/buffer/buffer.py`

### /csvs_buffers/

### /csvs_combined/
The final output

### /csvs_points/

### /dependency/

### /logs/

### /points/
Your points from [The DHS Program](https://dhsprogram.com/data/available-datasets.cfm). For more information about accessing the GPS data, please [see this post](https://userforum.dhsprogram.com/index.php?t=msg&th=6448&start=0&) in our [user forum](https://userforum.dhsprogram.com/). We use these file names for the following projections

* clark1866.shp
* evi_custom.shp
* mollweide.shp
* wgs84.shp

### /Python/

### /rasters/
The raster files that you want to get extractions from
