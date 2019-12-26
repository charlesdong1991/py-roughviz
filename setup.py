from setuptools import setup, find_packages

__keywords__ = ["py-roughviz", "visualization", "sketchy charts", "hand-drawn charts"]

setup(
    name="py-roughviz",
    description="A Python implementation of JavaScript Library RoughViz to create sketchy charts.",
    version="0.1.0",
    author="Kaiqi Dong",
    author_email="kaiqidong1991@gmail.com",
    licnese="MIT",
    keywords=__keywords__,
    packages=find_packages(exclude=("tests",)),
    install_requires=["jinja2", "ipython"],
    tests_require=["pytest"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ]
)
