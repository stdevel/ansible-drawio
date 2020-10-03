"""
Role unit tests
"""
import fnmatch


def test_drawio_package(host):
    """
    Ensure that the drawio package is installed
    """
    drawio_pkg = host.package("draw.io")
    drawio_bin = host.file("/usr/bin/drawio")

    assert drawio_pkg.is_installed
    assert drawio_bin.exists


def test_drawio_appimage(host):
    """
    Ensure that drawio AppImage is installed
    """
    opt_files = host.file("/opt").listdir()
    images = fnmatch.filter(opt_files, "drawio*.AppImage")
    assert images
