import io
import os
import re
from setuptools import setup, find_packages


def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, 'albumentations_gui', '__init__.py')
    with io.open(version_file, encoding='utf-8') as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)

setup(
    name='albumentations_gui',
    version=get_version(),
    description='GUI for albumentations library',
    long_description='GUI for albumentations library',
    long_description_content_type='text/markdown',
    author='Druzhinin Mikhail',
    license='MIT',
    url='https://github.com/Dipet/albumentations_gui',
    packages=find_packages(),
    install_requires=['albumentations', 'PyQt5'],
    extras_require={},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={'console_scripts': ['albumentations_gui = albumentations_gui.albumentations_gui:main']}
)
