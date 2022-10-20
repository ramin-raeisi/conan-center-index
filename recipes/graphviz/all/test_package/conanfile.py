from conan import ConanFile
from conan.tools.build import can_run


# It will become the standard on Conan 2.x
class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "VirtualBuildEnv"
    test_type = "explicit"

    def build_requirements(self):
        return True
        # self.tools_requires(self.tested_reference_str)

    def test(self):
        if can_run(self):
            pass
            # self.run checks the command exit code
            # the tool must be available on PATH
            # self.run("tool --version")
