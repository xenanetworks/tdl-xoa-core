import setuptools


def main() -> None:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="xena-rfc-core",
        description="Xena Python RFC framework for Xena test suite execution, integration, and development.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Leonard Yu",
        author_email="leonard.yu@teledyne.com",
        maintainer="Teledyne LeCroy Xena",
        maintainer_email="support@xenanetworks.com",
        url="https://github.com/xenanetworks/xena-python-rfc-core",
        packages=setuptools.find_packages(),
        license='Apache 2.0',
        install_requires=["xena-driver", "pydantic==1.10.2", "semver", "oyaml",],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Application Frameworks",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
        ],
        python_requires=">=3.8.9",
    )


if __name__ == '__main__':
    main()
