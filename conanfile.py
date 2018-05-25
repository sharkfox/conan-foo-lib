
from conans import ConanFile, CMake

class ConanFoo(ConanFile):
    name        = "foo"
    version     = "4.0.1"
    description = "This is the famous foo library."
    url         = "https://github.com/sharkfox/conan-foo-lib"
    license     = "proprietary"
    generators  = "cmake"
    settings    = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone -b v%s %s.git ." % (self.version, self.url))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern = "*.h", dst = "include", src = "src", keep_path = False)
        self.copy(pattern = "*.a", dst = "lib", keep_path = False)
        self.copy(pattern = "*.lib", dst = "lib", keep_path = False)
        self.copy(pattern = "*.xml")

