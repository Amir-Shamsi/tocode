# tocode
<p align="center">
  <img src="doc/tocode.png">
</p>

This is a library which can convert the strings to code and return the literal eval of that it will convert strings which contain:
 - lists
 - tuples
 - dictionaries
 - sets

into the python eval and the most important thing in this library that make it unique is:<br>
**when your strings doesn't have any `quotation` no worries it will add qoutations for you!**

example

**before**:
```diff
! "{'this': 5, (Alex, Daniel): are good boys, (5, 4): 8.5}" 
```

**after**:
```diff
+ "{'this': 5, ('Alex', 'Daniel'): 'are good boys', (5, 4): 8.5}
```
