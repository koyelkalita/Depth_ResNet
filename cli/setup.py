from setuptools import setup, find_packages

setup(
    name='polypsnet',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'Pillow',
        'matplotlib',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'polypsnet=polypsnet.cli:main',
        ],
    },
)