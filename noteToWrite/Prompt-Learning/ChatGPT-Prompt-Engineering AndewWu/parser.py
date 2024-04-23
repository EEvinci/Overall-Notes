from lark import Lark, Transformer, v_args

json_grammar = """
    start: value
    value: object
         | array
         | string
         | "true" -> true
         | "false" -> false
         | "null" -> null
    array  : "[" [value ("," value)*] "]"
    object : "{" [pair ("," pair)*] "}"
    pair   : string ":" value
    string : ESCAPED_STRING
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS 
"""


class TreeToJson(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[0][1:-1]

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    def null(self, _): return None
    def true(self, _): return True
    def false(self, _): return False


json_parser = Lark(json_grammar, parser='lalr', transformer=TreeToJson())
tree = json_parser.parse('{ "name" : "John", "age" : 30, "city" : "New York"}')
print(json_parser.transform(tree))
