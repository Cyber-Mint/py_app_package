==============
py_app_package
==============
-------------------------
A python3 template for packaging your application
-------------------------

Cloning source
--------------

Get this package by:
    git clone git@github.com:Cyber-Mint/py_app_package.git

Activate the virtual environment with venv before coding, testing & packaging   
    cd py_app_package
    python3 -m venv ~/dev/py_app_package 
    source bin/activate
  

A packaging template for a package-able python application.

    >>> import app
    >>> print app.say_hello()



To install source (development):
    :~ pip3 install -e .
    
.. code-block::

    Obtaining file:///home/user/dev/py_app_package
    Requirement already satisfied: faker in ./lib/python3.8/site-packages (from py-app-package==0.1) (4.1.0)
    Requirement already satisfied: text-unidecode==1.3 in ./lib/python3.8/site-packages (from faker->py-app-package==0.1) (1.3)
    Requirement already satisfied: python-dateutil>=2.4 in ./lib/python3.8/site-packages (from faker->py-app-package==0.1) (2.8.1)
    Requirement already satisfied: six>=1.5 in ./lib/python3.8/site-packages (from python-dateutil>=2.4->faker->py-app-package==0.1) (1.15.0)
    Installing collected packages: py-app-package
      Attempting uninstall: py-app-package
        Found existing installation: py-app-package 0.1
        Uninstalling py-app-package-0.1:
          Successfully uninstalled py-app-package-0.1
      Running setup.py develop for py-app-package
    Successfully installed py-app-package
    
    
   
But, to install from wheel binary::
    :~ pip3 install wheel
    :~ pip3 install .
    

Once it is installed you can run the command line interface defnied in setup.py::
    $~ app-cli

which will yield something like::
    Hello World
    From : Kara Mclaughlin 
    
To run unit tests::
    &~ pip3 install tox
    &~ tox


.. |hr| raw:: html
Copyright |copy| 2020, Cyber-Mint (Pty) Ltd |---| all rights reserved.

.. |copy| unicode:: 0xA9 .. copyright sign
.. |---| unicode:: U+02014 .. em dash
   :trim:
   

