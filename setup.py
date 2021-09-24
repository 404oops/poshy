from setuptools import setup
long_description = (this_directory / "readme.md").read_text()
setup(
    name='poshy',
    packages=['aya'],
    version='1.2',
    description='An extensible shell written in python',
    long_description=long_description,
    long_description_content_type='text/markdown'
    scripts=['bin/poshy']
)