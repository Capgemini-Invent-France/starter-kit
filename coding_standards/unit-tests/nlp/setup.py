from setuptools import find_packages, setup

setup(
    name="nlp",
    version="0.0.1",
    description="",
    python_requires=">=3.7",
    author="thibaultVenet",
    author_email="thibault.venet@capgemini.com",
    packages=find_packages(),
    package_dir={"": "."},
    package_data={"nlp": ["*.md"]},
)
