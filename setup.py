import setuptools
 
with open('README.md','r') as f:
    description = f.read()

setuptools.setup(
    name='text summarizer',
    version='0.0.1',
    author='Jake',
    author_email='awaistahseenaccoun@gmail.com',
    url="https://github.com/awaistahseen009/text-summarizer-project",
    project_urls={
        "Bug Tracker":"https://github.com/awaistahseen009/text-summarizer-project"
    },
    package_dir={"":"src"},
    description='A text summarization tool',
    long_description=description,
    packages=setuptools.find_packages(where="src")
)
