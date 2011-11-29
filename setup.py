from setuptools import find_packages
from setuptools import setup

setup(name='django-analytics',
      version='0.1',
      description='A templatetag to add google analytics code to your template.',
      author='Andy Baker',
      author_email='andy@andybak.net',
      packages=find_packages(),
      include_package_data=True,
)
