from setuptools import setup, find_packages

setup(
    name='jejunuMeals',
    version='1.0.2',
    url='https://github.com/BetaF1sh/jejunuMeals',
    license='GPL v3.0',
    author='BetaF1sh',
    author_email='iam@muhun.kim',
    description='Jeju National University meal data crawler',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=['bs4', 'requests'])
