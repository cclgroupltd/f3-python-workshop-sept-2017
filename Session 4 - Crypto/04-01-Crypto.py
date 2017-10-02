#!/usr/bin/env python3

"""
Copyright (c) 2017, CCL Forensics
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the CCL Forensics nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL CCL FORENSICS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

"""
The following code was originally used as a basis for a Python taster
day presented by Alex Caithness for the First Forensics Forum (F3)
in September, 2017. It is presented here for educational purposes.
"""

import Crypto.Cipher.AES

# pycrypotdome is a drop in replacement module for the venerable
# pycrypto module.

iv = b"0123456789abcdef"
key = b"keykeykeykey!!!!"

# The arguments passed to the new() function for each block cipher
# type will be the key, followed by the mode - and then specific
# arguments for the mode chosen (refer to the documentation)
encrypter_alg = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CFB, iv)
plain_text = b"this is the plain text"
cipher_text = encrypter_alg.encrypt(plain_text)
print(cipher_text)

more_cipher_text = encrypter_alg.encrypt(plain_text)
print(more_cipher_text)

decrypter_alg = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CFB, iv)
decrypted = decrypter_alg.decrypt(cipher_text)
print(decrypted)



