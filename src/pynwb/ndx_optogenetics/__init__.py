import os
from pynwb import load_namespaces, get_class

# Set path of the namespace.yaml file to the expected install location
ndx_optogenetics_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    'ndx-optogenetics.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_optogenetics_specpath):
    ndx_optogenetics_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        'ndx-optogenetics.namespace.yaml'
    ))

# Load the namespace
load_namespaces(ndx_optogenetics_specpath)

# TODO: import your classes here or define your class using get_class to make
# them accessible at the package level
OpticFiberImplant = get_class('OpticFiberImplant', 'ndx-optogenetics')
OrthogonalStereotacticTarget = get_class('OrthogonalStereotacticTarget', 'ndx-optogenetics')
