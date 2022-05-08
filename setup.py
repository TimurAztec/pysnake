from setuptools import find_packages, setup
import setuptools

setup(
    name="pysnake",
    version='0.0.1',
    description="Simple snake game",
    author='TimurAztec',
    author_email='timotiaztec@gmail.com',
    entry_points = {
        'console_scripts': [
            'pysnake = main:main'
        ]
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "keyboard>=0.13.5",
        "Pillow>=9.1.0",
        "playsound==1.2.2"
    ]
)