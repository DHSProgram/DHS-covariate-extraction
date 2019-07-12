call activate cov

echo "extracting from rasters"

python Python\run_all.py clark_1866
python Python\run_all.py evi_custom
python Python\run_all.py wgs84
python Python\run_all.py mollweide
pause
