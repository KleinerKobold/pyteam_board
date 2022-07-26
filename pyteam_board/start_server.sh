source ../venv/bin/activate
cd ../django-skills
python3 setup.py sdist 
python3 -m pip install django-skills/dist/django-skills-0.1.tar.gz
cd ../pyteam_board
python3 manage.py runserver
