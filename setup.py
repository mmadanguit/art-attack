import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="art-attack-pkg-olin-college",
    version="0.0.1",
    author="Anna Commers, Elisa Dhanger, Jennifer Lee, Marion Madanguit, Luke Nonas-Hunter",
    author_email="lhunter@olin.edu",
    description="A package to communicate with an Arduino to control multiple servos using computer vision and the PCA9685 chip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmadanguit/art-attack",
    project_urls={
        "Bug Tracker": "https://github.com/mmadanguit/art-attack/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "python-src"},
    packages=setuptools.find_packages(where="python-src"),
    python_requires=">=3.6",
)
