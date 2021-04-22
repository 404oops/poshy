# must be run where 'Start Poshy' is located
curl https://raw.githubusercontent.com/nic68/minifetch/master/minifetch.py > minifetch.py
mv minifetch.py bin/bin/programs/
echo 'import bin.program.minifetch' >> bin/ayploader.py
echo 'Done'
