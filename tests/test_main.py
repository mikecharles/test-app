from python_skeleton import __main__


def test_main_output(capsys):
    __main__.main()
    sysout, syserr = capsys.readouterr()
    assert sysout == 'This is the main function.\n'
