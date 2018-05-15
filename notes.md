- as far as i've seen, `locals()` seems to hurt programming more than using `globals()`, mainly because it provides lookup issues.
- this is starting to look more like lisp than python
- considering suicide is no longer a valid choice
- it gets fun when you start finding interesting ideas
- #operatingsysteminoneline
- there's a sorta beauty to writing this, although it's always the same method and tactic, there's definite exceptions where you can nicely integrate the core features of python with such an abomination
- there's no such thing as a beautiful one liner with more than one functionality
- this shit really makes you think outside the box for finding ways to bypass python's `no-keywords-in-expressions` restriction, especially exception handling
- this doesn't make you a better programmer more than it would make you higher iq
- there's something interesting to hearing that something seemingly large or medium-sized can be condensed to one line
- i'm starting to contemplate whether what i'm doing isn't *truly* one-lines, surely a one liner would mean that if you tried to expand it to anything more than one line (without bloating it, same bytecode) you wouldn't be able to
- can i get onto the core dev. team yet?
- i think i found an issue in python during my creation of tic-tac-toe
```py
>>> my_lists = [[0]*3]*3
>>> my_lists[0] is my_lists[1]
True
>>> my_not_retarded_lists = [[0]*3, [0]*3, [0]*3]
>>> my_not_retarded_lists[0] is my_not_retarded_lists[1]
False
```
caused me to have some issues where all the rows of that column that the user selected to change changed, and not just the specific co-ordinate the user selected.

```py
>>> my_lists[0].__setitem__(0, 1)
>>> my_lists
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

smh
