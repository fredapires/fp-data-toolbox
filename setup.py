
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fp_data_toolbox',
    version='0.0.1',
    author='Fred Pires',
    author_email='fredapires@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fredapires/fp_data_toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/fredapires/fp_data_toolbox/issues"
    },
    license='MIT',
    packages=['toolbox'],
    install_requires=[
        'pandas',
        'numpy',
        'seaborn'
    ],
)