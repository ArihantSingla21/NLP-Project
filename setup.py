from setuptools import find_packages,setup
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description=f.read()
    
__version__ ="0.0.0"
REPO_NAME= "NLP-Project"
AUTHOR="ArihantSingla21"
SRC_REPO="textsummarizer"
AUTHOR_EMAIL="arihantsingla21@gmail.com"  

setup(
    name=REPO_NAME,
    version=__version__,
    author="ArihantSingla21",
    author_email="arihantsingla21@gmail.com",
    description= "python packages for text summarization",
    long_description=long_description,
    long_description_content="text/markdown",   
    url=f"http://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":"http://github.com/{AUTHOR}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=find_packages(where="src")
)