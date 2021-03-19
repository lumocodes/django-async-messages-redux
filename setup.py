#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-async-messages-redux',
      version='0.4.1',
      url='https://github.com/maurizi/django-async-messages',
      author='Michael Maurizi',
      author_email='michael@maurizi.org',
      description="Send asynchronous messages to users (eg from offline scripts). Useful for integration with Celery.",
      long_description=open('README.rst').read(),
      packages=find_packages(exclude=['tests']),
      install_requires=['django>=1.11'],
      classifiers=[
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: MIT License",
            "Environment :: Web Environment",
            "Development Status :: 5 - Production/Stable",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Framework :: Django",
            "Framework :: Django :: 2.2"
            "Framework :: Django :: 3.0"
            "Framework :: Django :: 3.1"
      ],
      )
