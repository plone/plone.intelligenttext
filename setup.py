from setuptools import setup, find_packages

version = '2.0.2'

setup(name='plone.intelligenttext',
      version=version,
      description="Provides transforms from text/x-web-intelligent to "
                  "text/html and vice versa.",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.intelligenttext',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      test_suite="plone.intelligenttext.tests.test_suite",
      install_requires=[
        'setuptools',
      ],
      )
