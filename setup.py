from setuptools import setup

setup(
    name="self_sensored",
    version="0.0.1",
    description="A Python SDK for the Self-Sensored REST API.",
    url="https://github.com/Ladvien/self_sensored_python_sdk.git",
    author="C. Thomas Brittain",
    author_email="honeysucklehardware@gmail.com",
    packages=[
        "self_sensored"
    ],
    zip_safe=False,
    install_requires=["pandas"],
)
