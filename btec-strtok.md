recursive lambdas, static list usage, damn all of this shit is interesting!

issue: it doesn't work for any other delimiter besides the default one, don't plan on fixing it and that's why the name starts with `btec-`.

usage follows:

```py
>>> my_input = input()
my name is unazed, and i like huge pythons
>>> strtok(my_input, None)
>>> strtok(my_input)
'my'
>>> strtok(my_input)
'name'
>>> strtok(my_input)
'is'
>>> strtok(my_input)
'unazed,'
>>> strtok(my_input)
'and'
>>> strtok(my_input)
'i'
>>> strtok(my_input)
'like'
>>> strtok(my_input)
'huge'
>>> strtok(my_input)
'pythons'
>>> strtok(my_input)
(implicit None)
>>> 
```
