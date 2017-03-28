import subprocess


def test_linkcheck(tmpdir):
    """ validates links inside documentation
    """
    doctrees = tmpdir.join("doctrees")
    htmldir = tmpdir.join("html")
    subprocess.check_call(
        ["sphinx-build", "-W", "-blinkcheck",
         "-d", str(doctrees), "source", str(htmldir)])

