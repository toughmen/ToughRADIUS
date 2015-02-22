#!/usr/bin/python

from setuptools import setup, find_packages
import toughradius

version = toughradius.__version__

install_requires = [
    'DBUtils>=1.1',
    'MySQL-python>=1.2.5',
    'Mako>=0.9.0',
    'Beaker>=1.6.4',
    'MarkupSafe>=0.18',
    'PyYAML>=3.10',
    'SQLAlchemy>=0.9.8',
    'Twisted>=13.0.0',
    'autobahn>=0.9.3-3',
    'bottle>=0.12.7',
    'six>=1.8.0',
    'tablib>=0.10.0',
    'zope.interface>=4.1.1',
    'pycrypto==2.6.1',
    'sh==1.11'
]
install_requires_empty = []

package_data={
    'toughradius': [
        'console/admin/views/*',
        'console/customer/views/*',
        'console/static/css/*',
        'console/static/fonts/*',
        'console/static/img/*',
        'console/static/js/*',
        'console/static/favicon.ico',
        'radiusd/dicts/*'
    ]
}


setup(name='toughradius',
      version=version,
      author='jamiesun',
      author_email='jamiesun.net@gmail.com',
      url='https://github.com/talkincode/ToughRADIUS',
      license='BSD',
      description='RADIUS Server',
      long_description=open('README.md').read(),
      classifiers=[
       'Development Status :: 6 - Mature',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: BSD License',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       "Programming Language :: Python :: Implementation :: PyPy"
       'Topic :: Software Development :: Libraries :: Python Modules',
       'Topic :: System :: Systems Administration :: Authentication/Directory',
       ],
      packages=find_packages(),
      package_data=package_data,
      keywords=['radius', 'authentication'],
      zip_safe=True,
      include_package_data=True,
      install_requires=install_requires,
      scripts=['bin/toughrad','bin/toughctl'],
      tests_require='nose>=0.10.0b1',
      test_suite='nose.collector',
)