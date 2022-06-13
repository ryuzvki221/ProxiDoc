from src.proxidoc import __version__,author


def test_version():
    assert __version__() == '0.1.0'

def test_author():
    assert author() == 'cheikh'

