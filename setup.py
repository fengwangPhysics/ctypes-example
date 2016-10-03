import subprocess
from distutils.core import setup

subprocess.call(['make', '-C', 'src'])

setup(name='TestModule',
  version='1.0',
  description='Python bindings of C lib',
  author='Feng Wang',

  packages = ['TestModule'],
  package_dir = {'TestModule': 'TestModule'},
  package_data = {
      'TestModule': ['lib/libtest.so'],
  },
)
