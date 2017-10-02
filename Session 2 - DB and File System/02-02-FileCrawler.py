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
import os
import pathlib
import typing

# For your interest: here is a function which does recursive walking
# of a directory using pathlib. It's not quite synonymous with
# os.walk as it doesn't organise the results into lists (because in
# pathlib, you can ask the objects whether or not they are
# directories etc.)
def walk(root: pathlib.Path, follow_symlinks: bool=False) -> typing.Iterable[pathlib.Path]:
    stack = [root]
    while stack:
        this_dir = stack.pop()
        for p in this_dir.iterdir():
            yield p
            if p.is_dir() and (follow_symlinks or not p.is_symlink):
                stack.append(p)

# the b at the start of the string means that it's a binary "bytes"
# object.
FILE_SIG = b"SQLite format 3\x00"

# Get the start directory from command line arguments.
start_dir = sys.argv[1]

# The os.walk function recursively walks across a folder structure.
# and yields a tuple containing the: current directory it is
# accessing, a list of sub directories and a list of files.
for current_dir, dirs, files in os.walk(start_dir):
    for file in files:
        # We create the full path, safely and in a platform
        # independent manner using os.path.join
        full_path = os.path.join(current_dir, file)

        # open the file in read-only, binary mode. A file object
        # gives us access to the file for reading and writing
        # (dependant on the mode used)
        f = open(full_path, "rb")
        first_16_bytes = f.read(16)
        f.close()

        # Check that the first 16 bytes match our file signature...
        if first_16_bytes == FILE_SIG:
            print(full_path)

