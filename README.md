# tocode
<p align="center">
  <img src="doc/tocode.png">
</p>

[![Python version](https://img.shields.io/badge/python->%5E3.4-purple?style=flat-square)](https://www.python.org/)
[![BSD Licence](https://img.shields.io/badge/licence-MIT-geen?style=flat-square)](LICENSE)
<a href="https://github.com/Amir-Shamsi/tocode" title="Repo Size">
<img src="https://img.shields.io/github/repo-size/Amir-Shamsi/tocode?label=Repo%20Size&logo=Github&style=flat-square" alt="Project Initiator Repo Size"/>
</a>
[![Downloads](https://static.pepy.tech/personalized-badge/tocode?period=total&units=international_system&left_color=black&right_color=MediumVioletRed&left_text=Downloads)](https://pepy.tech/project/tocode)
[![PyPI version shields.io](https://img.shields.io/pypi/v/tocode.svg?style=flat-square)](https://pypi.python.org/pypi/tocode/)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/amir-shamsi/tocode/CodeQL?style=flat-square)
  
This is a library that can convert the strings to code and return the literal eval of that, it will convert strings which contain:
 - lists
 - tuples
 - dictionaries
 - sets
into the python eval.

## Overview

The most important thing in this library that make it unique is:<br>
**if your strings don't have any `quotation` no worries it will add quotations for you!**

example

**before**:
```diff
! "{'this': 5, (Alex, Daniel): are good boys, (5, 4): 8.5}" 
```

**after**:
```diff
+ "{'this': 5, ('Alex', 'Daniel'): 'are good boys', (5, 4): 8.5}
```

## Usage

In the following paragraphs, I am going to describe how you can get and use tocode for your own projects.

###  Getting it

To download tocode library, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install tocode
```

### Using it

tocode was programmed with ease-of-use in mind. First, import literal_eval from tocode.

for more exact usage documents you can see the example files [here](https://github.com/Amir-Shamsi/tocode/blob/master/src/examples)

```Python
import tocode

# Example:
my_array = " ['Hello', Goodbye my friend, 2.5, (4, ok), {one: 450, 'two': 12}] "
my_array = tocode.literal_eval(my_array, no_string_quotation=True)
"""
  if some of the strings don't have quotation set `no_string_quotation` to True
  otherwise, set it to False or leave it.
"""
# will return the list into a python list
```
output:
```python
['Hello', 'Goodbye my friend', 2.5, (4, 'ok'), {'one': 450, 'two': 12}]
```

## Support 
Supported versions of python for this library are as follow:
* [Python v3.4](https://www.python.org/downloads/release/python-340/)
* [Python v3.5](https://www.python.org/downloads/release/python-350/)
* [Python v3.6](https://www.python.org/downloads/release/python-360/)
* [Python v3.7](https://www.python.org/downloads/release/python-370/)
* [Python v3.8](https://www.python.org/downloads/release/python-380/)
* [Python v3.9](https://www.python.org/downloads/release/python-390/)
* [Python v3.10](https://www.python.org/downloads/release/python-3100/)


## License
This project is under MIT license read it
[here](https://github.com/Amir-Shamsi/tocode/blob/master/LICENSE):
```LICENSE
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
