import re

class TablaPredectiva:
    def __init__(self):
        self.stack = []
        self.table = {
            ('E', 'alter table'): ['C', 'D'],
            ('D', 'a...z'): ['I', 'A', 'V'],
            ('I', 'a...z'): ['L', 'R'],
            ('L', 'a...z'): ['LETTER'],
            ('R', 'a...z'): ['LETTER', 'R'],
            ('R', ';'): ['EPSILON'],
            ('R', '$'): ['EPSILON'],
            ('A', 'drop column'): ['DROP_COLUMN'],
            ('C', 'alter table'): ['ALTER_TABLE'],
            ('V', 'a...z'): ['I', 'P'],
            ('P', ';'): ['SEMICOLON']
        }
        
    def parse(self, tokens):
        self.tokens = tokens
        self.stack = ['$', 'E']
        self.cursor = 0
        output = []
        
        while self.stack:
            output.append(f"Pila: {self.stack}")
            top = self.stack[-1]
            current_token = self.tokens[self.cursor][0] if self.cursor < len(self.tokens) else '$'
            
            if top == current_token:
                self.stack.pop()
                self.cursor += 1
            elif (top, current_token) in self.table:
                self.stack.pop()
                symbols = self.table[(top, current_token)]
                if symbols != ['EPSILON']:
                    for symbol in reversed(symbols):
                        self.stack.append(symbol)
            else:
                raise Exception(f"Error: No se encontró la regla en la tabla para: {top}, {current_token}")
        
        if self.cursor != len(self.tokens):
            raise Exception("Error de sintaxis: La entrada no es válida")
        
        return "\n".join(output)

def lexer(input_string):
    tokens = []
    token_specs = [
        ('ALTER_TABLE', r'alter table'),
        ('DROP_COLUMN', r'drop column'),
        ('LETTER', r'[a-z]'),
        ('SEMICOLON', r';'),
        ('IGNORE', r'[ \t\n]+'),
        ('MISMATCH', r'.'),
    ]
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
    for match in re.finditer(token_regex, input_string):
        type = match.lastgroup
        if type == 'IGNORE':
            continue
        elif type == 'MISMATCH':
            raise RuntimeError(f'Carácter no válido: {match.group(0)}')
        else:
            tokens.append((type, match.group(0)))
    return tokens

def analizar_entrada(input_string):
    try:
        tokens = lexer(input_string)
        parser = TablaPredectiva()
        estado_pila = parser.parse(tokens)  
        return f"Análisis completado con éxito.\n Pila: {estado_pila}"
    except Exception as e:
        return str(e)
