while(globals().__setitem__("NOTFOUND", 0xFFFF),globals().__setitem__("EXISTS", 0xFFFF-1),globals().__setitem__("getvar", lambda n: globals().get(n,NOTFOUND)),globals().__setitem__('setvar', lambda n, k, override=False: (globals().__setitem__(n, k) if getvar(n) == NOTFOUND or override else EXISTS)),setvar("verify_sums", lambda s: __import__("sys").exit("%s wins" % playermap[10]) if 30 in s else __import__("sys").exit("%s wins" % playermap[1]) if 3 in s else __import__("sys").exit("draw") if count//2 > 5 else False),setvar("printboard", lambda: print('\n'.join(' '.join(map(lambda s: playermap[s], row)) for row in board))),setvar("getinput", lambda: setrc(int(input("row (idx) >> ")), int(input("column (idx) >> ")), [*playermap.keys()][count % 2])),setvar("setrc", lambda row, column, p: board[int(row)].__setitem__(int(column), p) if getvar("board") else print("board is being created. please wait")),setvar("board", [[0]*3, [0]*3, [0]*3]),setvar("count", 0),setvar("first", True),setvar("start", __import__("random").choice([1, 10])),setvar("playermap", {1: "x", 10: "o", 0: "-"}),setvar("sums", [*map(sum, board)]+[*map(sum, [*zip(*board)])]+[sum(board[n][n] for n in range(3)), sum(board[n][k] for n, k in [*zip([2, 1, 0], [0, 1, 2])])], True),print("welcome to my one-line tic-tac-toe game!") if first else None,setvar("first", False, True),setvar("count", count+1, True)): (printboard(), verify_sums(sums), getinput())
