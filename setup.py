from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Dragon",
    version="1.0.0",
    author="Anjana",
    author_email="kamleanjana@gmail.com",
    description="A Python package for simple calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johndoe/PyWeather",
    packages=find_packages(),
    package_dir={"": "pyweather"},
    install_requires=[
      
    ],
    extras_require={
       
    },
    entry_points={
       
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)