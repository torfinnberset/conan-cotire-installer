from conans import ConanFile, tools
import os


class CotireConan(ConanFile):
    name = "cotire_installer"
    version = "1.8.0"
    generators = "cmake"
    url = "https://github.com/torfinnberset/conan-cotire-installer"
    homepage = "https://github.com/sakra/cotire"
    description = "Cotire (compile time reducer) is a CMake module that speeds up"  \
                  " the build process of CMake based build systems by fully automating" \
                  " techniques such as precompiled header usage and single compilation " \
                  " unit builds for C and C++."
    license = "MIT"

    def source(self):
        tools.get(F"https://github.com/sakra/cotire/archive/cotire-{self.version}.zip")

    def package(self):
        self.copy(pattern="*.cmake", src=F"{self.source_folder}/cotire-cotire-{self.version}/CMake")
