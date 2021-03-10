from setuptools import setup

setup(
    name="energy-estimator",
    version="1.0",
    description="Energy Estimator",
    author="Diego Gonzalez",
    py_modules=["src"],
    install_requires=["click"],
    entry_points={"console_scripts": ["energy-estimator = src.cli:estimator"]},
)
