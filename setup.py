from setuptools import setup, find_packages


setup(
    name='t2speech',
    version='0.1',
    license='MIT',
    author="Tiam Samzadeh",
    author_email='tiamsamzadeh@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Tiamiscool/t2speech/tree/main',
    keywords='t2speech',
    install_requires=[
          'gtts',
      ],

)