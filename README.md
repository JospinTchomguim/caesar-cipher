# caesar-cipher
Program with graphical interface for encryption and decryption of Cesar


In cryptography, the shift cipher, also known as Caesar's cipher or Caesar's code, is a very simple cipher method used by Julius Caesar in his secret correspondence (hence the name "cipher of Caesar").

The ciphertext is obtained by replacing each letter of the original plaintext with a letter at a fixed distance, always on the same side, in the order of the alphabet. For the last letters (in the case of a shift to the right), we start again from the beginning. For example with a shift of 3 to the right, A is replaced by D, B becomes E, and so on until W which becomes Z, then X becomes A etc. It is a circular permutation of the alphabet. The length of the offset, 3 in the example mentioned, constitutes the key of the cipher that it suffices to transmit to the recipient — if he already knows that it is a Caesar cipher — so that he can decipher the message. In the case of the Latin alphabet, the Caesar cipher has only 26 possible keys (including the null key, which does not modify the text).

This is a special case of encryption by monoalphabetic substitution: these substitutions are based on a similar principle, but are obtained by any permutations of the letters of the alphabet. In the general case, the key is given by the permutation, and the number of possible keys is then disproportionate to that of the Caesar ciphers.

The Caesar cipher could have been used as part of a more complex method, such as the Vigenère cipher. Alone, it offers no communication security, because of the very low number of keys, which makes it possible to try them systematically when the encryption method is known, but also because, like any encoding by monoalphabetic substitution, it can be "broken" very quickly by frequency analysis (some letters appear much more often than others in a natural language).

EXEMPLE:

Encryption can be represented by the superposition of two alphabets, the clear alphabet presented in the normal order and the encrypted alphabet shifted, to the left or to the right, by the desired number of letters. Below is an example of encoding 3 letters to the right. The offset parameter (here 3) is the encryption key:

clear: ABCDEFGHIJKLMNOPQRSTUVWXYZ
encrypted: DEFGHIJKLMNOPQRSTUVWXYZABC

To encode a message, just look at each letter of the plain message, and write the corresponding encoded letter. To decipher, we simply do the opposite.

original: WIKIPEDIA THE FREE ENCYCLOPEDIA
encoded: ZLNLSHGLD O'HQFBFORSHGLH OLEUH

Encryption can also be represented using congruences on integers. Starting by transforming each letter into a number (A = 0, B = 1, etc., Z = 25)1, to encode a letter x with a key n, just apply the formula:

E_{n}(x)= (x+n)[26]

Decryption consists of using the opposite key ( − n instead of n):

D_{n}(x)= (x-n)[26] 

We can arrange for the result to always be represented by an integer from 0 to 25: if x + n (respectively x − n) is not in the interval [0, 25], just subtract (respectively add) 26.

The offset always remaining the same for the same message, this method is a monoalphabetic substitution, unlike the Vigenère cipher which constitutes a polyalphabetic substitution.
