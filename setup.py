from setuptools import setup, find_packages

setup(
    name='tes',
    version='1.0',
    py_modules=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'Elasticsearch', 'Texttable'
    ],
    entry_points={
        'console_scripts': [
        'tes=main:cli',
        'tes:cat=commands.cat_api:cat',
        'tes:cluster=commands.cluster_api:cluster',
        'tes:node=commands.node_api:node'
        ]
        }
)
