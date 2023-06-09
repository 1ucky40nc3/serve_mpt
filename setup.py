from setuptools import find_packages, setup

setup(
    name="serve_mpt",
    version="0.0.1",  # expected format is one of x.y.z.dev0, or x.y.z.rc1 or x.y.z (no to dashes, yes to dots)
    author="Louis Wendler",
    author_email="louisnwendler@gmail.com",
    description="Quantize and serve the MPT-7B models from Mosaic ML, Inc.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="Apache 2.0 License",
    url="https://github.com/1ucky40nc3/serve_mpt",
    package_dir={"": "src"},
    packages=find_packages("src"),
)