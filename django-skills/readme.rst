=====
Skills
=====

Skills is a Django app 
Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "skills" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'skills',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('skills/', include('skills.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a skill (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/skills/ 

Build
------

1. python setup.py sdist 

2. python -m pip install django-skills/dist/django-polls-0.1.tar.gz