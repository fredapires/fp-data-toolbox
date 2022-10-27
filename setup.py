
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fp_data_toolbox',
    version='0.1.18',  # MUST increment this whenever we would like to make changes
    author='Fred Pires',
    author_email='fredapires@gmail.com',
    description='Personal data toolbox for Fred Pires',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fredapires/fp_data_toolbox',
    project_urls={
        "Bug Tracker": "https://github.com/fredapires/fp_data_toolbox/issues"
    },
    license='MIT',
    packages=[
        'fp_data_toolbox'
    ],
    ###
    # Including data packages
    ###
    # exclude_package_data={'fp_data_toolbox': ['data/*.src']},
    include_package_data=True,
    # package_dir={'fp_data_toolbox'},
    # packages=setuptools.find_packages(where='src'),
    ###
    install_requires=[
        'pandas',
        'numpy',
        'seaborn',
        'pandas_profiling',
        'popmon',
        'dataprep',
        'dtale'
    ],
    ###
)
