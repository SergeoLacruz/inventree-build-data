# -*- coding: utf-8 -*-

import setuptools
from inventree_build_data.version import PLUGIN_VERSION


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="inventree-build-data",
    version=PLUGIN_VERSION,
    author="Michael Buchmann",
    author_email="michael@buchmann.ruhr",
    description="Assign additional data to a build for external manufacturing",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="inventree build inventory ems manufacturing",
    url="https://github.com/SergeoLacruz/inventree-build-data",
    license="MIT",
    packages=setuptools.find_packages(),
    setup_requires=[
        "wheel",
        "twine",
    ],
    python_requires=">=3.6",
    entry_points={
        "inventree_plugins": [
            "BuildOrderData = inventree_build_data.build_order:BuildOrderData"
        ]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Framework :: InvenTree",
    ],
)
