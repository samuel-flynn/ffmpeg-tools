"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'ReadMe.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ffmpeg-tools',

    version='0.1.0',

    description='A small set of FFMPEG scripts for trimming movies and GIFs',
    long_description=long_description,

    url='https://github.com/samuel-flynn/ffmpeg-tools',

    author='Samuel Flynn',
    author_email='flynn.samuel@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'Topic :: Multimedia :: Sound/Audio :: Editors',
        'Topic :: Multimedia :: Video :: Conversion',
        'Topic :: Multimedia :: Video :: Non-Linear Editor',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    keywords='ffmpeg gif mp4 avi video conversion converter trim trimming crop cropping',

    packages=find_packages('ffmpeg_tools'),

    install_requires=['docopt'],

    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    data_files=[('config_data', ['resources/config.ini'])],

    entry_points={
        'console_scripts': [
            'combine=ffmpeg_tools:combine',
        ],
    },
)