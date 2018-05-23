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
setvar("parse_instruction", lambda i: [{"opcode": inst[0],"operands": inst[1:]} for inst in [i.replace(",", " ").split()] if inst][0]),
setvar("imp", lambda n: setvar(n, __import__(n), False)),
setvar("operand_map", {
    ("Register", Register): tuple([Register(reg, None) for reg in ("eax", "ecx", "edx", "ebx", "esp", "ebp", "esi", "edi")]),
    ("Variable", Variable): set()
}),
setvar("print_register", lambda name: ret if True in [(setvar("ret", reg.content), True)[1] if reg.name == name else None for reg in operand_map[('Register', Register)]] else sys.exit("error: no such register %r" % name)),
setvar("print_variable", lambda name: [print(var.content) if var.name == name else None for var in operand_map[('Variable', Variable)]]),
setvar("opcode_typemap", {
    (Variable , Variable ): ["mov"],
    (Variable , Immediate): ["mov", "add"],
    (Variable , Register ): ["mov", "add"],
    (Immediate, Variable ): False,
    (Immediate, Immediate): False,
    (Immediate, Register ): False,
    (Register , Variable ): ["mov", "add"],
    (Register , Immediate): ["mov", "add"],
    (Register , Register ): ["mov", "add"],
    (Register,): ["inc"],
    (Variable,): ["inc"],
}),
setvar("opcode_function_map", {
    "mov": lambda op1, op2: setattr(op1, "content", op2.content),
    "add": lambda op1, op2: setattr(op1, "content", int(op1.content)+int(op2.content)),
    "inc": lambda op1: setattr(op1, "content", int(op1.content)+1)
}),
setvar("identify_operand_type", 
lambda operand, define_labels=False:
    r
    if any((setvar("r", reg), True)[1] if reg.name == operand else False for reg in operand_map[('Register', Register)]) else
    Immediate(int(operand))
    if operand.isdigit() else
    v
    if any((setvar("v", var), True)[1] if var.name == operand else False for var in operand_map[('Variable', Variable)]) else
    (setvar("v", Variable(operand)), operand_map[('Variable', Variable)].add(v), v)[-1]
    if define_labels else
    sys.exit("error: undefined label %r" % operand)
),
setvar("generate_opcode_map", lambda opcode_typemap, opcode_function_map: { (op, *pair[0]): opcode_function_map[op] for pair in opcode_typemap.items() if pair[1] for op in pair[1]}),
imp("sys"),
imp("os"),
sys.exit("usage:\n  python3 asm.py <source-file>") if len(sys.argv) != 2 else setvar("sfile", sys.argv[1]),
sys.exit("error: no file %r" % sfile) if sfile not in os.listdir() else setvar("sfile", open(sfile)),
[*map(str.strip, [*sfile])],
sfile.close()
)[-2]: (
setvar("parsed_line", parse_instruction(line)),
setvar("parsed_line", {parsed_line['opcode']: [identify_operand_type(op, True) for op in parsed_line['operands']]}),
setvar("line_template", ([*parsed_line.keys()][0], *map(type, [*parsed_line.values()][0]))),
print(line_template),
setvar("generated_opcode_map", generate_opcode_map(opcode_typemap, opcode_function_map)),
sys.exit("error: operand type mismatch for %r" % parsed_line) if (setvar("opcode", generated_opcode_map.get(line_template, None)), opcode)[1] is None else None,
opcode(*[*parsed_line.values()][0]),
breakpoint()
)
