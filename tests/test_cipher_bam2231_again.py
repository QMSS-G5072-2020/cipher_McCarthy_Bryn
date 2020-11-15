from cipher_bam2231_again import __version__
from cipher_bam2231_again import cipher_bam2231_again

def test_version():
    assert __version__ == '0.1.0'

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_1():
    expected = 'uftujoh'
    sample_word = 'testing'
    actual = cipher(sample_word, shift = 1)
    assert expected == actual
