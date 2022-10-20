from conans import ConanFile, tools
from conans import __version__ as conan_version
from conans.model.version import Version
import os
import subprocess


class PlantUML(ConanFile):
    name = "PlantUML"
    version = "1.2020.0"
    description = "PlantUML. Useful as build_require"
    author = "Satyam Satyam.LaxmiSharanLal@in.bosch.com"
    url = "https://github.com/ramin-raeisi/plantuml-conan/releases/download/1.2020.0/conan_package.tgz"
    exports_sources = "plantuml.jar"
    settings = "os", "arch"
    short_paths = True
    apply_env = False

    def build(self):
        tools.get(self.url)

        if self.settings.os == "Linux":
            myCmd = 'ls -al'
            process = subprocess.Popen(myCmd, stdout=subprocess.PIPE, shell=True)
            proc_stdout = process.communicate()[0].strip()
            print(proc_stdout)

            myCmd2 = 'chmod ug+rwx plantuml.jar'
            process = subprocess.Popen(myCmd2, stdout=subprocess.PIPE, shell=True)
            proc_stdout = process.communicate()[0].strip()
            print(proc_stdout)

            myCmd3 = 'ls -al'
            process = subprocess.Popen(myCmd3, stdout=subprocess.PIPE, shell=True)
            proc_stdout = process.communicate()[0].strip()
            print(proc_stdout)

    def package(self):
        self.copy("*", "", "", True, True)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder))
        self.cpp_info.includedirs = []
