from setuptools import setup

setup(name='py_app_package',
      version='0.1.0',
      description='A packaging template application ',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Operating System :: POSIX :: Linux',
          'Topic :: Software Development',
      ],
      keywords='python package template',
      url='https://github.com/Cyber-Mint/py_app_package',
      author='Bank-Builder',
      author_email='bank-builder@cyber-mint.com',
      license='MIT',
      packages=['app'],
      install_requires=[
          'faker',
      ],
      include_package_data=True,
      entry_points={
          'console_scripts': ['app-cli=app.app_cli:main'],
      },
      zip_safe=False)
