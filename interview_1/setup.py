from setuptools import setup, find_packages

setup(
    name="innovyze-interview-challenge-1",
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"}
)
