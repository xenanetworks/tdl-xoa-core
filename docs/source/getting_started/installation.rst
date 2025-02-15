Installing Xena Python RFC Core
===============================

Xena Python RFC Core is available to install via the `Python Package Index <https://pypi.org/>`_. You can also install from the source file.

Prerequisites
-------------

Before installing Xena Python RFC Core, please make sure your environment has installed:
    
* `Python`_
* `pip`_

Python
^^^^^^

Xena Python RFC Core requires that you `install Python <https://realpython.com/installing-python/>`_  on your system.

.. note:: 

    Xena Python RFC Core requires Python >= 3.8.

``pip``
^^^^^^^^

Make sure ``pip`` is installed on your system. ``pip`` is the `package installer for Python <https://packaging.python.org/guides/tool-recommendations/>`_ . You can use it to install packages from the `Python Package Index <https://pypi.org/>`_  and other indexes.

Usually, ``pip`` is automatically installed if you are:

* working in a `virtual Python environment <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments>`_ (`virtualenv <https://virtualenv.pypa.io/en/latest/#>`_ or `venv <https://docs.python.org/3/library/venv.html>`_ ). It is not necessary to use ``sudo pip`` inside a virtual Python environment.
* using Python downloaded from `python.org <https://www.python.org/>`_ 

If you don't have ``pip`` installed, you can:

* Download the script, from https://bootstrap.pypa.io/get-pip.py.
* Open a terminal/command prompt, ``cd`` to the folder containing the ``get-pip.py`` file and run:

.. code-block:: console

    $ python3 get-pip.py

.. seealso::

    Read more details about this script in `pypa/get-pip <https://github.com/pypa/get-pip>`_.

    Read more about installation of ``pip`` in `pip installation <https://pip.pypa.io/en/stable/installation/>`_.


Installing From PyPI Using ``pip``
----------------------------------

``pip`` is the recommended installer for Xena Python RFC Core. The most common usage of ``pip`` is to install from the `Python Package Index <https://pypi.org/>`_ using `Requirement Specifiers <https://pip.pypa.io/en/stable/cli/pip_install/#requirement-specifiers>`_.

.. note::
    
    If you install Xena Python RFC Core using ``pip install xena-rfc-core``, XOA Python API (PyPI package name `xoa_driver <https://pypi.org/project/xoa-python-api/>`_) will be automatically installed.


.. _install_core_global:

Install to Global Namespace
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ pip install xena-rfc-core            # latest version
    $ pip install xena-rfc-core==1.0.7     # specific version
    $ pip install xena-rfc-core>=1.0.7     # minimum version


.. _install_core_venv:

Install in Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install Xena Python RFC Core in a virtual environment, so it does not pollute your global namespace. 

For example, your project folder is called ``/my_xoa_project``.

.. code-block:: console

    [my_xoa_project]$ python3 -m venv ./env
    [my_xoa_project]$ source ./env/bin/activate

    (env) [my_xoa_project]$ pip install xena-rfc-core         # latest version
    (env) [my_xoa_project]$ pip install xena-rfc-core==1.0.7  # specific version
    (env) [my_xoa_project]$ pip install xena-rfc-core>=1.0.7 # minimum version

Afterwards, your project folder will be:

.. code-block::
    :caption: After creating Python virtual environment

    /my_xoa_project
        |
        |- env

.. seealso::

    * `Virtual Python environment <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments>`_
    * `virtualenv <https://virtualenv.pypa.io/en/latest/#>`_
    * `venv <https://docs.python.org/3/library/venv.html>`_


Upgrading From PyPI Using ``pip``
---------------------------------

To upgrade Xena Python RFC Core package from PyPI:


.. code-block:: console

    $ pip install xena-rfc-core --upgrade


.. note::
    
    If you upgrade Xena Python RFC Core using ``pip install --upgrade xena-rfc-core``, Xena Python API (PyPI package name `xena-driver <https://pypi.org/project/xena-driver/>`_) will be automatically upgraded.


Installing Manually From Source
-------------------------------

If for some reason you need to install Xena Python RFC Core manually from source, the steps are:

**Step 1**, make sure Python packages `wheel <https://wheel.readthedocs.io/en/stable/>`_ and  `setuptools <https://setuptools.pypa.io/en/latest/index.html>`_ are installed on your system. Install ``wheel`` and ``setuptools`` using ``pip``:

.. code-block:: console

    $ pip install wheel setuptools

**Step 2**, download the Xena Python RFC Core source distribution from `Xena Python RFC Core Releases <https://github.com/xenanetworks/open-automation-core/releases>`_. Unzip the archive and run the ``setup.py`` script to install the package:

.. code-block:: console

    [xena_rfc_core]$ python3 setup.py install


**Step 3**, if you want to distribute, you can build ``.whl`` file for distribution from the source:

.. code-block:: console

    [xena_rfc_core]$ python3 setup.py bdist_wheel

.. important::

    If you install Xena Python RFC Core from the source code, you need to install Xena Python API (PyPI package name `xoa_driver <https://pypi.org/project/xena-driver/>`_) separately. This is because Xena Python API is treated as a 3rd-party dependency of Xena Python RFC Core. You can go to `Xena Python API <https://github.com/xenanetworks/xena-python-api>`_ repository to learn how to install it.


Uninstall and Remove Unused Dependencies
----------------------------------------

``pip uninstall xena-rfc-core`` can uninstall the package itself but not its dependencies. Leaving the package's dependencies in your environment can later create conflicting dependencies problem.

We recommend install and use the `pip-autoremove <https://github.com/invl/pip-autoremove>`_ utility to remove a package plus unused dependencies.

.. code-block:: console

    $ pip install pip-autoremove
    $ pip-autoremove xena-rfc-core -y

.. seealso::

    See the `pip uninstall <https://pip.pypa.io/en/stable/cli/pip_uninstall/#pip-uninstall>`_ reference.

    See `pip-autoremove <https://github.com/invl/pip-autoremove>`_ usage.



