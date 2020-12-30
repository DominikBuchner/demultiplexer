import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demultiplexer",
    version="1.0.2",
    author="Dominik Buchner",
    author_email="dominik.buchner524@googlemail.com",
    description="python script to demultiplex illumina reads tagged with the leeselab tagging scheme",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DominikBuchner/demultiplexer",
    packages=setuptools.find_packages(),
    license = 'MIT',
    install_requires = ['PySimpleGUI >= 4.19.0',
                        'openpyxl >= 3.0.3',
                        'psutil >= 5.7.3',
                        'biopython >= 1.78',
                        'joblib >= 0.16.0',
                        ],
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points = {
        "console_scripts" : [
            "demultiplexer = demultiplexer.__main__:main",
        ]
    },
)
