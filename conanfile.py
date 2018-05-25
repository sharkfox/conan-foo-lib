
from conans import ConanFile, CMake
import os

class ConanFoo(ConanFile):
    name        = "foo"
    version     = "4.0.1"
    description = "This is the famous foo library."
    url         = "http://example.com"
    license     = "proprietary"
    generators  = "cmake"
    settings    = "os", "compiler", "build_type", "arch"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern = "*.h", dst = "include", src = "src", keep_path = False)
        self.copy(pattern = "*.a", dst = "lib", keep_path = False)
        self.copy(pattern = "*.lib", dst = "lib", keep_path = False)
        self.copy(pattern = "*.xml")

