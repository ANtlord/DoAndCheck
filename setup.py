import sys
from setuptools import find_packages, setup

def get_packages():
    kwargs = {
        'exclude': ['tests.*', 'tests'],
    }
    if 'flake8' in sys.argv:
        del kwargs['exclude']
    return find_packages(**kwargs)

setup(
    name='doandcheck',
    version='0.0.1',
    packages=get_packages(),
    url='',
    license='',
    author='ANtlord',
    author_email='',
    description='Simple check list that is based on Qt',
    setup_requires=['PyQt5==5.11.3'],
    install_requires=[],
    tests_require=[],
    include_package_data=True,
    entry_points = {
        'console_scripts': ['doandcheck=doandcheck.__main__:main'],
    }
)
