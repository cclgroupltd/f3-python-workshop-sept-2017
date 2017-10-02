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

# Declaring Variables
number = 7
text = "Hello, world!"

# Printing to the console is as easy as using the print statement
print(number)
print(text)

# All data in python is represented by objects - data which can also
# do something, here we ask the strings to return differently
# capitalised versions of themselves and also tell us about their
# content.
print(text.upper())
print(text.lower())
print(text.title())
print(text.isupper())
print(text.isnumeric())

# if statements allows your code to make choices based on currently
# held
if number > 6:
    print(f"the number {number} is greater than 7")

# Loops allow you code to repeat certain actions. Here we are using a
# "for" loop which allows us to perform an action *for each item in a
# sequence*. Here our sequence is the string "text". A string in a
# for loop will yield a single character per iteration of the loop.
for character in text:
    if character in ("a", "e", "i", "o", "u"):
        print(f"The character {character} is a vowel")
    else:
        print(f"The character {character} is not a vowel")