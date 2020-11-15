def cipher(text, shift, encrypt=True):
    """
    Encrypts words by shifting the direction of letters.

    Parameters:
    -----------
    text = Word whose letters will be converted. String.
    shift = Number of positions up/down the alphabet to shift letters. Int.
    encrypt = Direction of encryption. Boolean.

    Examples:
    -----------
    cipher("testing", 1)
    "uftjoh"

    cipher("uftjoh", -1)
    "testing"

    cipher("uftjoh", 1, encrypt = False)
    "testing"
    """
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
