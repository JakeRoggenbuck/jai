# Jai
Our entry to the [langjam](https://github.com/langjam/jam0001)

# Requirements:
Rust & Python
1. Pip requirements: run 
	
	```
	pip install -r requirements.txt
	```

# Build instructions
1. Build the lexer crate with
	
	```
	maturin build
	```

2. Install lexer with 
	
	```
	pip install ./target/wheels/jai-0.1.0-cp38-cp38-manylinux_2_24_x86_64.whl
	```

# Subject to change (Draft)

# Decisions
- pointers?
- char and then char array or lists?
- auto?
- first class functions?
- Should we do cruz-lang style comments with added line terminator?

# Syntax
## Variable
```c
type variable = value;
```

## Functions
```c
// First suggestion
"returns int";
"takes int, str";
myfunc() { }
```

```c
// Second suggestion
"returns int and takes int, str";
myfunc() { }
```

## Comment
```c
"this is a comment";
```

# Types
| Name | details                      |
|------|------------------------------|
| int  | an integer                   |
| char | a character                  |

# Debated
| Name       | details                                      |
|------------|----------------------------------------------|
| auto       | automatically determins type                 |
| str        | either a collection of char or it's own type |
| bool       | a true or false value                        |
| list       | a collection of any type                     |
| key: value | a key value hash                             |


# Turning source into tokens
## Source code
```c
"returns string";
"takes str, int";
jai(name, version) {
	return "This lang is called " + name + " and we are on version: " + version;
}
```

## Token stream from calling lexer.next() in a loop
```
Token("returns string", StringLiteral: 33)
Token(";", Semicolon: 15)
Token("takes str, int", StringLiteral: 33)
Token(";", Semicolon: 15)
Token("jai", Identifier: 31)
Token("(", LeftParen: 10)
Token("name", Identifier: 31)
Token(",", Comma: 13)
Token("version", Identifier: 31)
Token(")", RightParen: 11)
Token("{", LeftBrace: 6)
Token("return", Return: 35)
Token("This lang is called ", StringLiteral: 33)
Token("+", Operator: 5)
Token("name", Identifier: 31)
Token("+", Operator: 5)
Token(" and we are on version: ", StringLiteral: 33)
Token("+", Operator: 5)
Token("version", Identifier: 31)
Token(";", Semicolon: 15)
Token("}", RightBrace: 7)
Token("\n", Newline: 28)
Token("", EOF: 0)
```
