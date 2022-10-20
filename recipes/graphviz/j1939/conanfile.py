from conans import ConanFile, tools
from conans import __version__ as conan_version
from conans.model.version import Version
import os
import subprocess


class PlantUML(ConanFile):
    name = "J1939"
    version = "1.1.0"
    description = "canbus framework"
    author = "Satyam Satyam.LaxmiSharanLal@in.bosch.com"
    url = "https://github.com/ramin-raeisi/J1939-release/releases/download/1.1.0.v2/J1939Static.tar.xz"
    settings = "os", "arch"
    short_paths = True
    apply_env = False

    def build(self):
        tools.get(self.url)

    def package(self):
        self.copy("*", "", "", True, True)

    def package_info(self):
        # folders not used for pre-built binaries
        self.cpp_info.frameworkdirs = []
        self.cpp_info.resdirs = []
        self.cpp_info.includedirs = []

        bin_folder = os.path.join(self.package_folder, "bin")
        new_var = os.path.join(self.package_folder, "lib")
        self.output.info("-----package_folder {} ---{}".format(self.package_folder, new_var))
        self.cpp_info.builddirs = [os.path.join(self.package_folder, "lib/cmake")]
        self.output.info("self.cpp_info.builddirs : {}".format(self.cpp_info.builddirs))
        self.cpp_info.libdirs = [os.path.join(self.package_folder, "lib")]
        self.cpp_info.includedirs = [os.path.join(self.package_folder, "include")]
        # In case need to find packaged tools when building a package
        self.buildenv_info.append("PATH", bin_folder)
        # In case need to find packaged tools at runtime
        self.runenv_info.append("PATH", bin_folder)
        # TODO: Legacy, to be removed on Conan 2.0

        self.env_info.PATH.append(bin_folder)
        # self.cpp_info.libs = self.collect_libs()
        # self.env_info.LD_LIBRARY_PATH = self.cpp_info.libdirs[0]

        self.output.info("Appending PATH environment variable with : {}".format(bin_folder))
        self.output.info("LIBDIRS : {}".format(self.cpp_info.libdirs[0]))
        self.output.info("self.package_folder : {}".format(self.package_folder))
        self.output.info("includedirs : {}".format(self.cpp_info.includedirs))
        self.output.info("self.cpp_info.libs : {}".format(self.cpp_info.libs))
        self.output.info("v2 self.cpp_info.builddirs : {}".format(self.cpp_info.builddirs))
