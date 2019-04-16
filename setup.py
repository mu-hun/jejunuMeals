from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='jejunuMeals',
    version='1.4',
    url='https://github.com/BetaF1sh/jejunuMeals',
    license='MIT',
    author='BetaF1sh',
    author_email='iam@muhun.kim',
    description='Jeju National University meal data crawler',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3',
    install_requires=['bs4', 'requests'])
