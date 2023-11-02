# build_files.sh
pip install -r requirements.txt

# make migrations

python3.9 manage.py migrate 
python3.9 manage.py collectstatic

python3.9 manage.py createsuperuser --username yonas --email your_email@example.com --noinput

