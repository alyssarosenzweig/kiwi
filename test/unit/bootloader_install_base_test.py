
from mock import patch

import mock

from .test_helper import *

from kiwi.exceptions import *
from kiwi.bootloader.install.base import BootLoaderInstallBase


class TestBootLoaderInstallBase(object):
    def setup(self):
        self.bootloader = BootLoaderInstallBase(
            'root_dir', mock.Mock()
        )

    @raises(NotImplementedError)
    def test_install(self):
        self.bootloader.install()
