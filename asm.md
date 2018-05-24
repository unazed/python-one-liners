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
