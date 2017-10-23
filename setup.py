from distutils.core import setup

setup(
    name='qrnr',
    version='0.1',
    packages=['qrnr'],
    entry_points={
        'console_scripts': [
            'qrnr = qrnr.__main__:main'
        ]
    },
    install_requires=[
        'sqlalchemy'
    ],
    license='MIT License',
    description="""a tool to issue queries to databases in CLI using sqlalchemy."""
)
