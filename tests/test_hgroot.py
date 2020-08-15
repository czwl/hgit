import pytest

from pyfakefs   import fs

def test_fake_fs(fs):
    # "fs" is the reference to the fake file system
    fs.create_file('/var/data/xx1.txt')
    assert os.path.exists('/var/data/xx1.txt')