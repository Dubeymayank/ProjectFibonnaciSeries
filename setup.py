import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="fibonnaciSeries",
    version="0.0.1",
    author="Mayank Dubey",
    author_email="dbmayank@gmail.com",
    packages=["fibonnaciSeries"],
    description="A sample test package to generate fibonnaci Series",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)