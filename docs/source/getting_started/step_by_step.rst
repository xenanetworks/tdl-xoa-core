Step-by-Step Guide
===================

This section provides a step-by-step guide on how to use XOA Core to run XOA test suites. 


Create Project Folder
---------------------

To run XOA test suites, you need a folder to place the test suite plugins, the test configuration files, and yous Python script to control the tests.

Let's create a folder called ``/my_xoa_project``

.. code-block::
    :caption: Create the project folder

    /my_xoa_project
        |


Install XOA Core
-----------------------------

After creating the folder, you can either choose to :ref:`install XOA Core in a Python virtual environment <install_core_venv>` or :ref:`install in your global namespace <install_core_global>` .

If you have already installed XOA Core in your system, either to your global namespace or in a virtual environment, you can skip this step.


Place Test Suite Plugins
------------------------

Depending on what XOA test you want to run, place the corresponding XOA test suite plugins and the test configuration files in ``/my_xoa_project``.

Your project folder will look like this afterwards.

.. code-block::
    :caption: Copy test suite plugins into the project folder

    /my_xoa_project
        |
        |- /test_suites
            |- /plugin2544
            |- /plugin2889
            |- /plugin3918


Run Tests from XOA Test Suite Configurations
--------------------------------------------------------

.. important::

    If you run **Xena GUI test suite configuration files** (``.x2544`` for :term:`Xena2544`, ``.x2889`` for :term:`Xena2889`, ``.x3918`` for :term:`Xena3918`), go to `Run Tests from Xena Test Suite GUI Configurations`_.

Copy your XOA test configuration ``.json`` files into ``/my_xoa_project`` for easy access. Then create a ``main.py`` file inside the folder ``/my_xoa_project``.

.. code-block::
    :caption: Copy XOA test configs and create main.py

    /my_xoa_project
        |
        |- main.py
        |- new_2544_config.json
        |- new_2889_config.json
        |- new_3918_config.json
        |- /test_suites
            |- /plugin2544
            |- /plugin2889
            |- /plugin3918

This ``main.py`` controls the test workflow, i.e. load the configuration files, start tests, receive test results, and stop tests. The example below demonstrates a basic flow for you to run XOA tests.

.. literalinclude:: ../code_example/running_xoa_config.py
    :language: python


Then simply run ``main.py``:

.. code-block:: console

    [my_xoa_project]$ python3 main.py


Run Tests from Xena Test Suite GUI Configurations
-------------------------------------------------

If you want to run your test suite GUI configuration files, you should install ``xena-rfc-converter``  to convert Valkyrie test suite configurations into XOA test suite configurations, as illustrated below.

.. image:: ../_static/xoa_converter_illustration.png
    :width: 600
    :alt: Illustration of GUI-to-Python conversion flow


.. seealso::
    
    Read more about installing `XOA Converter <https://docs.xenanetworks.com/projects/xena-python-rfc-converter>`_


Copy your GUI test configurations into ``/my_xoa_project`` for easy access. Then create a ``main.py`` file inside the folder ``/my_xoa_project``.

.. code-block::
    :caption: Copy TUI test configs and create main.py

    /my_xoa_project
        |
        |- main.py
        |- old_2544_config.v2544
        |- old_2889_config.v2889
        |- old_3918_config.v3918
        |- /test_suites
            |- /plugin2544
            |- /plugin2889
            |- /plugin3918

This ``main.py`` controls the test workflow, i.e. convert the GUI configs into XOA configs, load the configuration files, start tests, receive test results, and stop tests. The example below demonstrates a basic flow for you to run the GUI tests.

.. literalinclude:: ../code_example/running_valkyrie_config.py
    :language: python


Receive Test Result Data
------------------------

XOA Core sends test result data (in JSON format) to your code as shown in the example below. It is up to you to decide how to process it, either parse it and display in your console, or store them into a file.

.. code-block:: python
    :caption: Receive test result data

    async for stats_data in ctrl.listen_changes(execution_id, _filter={types.EMsgType.STATISTICS}):
        print(stats_data)

.. seealso::

    Read about :doc:`../understand_xoa_core/test_result_types`

