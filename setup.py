from setuptools import setup, find_packages

setup(
    name='jot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pymongo',  
        'click'
    ],
    entry_points={
        'console_scripts': [
            'j=jot.jot:main',
        ],
    },
)
