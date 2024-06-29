from setuptools import setup, find_packages
import os

# Check if requirements.txt exists and read it
if os.path.exists('requirements.txt'):
    with open('requirements.txt') as f:
        required = f.read().splitlines()
else:
    required = []

setup(
    name='rf2rnd',
    version='0.1.0',
    packages=find_packages(),
    install_requires=required,
    author='Your Name',
    author_email='shadi.alhaj.ch@gmail.com',
    description='RF noise to random number generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pyshadi/rf2rnd',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
