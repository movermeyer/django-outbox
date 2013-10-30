import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-outbox',
    version='0.3',
    packages=['django_outbox'],
    include_package_data=True,
    license='The MIT License (MIT)',
    description='Django Outbox is an app that enable you to see the emails sent by your project through the web browser.',
    long_description=README,
    url='https://github.com/poiati/django-outbox',
    author='Paulo Poiati',
    author_email='paulo@poiati.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: The MIT License (MIT)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
