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

import urllib.request
import urllib.parse
import bs4

# This example demonstrates one method for scraping a page on a phpbb
# forum.

# The url here is hard-coded, but we could, of course retrieve it
# from the command line.
start_url = r"https://arstechnica.com/civis/viewtopic.php?f=6&t=1231727"

# We keep track of the next url in the thread. It will initially be
# the start url, but at the end of the loop we try to get the next
# one from the page.
next_url = start_url
while next_url:
    r = urllib.request.urlopen(next_url)
    soup = bs4.BeautifulSoup(r, "html.parser")
    for post in soup.find_all(class_="post"):
        post_id = post["id"]
        author_name = post.find(class_="post-author-name").get_text()
        post_date = post.find(class_="post-date").get_text()
        content = post.find(class_="post-content-inner").get_text()

        print(post_id)
        print(author_name.strip())
        print(post_date.strip())
        print(content)

    # We can search for an element based on its text, here we're
    # looking for an anchor tag with the text "Next".
    next_link = soup.find(class_="pager").find("a", text="Next")
    if next_link:
        next_url = urllib.parse.urljoin(next_url, next_link["href"])
    else:
        next_url = None
