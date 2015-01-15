from spack import *

class PyNose(Package):
    """nose extends the test loading and running features of unittest, making it easier to write, find and run tests."""
    homepage = "https://pypi.python.org/pypi/nose"
    url      = "https://pypi.python.org/packages/source/n/nose/nose-1.3.4.tar.gz"

    version('1.3.4', '6ed7169887580ddc9a8e16048d38274d')

    extends('python')

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)
