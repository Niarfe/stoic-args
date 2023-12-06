import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stoicargs",
    version="0.0.0",
    author="Efrain Olivares",
    author_email="efrain.olivares@gmail.com",
    description="Ultra lightweight arg parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Niarfe/stoicargs",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux, Mac",
    ),
)
