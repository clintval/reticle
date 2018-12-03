import setuptools

from pathlib import Path
from setuptools import find_packages

PACKAGE = 'reticle'
VERSION = '0.1.0'

setuptools.setup(
    name=PACKAGE,
    version=VERSION,
    author='clintval',
    author_email='valentine.clint@gmail.com',
    description='Python 3.6+ library for submitting to AWS Batch interactively.',
    url=f'https://github.com/clintval/{PACKAGE}',
    download_url=f'https://github.com/clintval/{PACKAGE}/archive/v{VERSION}.tar.gz',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    license='MIT',
    zip_safe=False,
    packages=[PACKAGE],
    install_requires=[
        'awscli',
        'boto3',
        'custom_inherit',
        'logzero',
        'sample_sheet',
        'smart_open',
    ],
    keywords='AWS Batch job submission',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Documentation': f'https://{PACKAGE}.readthedocs.io',
        'Issue-Tracker': f'https://github.com/clintval/{PACKAGE}/issues',
    },
)
