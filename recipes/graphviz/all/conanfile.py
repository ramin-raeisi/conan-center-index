from conan import ConanFile
from conan.tools.files import get, copy
from conan.tools.scm import Version
from conan.errors import ConanInvalidConfiguration
import os

required_conan_version = ">=1.47.0"


class PackageConan(ConanFile):
    name = "graphviz"
    description = "open source graph visualization software"
    license = "CPL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://graphviz.org/"
    topics = ("graph", "visualization", "diagram", "pre-built")
    settings = "os", "arch", "compiler", "build_type"
    version = "2.38.0"

    def layout(self):
        pass

    def package_id(self):
        pass
        del self.info.settings.compiler
        del self.info.settings.build_type

    # in case some configuration is not supported
    def validate(self):
        if self.info.settings.os != "Linux":
            raise ConanInvalidConfiguration("Only Supported in Linux for now {}".format(self.info.settings.os))

    # do not cache as source, instead, use build folder
    def source(self):
        pass

    # download the source here, than copy to package folder
    def build(self):
        get(self, "https://github.com/ramin-raeisi/graphviz-rel/releases/download/2.38.0/graphviz.tar.gz")

    # copy all needed files to the package folder
    def package(self):
        # a license file is always mandatory
        copy(self, pattern="LICENSE", dst=os.path.join(self.package_folder, "licenses"), src=self.source_folder)
        copy(self, pattern="*", dst=self.package_folder, src=self.source_folder)

    def package_info(self):
        # folders not used for pre-built binaries
        self.cpp_info.frameworkdirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
        self.cpp_info.includedirs = []

        bin_folder = os.path.join(self.package_folder, "bin")
        # In case need to find packaged tools when building a package
        self.buildenv_info.append("PATH", bin_folder)
        # In case need to find packaged tools at runtime
        self.runenv_info.append("PATH", bin_folder)
        # TODO: Legacy, to be removed on Conan 2.0
        self.env_info.PATH.append(bin_folder)
