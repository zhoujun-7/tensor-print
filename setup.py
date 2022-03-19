from gettext import install
from setuptools import setup, find_packages

setup(
    name = 'tensor-print',
    version = '0.0.2',
    keywords='tensor-print',
    description='print shape, max, min, std of tensor or ndarray',
    license = 'MIT License',
    url = 'https://github.com/zhoujun-7/tensor-print',
    author = 'zhou jun',
    author_email = 'jchow@cug.edu.cn',
    packages=find_packages(),
    include_package_data=True,
    platforms = 'any',
    install_requires=[],
)