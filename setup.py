from setuptools import setup, find_packages

setup(
    # Application name:
    name="latexfixer",

    # Version number (initial):
    version="0.2.0",

    # Application author details:
    author="Tom McLean",
    author_email="thomasowenmclean@gmail.com",

    # Packages
    packages=["latexfixer"],

    # Include additional files into the package
    include_package_data=True,


    # Details
    url="https://github.com/thomasowenmclean/latexfixer",

    #
    license="GPL",
    description="Transform unicode text into typographically more correct LaTeX compatible unicode.",

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
		'Topic :: Text Processing :: Markup :: LaTeX',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

    keywords='latex',

    # long_description=open("README.txt").read(),
    # Dependent packages (distributions)
    install_requires=['ftfy'],
)