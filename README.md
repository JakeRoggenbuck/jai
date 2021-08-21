# Jai 0.1.1
Our entry to the [langjam](https://github.com/langjam/jam0001)

# Requirements:
Rust & Python
1. Pip requirements: run 
	
	```sh
	pip install -r requirements.txt
	```

# Build instructions
1. Build the lexer crate with
	
	```sh
	maturin build
	```

2. Install lexer with 
	
	```sh
	pip install ./target/wheels/jai-0.1.1-*
	# Add a `--force-reinstall` if reinstalling
	```

# Troubleshooting
- If you get something saying `maturin command not found` after you install it via pip. Try using `python3 -m pip` to install it and `python3 -m maturin` to run it.
- If jai does not seem to change after editing the source, make sure to do the build instructions again and use `--force-reinstall`

# Test
1. Run build instructions
2. run pytest

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
| Name | details    |
|------|------------|
| int  | an integer |
| str  | a string   |

# Turning source into tokens
## Source code
```c
"returns string";
"takes str, int";
jai(name, version) {
	return "Name: " + name + " Version:" + version;
}
```

## Token stream from calling lexer.next() in a loop
```py
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
Token("Name: ", StringLiteral: 33)
Token("+", Operator: 5)
Token("name", Identifier: 31)
Token("+", Operator: 5)
Token(" Version:", StringLiteral: 33)
Token("+", Operator: 5)
Token("version", Identifier: 31)
Token(";", Semicolon: 15)
Token("}", RightBrace: 7)
Token("\n", Newline: 28)
Token("", EOF: 0)
```
