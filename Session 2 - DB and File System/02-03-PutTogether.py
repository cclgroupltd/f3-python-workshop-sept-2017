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
import sqlite3

FILE_SIG = b"SQLite format 3\x00"

start_dir = sys.argv[1]
for current_dir, dirs, files in os.walk(start_dir):
    for file in files:
        full_path = os.path.join(current_dir, file)

        f = open(full_path, "rb")

        first_16_bytes = f.read(16)
        f.close()

        if first_16_bytes == FILE_SIG:
            print(full_path)

            input_path = full_path
            connection = sqlite3.connect(input_path)
            cursor = connection.cursor()
            counter_cursor = connection.cursor()
            table_query = "SELECT name FROM sqlite_master WHERE type='table' AND rootpage != 0;"
            cursor.execute(table_query)

            for row in cursor:
                table_name = row[0]
                count_query = f"SELECT count(*) FROM {table_name};"

                try:
                    counter_cursor.execute(count_query)
                    count = counter_cursor.fetchone()[0]
                except sqlite3.OperationalError as e:
                    count = "Could not read table"

                print(f"\t{table_name}\t{count}")