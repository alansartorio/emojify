import setuptools

setuptools.setup(
    name="emojify",
    version="1.0",
    author="Alan Sartorio",
    author_email="alan42ga@hotmail.com",
    description="A command line text emojifier",
    url="https://github.com/alansartorio/emojify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={'emojipasta': ['emoji-mappings.json']},
    scripts=['emojify'],
    include_package_data=True,
    install_requires=["emoji"]
)