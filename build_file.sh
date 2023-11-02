# build_files.sh
pip install -r requirements.txt

# make migrations
pthon3.9 manage.py migrate 
python3.9 manage.py collectstatic
