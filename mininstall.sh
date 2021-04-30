# must be run where 'Start Poshy' is located
curl https://raw.githubusercontent.com/nic68/minifetch/master/minifetch.py > minifetch.py
mv minifetch.py poshy/addons/minifetch.py
echo 'from .addons import minifetch' >> poshy/aya.py
echo 'Done'
