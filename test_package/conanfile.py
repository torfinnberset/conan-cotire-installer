import os

from conans import ConanFile, CMake, tools


class CotireTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()

    def test(self):
        self.output.success("CMake configured with cotire")