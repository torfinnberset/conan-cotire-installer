from conans import ConanFile
from conans.tools import download, unzip
import os

VERSION = "1.6.6"


class CotireConan(ConanFile):
    name = "cotire"
    version = os.environ.get("CONAN_VERSION_OVERRIDE", VERSION)
    generators = "cmake"
    requires = tuple()
    url = "http://github.com/sakra/cotire"
    license = "MIT"

    def source(self):
        zip_name = "cotire.zip"
        download("https://github.com/sakra/"
                 "cotire/archive/{version}.zip"
                 "".format(version="cotire-" + VERSION),
                 zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="*.cmake",
                  dst="cmake/cotire",
                  src=os.path.join("cotire-cotire-" + VERSION, "CMake"),
                  keep_path=True)
