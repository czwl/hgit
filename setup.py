from io import open

from setuptools import find_packages, setup

version = "0.0.1"

readme_file = "README.md"

with open(readme_file) as f:
    readme = f.read()

REQUIRES = ["docopt", "wrapt", "gitpython"]

setup(
    name="hgit",
    version=version,
    description="A tool to manage monorepo as git branches.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Czwl Cd",
    author_email="64401603+czwl@users.noreply.github.com",
    maintainer="Czwl Cd",
    maintainer_email="64401603+czwl@users.noreply.github.com",
    url="https://github.com/czwl/hgit",
    license="Apache-2.0",
    keywords=["",],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=REQUIRES,
    tests_require=["coverage", "pytest"],
    entry_points={"console_scripts": ["hgit=hgit:cli"]},
    py_modules=["hgit"],
    packages=find_packages(),
)
