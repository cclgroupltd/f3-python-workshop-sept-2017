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

import sys
import bs4

# Beautiful soup is a 3rd party library which you can install using
# pip.
# The command line will be something like:
#     pip install --user bs4
# Or to create a wheel to use on an offline machine:
#     pip wheel bs4

input_file = sys.argv[1]
f = open(input_file, "rb")

# To search for data in the webpage we turn the file into a "soup".
# the procedure for doing this with data pulled from a web request is
# essentially identical except we provide the BeautifulSoup
# constructor with a request object rather than a file.
soup = bs4.BeautifulSoup(f, "html.parser")

# In this example we used the html from a wikipedia page and aimed
# to extract the table of contents and the links on the page.

# Using find we select the first tag with the id of "toc", and then
# within that tag we use find-all to get all the "li" elements.
# Similarly within the loop we get the tags with the class of
# "tocnumber" and "toctext" and get their text content. We have to
# use "class_" (with an underscore) as the word "class" has special
# meaning in Python.
for list_item in soup.find(id="toc").find_all("li"):
    toc_number = list_item.find(class_="tocnumber").get_text()
    toc_text = list_item.find(class_="toctext").get_text()

    print(toc_number, toc_text)

for anchor_tag in soup.find_all("a"):
    # the "get" method of a BeautifulSoup element gets the attribute
    # named if present, otherwise it returns "None" which when
    # evaluated in an "if" statement counts as "false", which is why
    # the code below works.
    link = anchor_tag.get("href")
    if link:
        print(link)
