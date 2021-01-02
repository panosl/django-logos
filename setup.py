#!/usr/bin/env python
from distutils.core import setup

from logos import VERSION


setup(name='logos',
    version=VERSION,
    description='Phaethon\'s Django based blog engine',
    author='Panos Laganakos',
    author_email='panos.laganakos@gmail.com',
    packages=['logos'],
    install_requires=[
        'Django',
        'unicode-slugify',
        'django-contrib-comments',
        'django-taggit',
    ],
    classifiers=['Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'],
)
