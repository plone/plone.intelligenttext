from setuptools import setup, find_packages

version = '2.2'

setup(
    name='plone.intelligenttext',
    version=version,
    description="Provides transforms from text/x-web-intelligent to "
                "text/html and vice versa.",
    long_description=(
        open("README.rst").read() +
        "\n" +
        open("CHANGES.rst").read()
    ),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
      ],
    keywords='transform intelligenttext',
    author='Plone Foundation',
    author_email='plone-developers@lists.sourceforge.net',
    url='https://pypi.python.org/pypi/plone.intelligenttext',
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
