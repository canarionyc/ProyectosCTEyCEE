from setuptools import setup, find_packages

setup(
    name="pycte",
    version="0.1.0",
    packages=find_packages(),
    description="Routines for implementing the Codigo Tecnico de la Edification (CTE) for Building Energy Efficiency",
    author="canarionyc",
    author_email="your.email@example.com",  # Update with your email
    url="https://github.com/canarionyc/pyCTE",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Update with your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add your dependencies here, e.g.:
        # "numpy>=1.18.0",
        # "pandas>=1.0.0",
    ],
)