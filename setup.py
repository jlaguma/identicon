import identicon
import sys
from setuptools import setup

if sys.version_info.major < 3 or (sys.version_info.minor < 6
                                  and sys.version_info.major == 3):
    sys.exit('Python < 3.6 is unsupported.')

with open('README.md', encoding='utf8') as file:
    long_description = file.read()

setup(
    name='identicon',
    version=identicon.__version__,
    author=identicon.__author__,
    author_email='james@taran.biz',
    url='https://github.com/jlaguma/identicon',
    packages=['identicon'],
    package_data={},
    install_requires=['click', 'pillow'],
    license='GNU GPLv3',
    description='Identicon Generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={'console_scripts': ['identicon = identicon.__main__:main']},
)
