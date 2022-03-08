from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

with open('doc/Version') as ver:
    version_ = ver.read()

setup(
    name='tocode',
    packages=find_packages(include=['tocode.*']),

    version='0.1.0',
    description='a python library that convert string to code.',
    author='Amir Shamsi',
    url='https://github.com/Amir-Shamsi/tocode',

    license='MIT',
    author_email='amirshamsi.github@gmail.com',

    github='https://github.com/Amir-Shamsi',
    linkedin='https://linkedin.com/in/amir-shamsi',

    install_requires=[],
    download_url='https://github.com/Amir-Shamsi/tocode/archive/refs/tags/'+ version_ +'.tar.gz',

    keywords=['tocode', 'convertor', 'string-to-code', 'code', 'string', 'code-generator', 'generator'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BST License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
