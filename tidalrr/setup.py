from setuptools import setup, find_packages

setup(
    name='tidalrr',
    version='2023.10.23.1',
    license="Apache2",
    description="Tidalrr",

    author='lejacobroy',
    author_email="lejacobroy@gmail.com",

    packages=find_packages(),
    include_package_data=False,
    platforms="any",
    install_requires=["aigpy>=2022.7.8.1", 
                      "requests>=2.22.0",
                      "pycryptodome", 
                      "pydub", 
                      "prettytable",
                      "lxml"],
    entry_points={'console_scripts': ['tidalrr = tidalrr:main', ]}
)
