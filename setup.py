#from distutils.core import setup
from setuptools import setup

setup(
    name='cutesong',
    version='0.1.0',
    author='alfateam123',
    author_email='alfateam123@gmail.com',
    packages=['cutesong'],
    #scripts=['scripts/list'],
    url='http://github.com/alfateam123/cutesong',
    #license='LICENSE.txt',
    description='openings.moe REST API Library',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.5.0"
    ],
    classifiers=[
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    #"Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards",
    "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    test_suite = "tests"
)
