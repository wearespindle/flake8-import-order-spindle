from setuptools import find_packages, setup


__title__ = 'flake8-import-order-spindle'
__author__ = 'Devhouse Spindle'
__email__ = 'opensource@wearespindle.com'
__version__ = '0.1'
__copyright__ = 'Copyright (C) 2017 Devhouse Spindle'
__license__ = 'MIT License'


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = ''

install_requires = [
    'flake8-import-order',
]

setup(
    name=__title__,
    version=__version__,
    description='Spindle\'s custom import order plugin',
    long_description=long_description,
    url='https://github.com/wearespindle/flake8-import-order-spindle',
    author=__author__,
    author_email=__email__,
    license=__license__,
    install_requires=install_requires,
    entry_points={
        'flake8_import_order.styles': [
            'spindle = flake8_import_order_spindle:SpindleOrder',
        ]
    },

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    keyword='flake8 import imports ordering',
    classifiers=[
        # Status.
        'Development Status :: 3 - Alpha',

        # Audience.
        'Intended Audience :: Developers',

        # License.
        'License :: OSI Approved :: MIT License',

        # Programming languages.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
