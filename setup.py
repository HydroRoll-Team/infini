from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='HydroRollCore',
    version='0.1.1',
    author='简律纯',
    author_email='i@jyunko.cn',
    description='Core of HydroRoll.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HydoRoll-Team/HydroRollCore',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=['tkinter'],
    entry_points={
        'console_scripts': [
            'HydroRoll = HydroRoll.__init__:main'
        ]
    },
)
