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
import sqlite3

# The sys module contains a range of system specific functionality
# but the most often used functionality is to get the arguments
# provided by the user at the command line.
input_path = sys.argv[1]

# We create a connection object that allows us to interact with our
# database
connection = sqlite3.connect(input_path)

# Cursors are used to execute queries on the database and retrieve
# rows from the result set. We can create as many as we require and
# run queries concurrently.
cursor = connection.cursor()
counter_cursor = connection.cursor()

# This query retrieves the names of the tables in the database.
table_query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(table_query)

# A database cursor in a for-loop will yield each row from the
# executed query each iteration of the loop.
for row in cursor:
    # the row is represented by a tuple, even when there's only a
    # single column, so here we get the table name by selecting the
    # zero'th item in the tuple.
    table_name = row[0]

    # We use this table name to build another query to get the count.
    # NB, in most cases when building queries like this we would use
    # parametrised queries, but you can't use a table name as a
    # parameter.
    count_query = f"SELECT count(*) FROM {table_name};"
    counter_cursor.execute(count_query)

    # As we know our query only returns a single row, we can use the
    # fetchone method rather than a loop.
    count = counter_cursor.fetchone()[0]

    print(f"{table_name}\t{count}")

