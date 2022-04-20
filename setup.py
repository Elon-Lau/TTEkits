# import pathlib
# from setuptools import setup
#
# # The directory containing this file
# HERE = pathlib.Path(__file__).parent
#
# # The text of the 'README file
# README = (HERE / "README.md").read_text()
#
# # This call the setup() does all the work
# setup(
#     name="TTEkits",
#     version="1.0.0",
#     description="It can estimate travel time in the city.",
#     long_description=README,
#     long_description_content_type="text/markdown",
#     url="https://github.com/Elon-Lau/TTEkits",
#     author="Elon Lau",
#     author_email="weitinglau1999@gmail.com",
#     # license=="MIT",
#     # classifiers=[
#     #     "License :: OSI Approved :: MIT License",
#     #     "Programming Language :: Python :: 3.6",
#     #     "Programming Language :: Python :: 3.7",
#     #     "Programming Language :: Python :: 3.8",
#     # ],
#     packages=["ttekits"],
#     include_package_data=True,
#     install_requires=[],
#     entry_points={
#         "console_scripts": [
#             "ttekits=ttekits.__main__:main",
#         ]
#     },
# )


from setuptools import setup, find_packages

GFICLEE_VERSION = '2020.8.4.6'

setup(
    name="TTEkits",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["cfastproject = ttekits=ttekits.__main__:main"]
    },
    install_requires=[
        "pandas"
    ],
    url='https://github.com/Elon-Lau/TTEkits',
    license='MIT',
    author="Elon Lau",
    author_email="weitinglau1999@gmail.com",
)
