from setuptools import setup

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
    url="https://github.com/deeshugupta/tes",
    download_url="https://github.com/deeshugupta/tes/archive/v1.0.tar.gz",
    keywords="tes elasticsearch Elasticsearch"
)
