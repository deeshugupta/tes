from setuptools import setup, find_packages

setup(
    name='tes',
    version='1.0',
    packages=['commands'],
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
        },
    author="Deepanshu Gupta",
    author_email="gupta.deeshu@gmail.com",
    description="Tool for Elasticsearch",
    keywords="tes elasticsearch Elasticsearch"
)
