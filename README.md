# Jai ![Pytest](https://img.shields.io/github/workflow/status/jakeroggenbuck/jai/pytest?style=for-the-badge)
Our entry to the [langjam](https://github.com/langjam/jam0001)

![image](https://user-images.githubusercontent.com/35516367/130336716-99aa86e5-3f79-4081-b8fa-6a133ca90e87.png)

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

![image](https://user-images.githubusercontent.com/35516367/130384789-ab1589f9-755f-411c-bda7-c9c8344aae7a.png)

# Syntax
## Variable
```c
type variable;
type variable = value;
```

## Functions
```c
fn myfunc(int num) -> int {
	return num + 10;
}
```

# Types
| Name | details    |
|------|------------|
| int  | an integer |
| str  | a string   |
