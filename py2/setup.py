#!/usr/bin/env python

import setuptools
#import sys

def readme():
    with open('TITLE.txt') as f:
         return f.readline().rstrip('\n')

def longDescription():
    with open('README.rst') as f:
         return f.read()


#from setuphelpers import get_version, require_python
#from setuptools import setup


#__version__ = get_version('unisos2/icm/__init__.py')
__version__ = '0.19'


requires = [
    'enum34',
    'unisos2.ucf',
    'unisos2.icm',
    'unisos2.common',    
    'blee.icmPlayer',
    'bisos.common',
    'bisos.platform',
    'pyjwt',
    'bravado',
    'PyJWT',  # Needed for bearerToken
]


#print('Setting up under python version %s' % sys.version)
#print('Requirements: %s' % ','.join(requires))


scripts = [
    "./bin/rinvoker.py",
    "./bin/wsInvokerIcmExamples.py",
    "./bin/bearerTokenProc.py",
    "./bin/mmwsBaseManage.py",
    "./bin/opScnPetstore.py",
    "./bin/rinvokerPetstore.py",
]


setuptools.setup(
    name='unisos2.mmwsIcm',
    version=__version__,
    namespace_packages=['unisos2'],
    packages=setuptools.find_packages(),
    scripts=scripts,
    # data_files=[
    #     ('pkgInfo', ["unisos2/pkgInfo/fp/icmsPkgName/value"]),
    # ],
    #package_dir={'unisos2.marme': 'unisos2'},
    # package_data={
    #     'unisos2.marme': ['pkgInfo/fp/icmsPkgName/value'],
    # },
    # package_data={
    #     '': ['unisos2/marme/resolv.conf'],
    # },
    include_package_data=True,
    zip_safe=False,
    author='Mohsen Banan',
    author_email='libre@mohsen.1.banan.byname.net',
    maintainer='Mohsen Banan',
    maintainer_email='libre@mohsen.1.banan.byname.net',
    url='http://www.by-star.net/PLPC/180047',
    license='AGPL',
    description=readme(),
    long_description=longDescription(),
    download_url='http://www.by-star.net/PLPC/180047',
    install_requires=requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )
