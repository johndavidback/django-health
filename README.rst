====
Django Health
====

Shows the health of your stack easily


Quick Start
-----------

1. Add 'health' to your INSTALLED_APPS setting:

    INSTALLED_APPS = (
        ...
        'health',
    )

2. Include the health URLconf in your project urls.py:

    url(r'^health/', include('health.urls')),

3. Run `python manage.py runserver`

4. Visit the health endpoint (http://127.0.0.1:8000/health/) for a `200 OK` to verify the site is up
