from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "hello-app-flask"
default_task = ["analyze", "publish"]


@init
def set_properties(project):
    
    project.set_property("flake8_exclude_patterns", "setup.py,/target,htmlcov,devenv")
    project.set_property("dir_source_main_python", "src/main/python/helloapp")
    project.set_property("dir_source_unittest_python", "src/unittest/python/helloapp")
    project.depends_on('flask')
    project.set_property('coverage_break_build', True)
    project.set_property('teamcity_output', True)
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_verbose_output', True)
    
