# must be run where 'Start Poshy' is located
curl https://raw.githubusercontent.com/nic68/minifetch/master/minifetch.py > minifetch.py
mv minifetch.py bin/bin/programs/
echo 'import bin.programs.minifetch' >> bin/bin/ayploader.py
echo 'Done'
