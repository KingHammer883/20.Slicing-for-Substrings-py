# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18, 2019
File: Slicing for Substrings
@author: Byen23

Some applications extract portions of strings called substrings. FOr example, an application that sorts filenames according to type might use the last three characters in a filename, called its 'extension', to determine the file's type(exceptions to this rule, such as the extensions '.py', and '.html', will be considered later in this chapter). 

On a Windows file system, a filename ending in '.txt' denotes a human-readable text file, whereas a filename ending in '.exe' denotes an executable file of machine code. You can use Python's subscript operator to obtain a substring through a process called 'slicing'. To extract a substring, the progreammer places a colon(:) in the subscript. An integer value can appear on either side of the colon. Here are some examples that show how slicing is used:
"""

name = "myfile.txt" 		# The entire string
print(name[0:])

print(name[0:1])			# The first character

print(name[0:2]) 			# The first two characters

print(name[:len(name)])		# The entire string

print(name[-3:])			# The last three characters

print(name[2:6])			# Drill to extract 'file'

"""Generally, when two integer positions are included in the slice, the range of character in the substring extends from the first position up to but not including the second position.

When the integer is omitted on either side of the colon, all of the characters extending to the end or the beginning are included in the substring. Note that the last line of code provides the correct range to obtain the filename's three-character extension"""
