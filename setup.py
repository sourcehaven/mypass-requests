from setuptools import setup

setup(
    name='mypass-requests',
    version='1.0.0',
    description='Mypass Requests Helper',
    author='ricky :) (: skyzip',
    author_email='skyzip96@gmail.com',
    license='MIT',
    packages=['mypass_requests'],
    package_dir={'mypass_requests': 'mypass'},
    install_requires=['requests'],
    package_data={'': ['license']}
)
