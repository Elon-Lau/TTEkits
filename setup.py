from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="TTEkits",
    version='0.0.6',
    description="This is a travel time estimation Python Library!",
    py_modules=["TTE"],
    package_dir={'': 'TTEkits'},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    extras_require = {"dev":[],},
    url="https://github.com/Elon-Lau/TTEkits",
    author="Elon Lau",
    author_email="weitinglau1999@gmail.com",
    setup_requires=['wheel']
)