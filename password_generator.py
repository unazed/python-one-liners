while (True,(globals().__setitem__("enc", __import__("hashlib").shake_128),globals().__setitem__("randbetween", __import__("random").randint),[(globals().__setitem__("bfr", enc(mpw.encode())),print("iteration %d" % (c+1)),print("\trv. 1: %s" % (globals().__setitem__("mem", bfr.digest(8*randbetween(1, 8))), mem)[-1]),print("\trv. 2: %r" % mem.decode('ascii', 'ignore')),print("\trv. 3: %r" % ''.join(filter(str.isalpha, mem.decode('utf8', 'ignore')))),print("\trv. 4: %r" % (''.join(filter(str.isnumeric, mem.decode('utf8', 'ignore'))) or 'empty'))) for c in range(8)]) if 'mpw' in globals() else ())[0]: mpw = input("master password (1 for 8... bargain) >> ")