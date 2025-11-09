from setuptools import setup, find_packages

setup(
    name='trajectory_fitting',
    version='1.0.0',
    author='Abhishek Jain',
    author_email='your_email@example.com',
    description='Parametric trajectory fitting with latent time estimation using alternating optimization.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.26.0',
        'pandas>=2.0.0',
        'matplotlib>=3.8.0',
        'scipy>=1.11.0'
    ],
    python_requires='>=3.8',
)
