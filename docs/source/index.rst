Documentation tutorial: rally scenarios
=============================================================


How to create yaml file with a list of scenarios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is a script `combine_files.py` that allows to combine all yaml scenarios into one file.

Example of usage:
    ``combine_files.py [-h] [--path PATH] [--filename FILENAME]``

arguments::

  -h, --help             show this help message and exit
  --path PATH            path to .yaml files, if specified then scenarios will
                         be combined only for the specific component (e.g. nova)
  --filename FILENAME    name of a new file where all scenarios will be stored

**Example 1.** Create cinder_scenarios.yaml with all scenarios from cinder/ folder:

``./combine_files.py --path cinder/ --filename cinder_scenarios.yaml``

**Example 2.** Create all_scenarios.yaml with all scenarios from all folders:

``./combine_files.py --filename all_scenarios.yaml``

Parameters
^^^^^^^^^^
Make sure to validate task_arguments.yaml file before running rally scenarios.
Parameters in task_arguments.yaml file can differ depending on deployed environment.

Glance image location
---------------------
Be aware that default value for glance image location is taken from download.cirros-cloud.net.
In case you do not have Internet connection you need to pre download needed image to machine from where
tests going to be run and update value of `glance_image_location` parameter to a path to downloaded file.

Start rally scenarios
^^^^^^^^^^^^^^^^^^^^^
``rally task start <name_of_file_with_scenarios> --task-args-file task_arguments.yaml``


.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
