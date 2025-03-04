import setuptools


def main() -> None:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="tdl-xoa-core",
        description="XOA framework for Xena test suite execution, integration, and development.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Leonard Yu",
        author_email="leonard.yu@teledyne.com",
        maintainer="Teledyne LeCroy Xena",
        maintainer_email="support@xenanetworks.com",
        url="https://github.com/xenanetworks/tdl-xoa-core",
        packages=setuptools.find_packages(),
        license='Apache 2.0',
        install_requires=["tdl-xoa-driver>=1.1", "pydantic>=2.0", "semver", "oyaml",],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Application Frameworks",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
        ],
        python_requires=">=3.9",
    )


if __name__ == '__main__':
    main()
