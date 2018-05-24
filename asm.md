unfinished however it can store variables, allow for extension and do other cool things ig.

turning out to be harder than i thought to compress a nicer `parse_instruction` function into one line, purely because lambdas can't force returns without some fuckery which i have yet to discover

(i know i'm going back on my word by building from the top -> down, but i honestly tried doing this in one line without this sort of high level knowledge and it's simply hideous looking hot shit that doesn't work)

```py
import sys


def split_instruction(string):
    if len(string.split()) == 1:
        return {
            "opcode": string.split()[0],
            "operands": ()
        }
    opcode = string.split()[0]
    string = ' '.join(string.split()[1:])

    def _parse_string(substring):
        string = ""
        for char in substring:
            if char == '"':
                return (string, len(string))
            string += char
        sys.exit("error: string with missing ending quotation marks.")
    def _parse_immediate(substring):
        string = ""
        for char in substring:
            if not char.isdigit():
                return (string, len(string))
            string += char
        return (string, len(string))
    def _parse_token(substring):
        string = ""
        for char in substring:
            if char in (",", " "):
                return (string, len(string))
            elif not char.isalnum():
                sys.exit("error: invalid characters in token name")
            string += char
        return (string, len(string))

    tokens = []
    str_len = False
    immed_len = False
    token_len = False
    
    for idx, char in enumerate(string):
        substring = lambda ofs=0: string[idx+ofs:]
        if str_len:
            str_len -= 1
        elif immed_len:
            immed_len -= 1
        elif token_len:
            token_len -= 1
        elif char == '"':
            pstring, length = _parse_string(substring(1))
            tokens.append(('"%s"' % pstring, Variable))
            str_len = length+1
        elif char.isdigit():
            immed, length = _parse_immediate(substring())
            tokens.append((immed, Immediate))
            immed_len = length
        elif char.isalpha():
            token, length = _parse_token(substring())
            tokens.append((token, Variable))
            token_len = length

    return {
        "opcode": opcode,
        "operands": tokens
    }
```

update: turns out it's pretty impossible to go back on your word because there's a large enough difference between these two arts of high level abstraction and lower level restriction s.t. trying to simply blend the dynamics of high level-ness will ignite.

```py
setvar("parse_instruction", lambda string:
    (
        setvar("_parse_string",  lambda substring:
            (
                setvar("sstring", ""),
                setvar("sentinel", False),
                setvar("ret", None),
            [
                (setvar("sentinel", True), setvar("ret", (sstring, len(sstring))))
                    if char == '"' else
                setvar("sstring", sstring+char)
                for char in substring if not sentinel
            ],
                sys.exit("error: no trailing quotation marks.") if not sentinel else ret
            )[-1]
        ),
        setvar("_parse_immediate", lambda substring:
            (
                setvar("istring", ""),
                setvar("sentinel", False),
                setvar("ret", None),
            [
                (setvar("sentinel", True), setvar("ret", (istring, len(istring))))
                    if not char.isdigit() else setvar("istring", istring+char)
                    if idx != len(substring)-1 else (setvar("istring", istring+char), setvar("ret", ("istring", len(istring))))
                for idx, char in enumerate(substring) if not sentinel
            ],
                ret
            )[-1]
        ),
        setvar("_parse_token", lambda substring:
            (
                setvar("tstring", ""),
                setvar("sentinel", False),
                setvar("ret", None),
            [
                (setvar("sentinel", True), setvar("ret", (tstring, len(tstring))))
                    if char in (" ", ",") else
                sys.exit("error: invalid character: %r, in token-name." % char)
                    if not char.isalnum() else setvar("tstring", tstring+char)
                    if idx != len(substring)-1 else (setvar("tstring", tstring+char), setvar("ret", (tstring, len(tstring))))
                for idx, char in enumerate(substring) if not sentinel
            ],
                ret
            )[-1]
        ),
        
        {
            "opcode": string.split()[0],
            "operands": ()
        } if len(string.split()) == 1 else (
            setvar("opcode", string.split()[0]),
            setvar("op_string", ' '.join(string.split()[1:])),
            setvar("str_len", 0),
            setvar("imm_len", 0),
            setvar("tok_len", 0),
            setvar("tokens", []),
        [
            [
            setvar("substring", lambda ofs=0: op_string[idx+ofs:]),
            (
                    [
                        setvar("sstring_length", _parse_string(substring(1))),
                        tokens.append(['"%s"' % sstring_length[0], Variable]),
                        setvar("str_len", sstring_length[1]+1)
                    ] if char == '"' else [
                        setvar("istring_length", _parse_immediate(substring())),
                        tokens.append([istring_length[0], Immediate]),
                        setvar("imm_len", istring_length[1])
                    ] if char.isdigit() else [
                        setvar("tstring_length", _parse_token(substring())),
                        tokens.append([tstring_length[0], Register if get_register(tstring_length[0]) else Variable]),
                        setvar("tok_len", tstring_length[1])
                    ] if char.isalpha() else None
                ) if all([setvar("str_len", str_len-1) if str_len else True,setvar("imm_len", imm_len-1) if imm_len else True,setvar("tok_len", tok_len-1) if tok_len else True]) else None
            ]
            for idx, char in enumerate(op_string)
        ],
        {
            "opcode": opcode,
            "operands": tokens
        }
        )[-1]
    )[-1]
),
```
