from setuptools import setup
from setuptools_rust import Binding, RustExtension

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jai",
    version="0.1.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JakeRoggenbuck/jai",
    rust_extensions=[
        RustExtension("jai", binding=Binding.PyO3),
    ],
    packages=["jai"],
    zip_safe=False,
)
