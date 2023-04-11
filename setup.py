from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='fp-data-toolbox',
    version='0.1.55',
    author='Fred Pires',
    author_email='fredapires@gmail.com',
    description='personal toolbox for data science',
    long_description='file: README.md',
    long_description_content_type="text/markdown",
    url='https://github.com/fredapires/fp_data_toolbox',
    packages=find_packages(),
    install_requires=[
        'build',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'missingno',
        'pandas-profiling',
        'ydata-profiling',
        'dataprep',
        'jupyter-helpers',
        'win10toast',
        'jaro_winkler',
        'openpyxl',
        'pyarrow',
        'pyodbc',
        'pyautogui',
        'faker',
        'pytest'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
