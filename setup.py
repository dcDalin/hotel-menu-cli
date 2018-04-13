from setuptools import setup

setup(
    name="hotel_menu",
    version='0.1',
    py_modules=['menu'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        mymenu=menu:cli
    ''',
)
