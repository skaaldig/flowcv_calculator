from setuptools import setup

setup(
    name='flowcv',
    version='0.1.0',
    packages=['flowcv'],
    entry_points={
        'console_scripts': [
            'flowcv = flowcv.__main__:main'
        ]
    })
