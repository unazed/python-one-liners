for line in (
globals().__setitem__("setvar", lambda n, v, o=True: globals().__setitem__(n, v) if o or n not in globals() else False),
setvar("Register", type("Register", (object,), {
"__init__":
    lambda self, name, content=None:
        (
        setattr(self, "content", content),
        setattr(self, "name", name),
        None
        )[-1]
})),
setvar("Variable", type("Variable", (object,), {"__init__": lambda self, name, content=None:(setattr(self, "content", content),setattr(self, "name", name),None)[-1]})),
setvar("Immediate", type("Immediate", (object,), {"__init__": lambda self, content: setattr(self, "content", content)})),
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
setvar("imp", lambda n: setvar(n, __import__(n), False)),
setvar("operand_map", {
    ("Register", Register): tuple([Register(reg, None) for reg in ("eax", "ecx", "edx", "ebx", "esp", "ebp", "esi", "edi", "flags")]),
    ("Variable", Variable): set()
}),
setvar("print_register", lambda name: ret if True in [(setvar("ret", reg.content), True)[1] if reg.name == name else None for reg in operand_map[('Register', Register)]] else sys.exit("error: no such register %r" % name)),
setvar("print_variable", lambda name: [print(var.content) if var.name == name else None for var in operand_map[('Variable', Variable)]]),
setvar("get_register", lambda name: (setvar("registers", [*filter(lambda r: isinstance(r, Register), [reg if reg.name == name else None for reg in operand_map[('Register', Register)]])]),False if not registers else registers[0])[-1]),
setvar("get_variable", lambda name: (setvar("variables",[*filter(lambda n: isinstance(n, Variable),[var if var.name == name else None for var in operand_map[('Variable', Variable)]])]),False if not variables else variables[0])[-1]),
setvar("get_string_varname", lambda string: (setvar("strings", [*filter(lambda n: isinstance(n, str), [var if var.content == string else None for var in operand_map[('Variable', Variable)]])]),False if not strings else strings[0])[-1]),
setvar("add_variable", lambda name, content=None: operand_map[('Variable', Variable)].add(Variable(name, content))),
setvar("opcode_typemap", {
    (Variable, Variable): ["mov"],
    (Variable, Immediate): ["mov", "add", "sub", "mul", "div", "pow", "call"],
    (Variable, Register): ["mov", "add", "sub", "mul", "div", "pow"],
    (Immediate, Variable): False,
    (Immediate, Immediate): False,
    (Immediate, Register): False,
    (Register, Variable): ["mov", "add", "sub", "mul", "div", "pow"],
    (Register, Immediate): ["mov", "add", "sub", "mul", "div", "pow"],
    (Register, Register): ["mov", "add", "sub", "mul", "div", "pow"],
    (Register,): ["inc", "dec"],
    (Variable,): ["inc", "dec"],
}),
setvar("stack", []),
setvar("opcode_function_map", {
    "mov": lambda op1, op2: setattr(op1, "content", op2.content),
    "add": lambda op1, op2: setattr(op1, "content", int(op1.content)+int(op2.content)),
    "inc": lambda op1: setattr(op1, "content", int(op1.content)+1),
    "dec": lambda op1: setattr(op1, "content", int(op1.content)-1),
    "sub": lambda op1, op2: setattr(op1, "content", int(op1.content)-int(op2.content)),
    "mul": lambda op1, op2: setattr(op1, "content", int(op1.content)*int(op2.content)),
    "div": lambda op1, op2: setattr(op1, "content", int(op1.content)//int(op2.content)),
    "pow": lambda op1, op2: setattr(op1, "content", int(op1.content)**int(op2.content)),
    "call": lambda op1, op2: globals()[op1.content](*[*[stack.pop() for _ in range(int(op2.content))]]) if len(stack) >= int(op2.content) else sys.exit("error: requested %r variables, but only got %r" % (op2.content, len(stack)))
}),
setvar("identify_operand_type", 
lambda instruction, define_labels=False:
    {
        instruction['opcode']:
        [
            get_register(operand[0]) if operand[1] is Register else
            sys.exit("error: undefined variable %r." % operand[0]) if not define_labels else (
            [add_variable(operand[0]), get_variable(operand[0])][-1] if not operand[0].startswith('"') else
            [add_variable(
                (
                    setvar("name",
                           "str_%s" % format(hash(operand[0])&0xFFFFFFFF, 'x')
                          ),
                    name
                )[-1],
                operand[0].replace('"', '')
            ),
            get_variable(name)
            ][-1]
            ) if not (
                setvar("_",
                    get_variable(operand[0])
                ),
                _
            )[-1] else _ if operand[1] is Variable else
            int(operand[0]) if operand[1] is Immediate else
            sys.exit("error: unknown error with variable: %r" % operand)
            for operand in instruction['operands']
        ]
    }
),
setvar("generate_opcode_map", lambda opcode_typemap, opcode_function_map: { (op, *pair[0]): opcode_function_map[op] for pair in opcode_typemap.items() if pair[1] for op in pair[1]}),
imp("sys"),
imp("os"),
sys.exit("usage:\n  python3 asm.py <source-file>") if len(sys.argv) != 2 else setvar("sfile", sys.argv[1]),
sys.exit("error: no file %r" % sfile) if sfile not in os.listdir() else setvar("sfile", open(sfile)),
[*map(str.strip, [*sfile])],
sfile.close()
)[-2]: (
print(line),
setvar("parsed_line", parse_instruction(line)),
setvar("parsed_line", identify_operand_type(parsed_line, True)),
setvar("line_template", ([*parsed_line.keys()][0], *map(type, [*parsed_line.values()][0]))),
setvar("generated_opcode_map", generate_opcode_map(opcode_typemap, opcode_function_map)),
sys.exit("error: operand type mismatch for %r" % parsed_line) if (setvar("opcode", generated_opcode_map.get(line_template, None)), opcode)[1] is None else None,
opcode(*[*parsed_line.values()][0]),
)
