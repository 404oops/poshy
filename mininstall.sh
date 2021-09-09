# must be run where 'Start Poshy' is located
curl https://raw.githubusercontent.com/nic68/minifetch/master/minifetch.py > minifetch.py
mv minifetch.py more/addons/minifetch.py
echo 'from .addons import minifetch' >> more/aya.py
echo 'Done'
