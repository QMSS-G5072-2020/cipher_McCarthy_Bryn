from cipher_bam2231_again import __version__
from cipher_bam2231_again import cipher_bam2231_again

def test_version():
    assert __version__ == '0.1.0'

def test_cipher_1():
    expected = 'uftujoh'
    sample_word = 'testing'
    actual = cipher(sample_word, shift = 1)
    assert expected == actual
