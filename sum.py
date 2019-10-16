inf = '∞'

class expression:

    def __init__(self, text, *variables):
        self.text = text
        self.variables = variables

    def do_operation(a, b, operator):
        variables = set()
        if isinstance(a, expression):
            variables.add(a.variables)
        if isinstance(b, expression):
            variables.add(b.variables)
        return expression(
            f'({a}{operator}{b})',
            *variables
        )

    operators = {
        '+': 'add',
        '-': 'sub',
        '*': 'mul',
        '/': 'truediv',
        '**': 'pow',
        '//': 'div',
    }
    for operator, funcname in operators.items():
        locals()[f'__{funcname}__'] = (lambda _operator: lambda self, other: expression.do_operation(self, other, _operator))(operator)
        locals()[ f'__r{funcname}__'] = (lambda _operator: lambda self, other: expression.do_operation(other, self, _operator))(operator)

    def __str__(self):
        return self.text

class sum_obj:
    
    def __init__(self):
        from string import ascii_lowercase
        globals().update(
            {c: expression(c, c) for c in ascii_lowercase}
        )

    def __ror__(self, other):
        self.variables = {}
        self.count = 10_000 if other == inf else other
        return self

    def __call__(self, func):
        self.func = func
        return self

    def __setattr__(self, key, value):
        if len(key) == 1:
            
            s = 0
            for i in range(self.count):
                s += eval(str(self.func), globals(), {key: value+i})
            print(s)

        else:
            super().__setattr__(key, value)

Σ = sum_obj()



(   '∞'                   \
|    Σ (  1/(2**i)  )     \
).  i=1                   \
