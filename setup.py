from setuptools import setup

required_libraries = ["numpy", "jupyter", "pandas", "matplotlib", "seaborn"]


setup(
    name="perfect",
    version="0.0.1",
    description="a little investigation into the properties of integer factorization and perfect numbers",
    author="jattenberg",
    author_email="josh@attenberg.org",
    url="https://github.com/jattenberg/perfect",
    license="MIT",
    packages=['perfect'],
    zip_safe=False,
    install_requires=required_libraries,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.6',
  ],
)
