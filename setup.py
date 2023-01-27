from setuptools import find_packages, setup


setup(
    name="slides",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "python-frontmatter",
    ],
    include_package_data=True,
)
