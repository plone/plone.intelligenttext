from setuptools import setup, find_packages
import sys, os

version = '1.0.2'

setup(name='plone.intelligenttext',
      version=version,
      description="Provides transforms from text/x-web-intelligent to text/html and vice versa.",
      long_description="""\
""",
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Kai Diefenbach',
      author_email='kai.diefenbach@iqpp.de',
      url='http://svn.plone.org/svn/plone/plone.intelligenttext',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
      ],
      )
