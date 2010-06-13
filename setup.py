from setuptools import setup, find_packages

version = '2.0'

setup(name='plone.intelligenttext',
      version=version,
      description="Provides transforms from text/x-web-intelligent to text/html and vice versa.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Kai Diefenbach',
      author_email='kai.diefenbach@iqpp.de',
      url='http://pypi.python.org/pypi/plone.intelligenttext',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
      ],
      )
