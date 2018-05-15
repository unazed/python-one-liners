this took a bit too long to make mainly because of the `receive_all` function which is actually a bit autistic. here it is:

```py
("receive_all",
  lambda self, ssize=4192, signal_timeout=2, _buffer=b"":
    (
      globals().__setitem__('_timeout',
        lambda time_, f, *args, **kwargs:
          (
            globals().__setitem__("signal", __import__("signal")),
            signal.signal(signal.SIGALRM, lambda _, frame: 0/0),
            signal.alarm(_time),
            f(*args, **kwargs),
            signal.alarm(0)
          )
      ),
      setvar("_inner_receive_all",
        lambda self, ssize=4192, _buffer=b"":
          (
            exec("def _autistic_receive_all(self, ssize=4192, _buffer=b''):\n\ttry: return [_autistic_receive_all(self, ssize, _buffer+data) if data else _buffer for data in [self.socket.recv(ssize)]][0]\n\texcept: return _buffer\nglobals()['_autistic_receive_all'] = _autistic_receive_all"),
            _autistic_receive_all
          )[1]
        ),
    _timeout(signal_timeout, _inner_receive_all(self), self, ssize),
    )[-1][-2]
)
```

here's what it essentially does:

1) you call receive_all
2) it instantiates the `_timeout` local function
3a) it creates the `_inner_receive_all` local function
3ba) that creates the `_autistic_receive_all` function which is the actual meat of the function
3bb) this `_autistic_receive_all` function uses recursion to retrieve the data segment by segment
4) an alarm is set and the `_inner_receive_all`'s inner `_autistic_receive_all` is called with `self` and `ssize`, whereupon the signal handler will raise a `ZeroDivisionError` after `signal_timeout` seconds have passed, and this will be caught by `_autistic_receive_all`'s `except: ...` clause which returns the `_buffer`, effectively passing it down to the `_timeout` function and then returning it to the original caller by retrieving the `[-1][-2]`'th index of the massive statement tuple

NOTES:
- this method only works for Linux (AFAIK) due to the usage of signals, i implemented it with signals because i just didn't want to use threading, fuck that.
- using `exec` is very cheaty however the repository is one liners, and as stated `the scripts posted have no intention of fully working to standardized expectations... so don't scrutinize them.`, i don't condone the usage of exec in professional or every-day code which other people will see but in this case not only is it unsafe but it's unavoidable.
- the indentation may be bent
- setting `signal_timeout` to `0` will cause it to hang, pls don't do this.
