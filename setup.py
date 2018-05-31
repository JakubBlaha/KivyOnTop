import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KivyOnTop",
    version="1.3",
    author="Jakub Bláha",
    author_email="jakub.blaha@example.com",
    description="Makes Kivy windows stay on top.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JakubBlaha/KivyOnTop",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)