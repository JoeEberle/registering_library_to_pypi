from setuptools import setup

setup(
    name="registering_library",
    version="josepheberle@outlook.com",
    py_modules=['pathlib'],
    author="library of functions to register libraries to PyPi",
    author_email="josepheberle@outlook.com",
    description="0.1.0",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JoeEberle/registering_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
