from setuptools import find_packages, setup

with open("README.md") as fp:
    long_description = fp.read()


setup(
    name="markdown-slides",
    version="0.1.6",
    packages=find_packages(),
    install_requires=[
        "flask",
        "jsonschema",
        "python-frontmatter",
        "pyyaml",
    ],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "slides = slides.__main__:__main__",
        ],
    },
)
