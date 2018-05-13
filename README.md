# python-one-liners
trust me i haven't run out of ideas

__synopsis of the fundamentals regarding one-liners in an imperative language:__

globals() is the variable space where within you can set variables because it's just a dictionary.

there's three layers of abstraction.

```py
a = 1
globals()['a'] = 1
globals().__setitem__('a', 1)
```

the first of which is what you normally do in standard practice

the second of which can be done but only when you want vary-able variable names e.g. a1, a2, a3, and don't want to hardcode it

the third of which is if you want to use it in its functional form which counts as an expression meaning it can be placed anywhere
and it'll be evaluated like normal, but it doesn't include any syntax like `=` which doesn't return a value.

i've found that if you use while loops in one liners you can usually be clever and have a certain index act as the dependent
variable e.g.:

```py
while [
  globals().__setitem__("my_count", 0)\  # if my_count doesn't exist, set it to 0. equivalent to `my_count = 0`
    if "my_count" not in globals() else\
  globals().__setitem__("my_count", my_count+1), # if my_count exists, add 1 to it, equivalent to `my_count += 1`
  globals().get("my_count", False)  # equivalent to just `my_count`, which returns the variable else False if it doesn't exist
][1] < 5:  # refers to the 2nd item in the list, which is the `my_count` variable, basically `while my_count < 5: pass`
	pass
```

although you could integrate the addition possibly

```py
while [
  globals().__setitem__("my_count", 0) if "my_count" not in globals() else 0,
  globals().get("my_count", False)
][1] < 5: my_count += 1
```

which is a waaay nicer form of the above version, equivalent to the imperative form:

```py
my_count = 0
while my_count < 5:
	my_count += 1
```


**protip:** the scripts posted have no intention of fully working to standardized expectations... so don't scrutinize them.
**post protip:** i code purely from the point of view i've described above, i don't write pretty (or thereabouts) code first and translate. that's no fun.
