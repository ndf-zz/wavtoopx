import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    python_requires='>=3',
    install_requires=[
        'soundfile',
    ],
    name="wavtoopx",
    version="1.0.0",
    author="Nathan Fraser",
    author_email="ndf@metarace.com.au",
    description="Alternate FV-1 Assembler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ndf-zz/wavtoopx",
    entry_points={
        'console_scripts': [
            'asfv1=wavtoopx:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
	'Environment :: Console',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
    ],
    py_modules=['wavtoopx',],
)

