# coding: utf-8
"""
Setup module.
"""


# External imports
from setuptools import find_packages
from setuptools import setup


# Run setup
setup(
    name='AoikInspectArgs',

    version='0.2.0',

    description='Inspect function arguments.',

    long_description="""`Documentation on Github
<https://github.com/AoiKuiyuyou/AoikInspectArgs>`_""",

    url='https://github.com/AoiKuiyuyou/AoikInspectArgs',

    author='Aoi.Kuiyuyou',

    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='inspect argument',

    package_dir={
        '': 'src'
    },

    packages=find_packages('src'),

    include_package_data=True,
)
