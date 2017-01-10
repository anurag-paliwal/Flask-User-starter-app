from setuptools import setup, find_packages

setup(
    name='flaskuserapp',
    version="1.0",
    description="Flask User starter app - a simple app to demonstrate flask",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts = ["manage.py","wsgi.py"],
    install_requires=[
        "Flask==0.12",
        "Flask-Login==0.4.0",
        "Flask-Migrate==2.0.2",
        "Flask-Script==2.0.5",
        "Flask-SQLAlchemy==2.1",
        "Flask-User==0.6.10",
        "Flask-WTF==0.13.1",
        "MySQL-python",
        "uwsgi"
    ],
    extras_require={
        "test": [
            "pytest==3.0.5",
            "pytest-flask==0.10.0",
            "pytest-cov==2.4.0"
        ]
    }

)
