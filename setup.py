from setuptools import setup, find_packages

# Package meta-data.
NAME = "singlish-translator"
DESCRIPTION = "Singlish to Sinhala conversion library"
URL = "https://github.com/SupunGurusinghe/SinglishProcessor.git"
EMAIL = "supunsameeran@gmail.com"
AUTHOR = "Supun Gurusinghe"
REQUIRES_PYTHON = ">=3.7.0"

# setup function
setup(
    include_package_data=True,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    name=NAME,
    version='0.1.0 ',
    packages=find_packages(include=['tab_cleaner', 'tab_cleaner.*']),
    python_requires=REQUIRES_PYTHON
)
