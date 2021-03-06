from setuptools import find_packages
from setuptools import setup

VERSION='0.0.1'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    classifiers=[],
    description='',
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',        
    },
    keywords='',
    include_package_data=True,
    install_requires=[
    ],
    long_description=open('README.rst').read() + '\n' + open('CHANGES.rst').read(),
    name='plone_content_behavior',
    namespace_packages=[
    ],
    packages=find_packages(),
    url='',
    version=VERSION,
    zip_safe=False,
)
