from setuptools import setup, find_packages

__keywords__ = ["py-roughviz", "visualization", "sketchy charts", "hand-drawn charts"]

setup(
    name="py-roughviz",
    description="The Python implementation of JavaScript Library RoughViz to create sketchy charts.",
    version="0.2.0",
    author="Kaiqi Dong",
    author_email="kaiqidong1991@gmail.com",
    licnese="MIT License",
    keywords=__keywords__,
    packages=find_packages(exclude=["test*"]),
    install_requires=["jinja2", "ipython"],
    download_url="https://github.com/charlesdong1991/py-roughviz/archive/v0.2.0.tar.gz",
    tests_require=["pytest"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ],
)
