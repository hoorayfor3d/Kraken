from kraken.tests import arm_component
from kraken.tests import arm_rig

from kraken.tests.arm_rig import ArmRig

from kraken.plugins.si_plugin import builder
reload(builder)

from kraken.plugins.si_plugin.builder import Builder

myArm = ArmRig("myArm")

siBuilder = Builder()
siBuilder.build(myArm)