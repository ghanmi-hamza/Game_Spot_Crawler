import setuptools

version = "1.0.0"


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="GameSpot_Crawler",
    version=version,
    author="Hamza Ghanmi",
    author_email="hamza.ghanmi56@gmail.com",
    license="MIT",
    description="A bot which scrapes everything about a Gamespot user's profile",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=["selenium==3.141.0","webdriver_manager"],

)
