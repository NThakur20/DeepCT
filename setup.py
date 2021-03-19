from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='DeepCT',
    version='0.1.0',
    url='https://github.com/AdeDZY/DeepCT',
    packages=['deepct'],
    long_description=readme,
    install_requires=[
        'tensorflow>2.0', 
    ],
)