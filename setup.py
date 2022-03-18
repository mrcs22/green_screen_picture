from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="green_screen_picture",
    version="0.0.1",
    author="mrcs22",
    author_email="marcusmoraes2010@hotmail.com",
    description="simple package to add background images to green screen",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrcs22/green_screen_picture"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
