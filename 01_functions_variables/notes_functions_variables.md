# Programming with Python

David J. Malan

## Introduction to programming with Python

* Functions & Variables
* Condtionals
* Loops
* Exceptions
* Libraries
* Unit Tests
* File I/O
* Regular Expressions
* Objet-Oriented Programming

### Functions, Variables

Type `code hello.py` and write `print("hello, world")

* Python is also a program. It's an interpreter.

You're written your very first program with Python!

* Functions : Kind of actions or words the program already knows an can use elsewhere.
* Arguments : input to a function that somehow influence its behavior.
* "side effect" in programming (like displaying "hello", "world" words on the screen).
* Bugs : a mistake in a program that can take many forms. Mistakess that are problem for you to solve.

Removing a parenthesis and explaining exception (illustration of a bug, SyntaxError: '(' was never closed).

Right tool for the right job. VSCode, colors, not Microsoft Word.

* `input()` function asking name and modifying print('hello, world")
* hardcode the answer to explain you can return values
* variables : stores a value. A number, a word,... inside a computer, inside your own program.
* `=` sign does mean equality but more "assignment"; you want to assign to the left, the value returned by the function to the right.
Delibarated written "name" in the string to show off it's not working
write it on 2 lines then explain he solved the problem, but that's not perfect and can be written on  1 line. Now introducing new concepts
* comments : juste there for you, your colleague,... `#`, multi-line : `"""` but this can have others meanings.
* pseudocode : stucturing your to do list, split it on smaller taks.
One way to solve the multi-line problem. Precising that there always are many ways to solve a problem.
About strings in print : `,` in function vs comma in the string.
* string : a sequence of texts. Technical term : `str` (type of data in program)
Introduces docs.python.org
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/functions.html#print
`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
In the documentations, arguments are often calls "parameters".
`*objects` menans that the function can take any numbers of objects.
`sep=' '` default value of the separator is a space char.
`end='\n'` means "new line" he's changing chars and show up what is does with examples (without spaces, with question mark,...).
NOTE/TIP : Doc is using simple quotes, but you can use both
`file=sys.stdout`
`flush=False`
Parameters are optionnal. (ndlr. verify if its always true, not sure I noted the right thing).
Question about quotes inside quote : he's showing that we can escape.

Introduces format string, f-string.

Introducting strip() showing we can input our name with multile spaces before and that might not be adequate to trust the user.

```
# Remove whitespace from str
name = name.strip()
```

Introducting `capitalize()`.

Introducing UP arrow key to avoir retype.

Tells we can do all in one line so we trade 8 lines of code vs 1 and says that it might be better so we now have less to read and we start to solve other problems

`first, last = name.split(" ")`

#### Another type of data : int

Numbers.

Symbols : + - * / %

`%` : modulo operator.

Python supports interactive mode
Shows interactive mode and type 1+1
print("hello, world")

Introduces cancatenation and shows that input does not take int we type as integers but string and that the plus operator concatenane which is suprising for newcomers.


Introduces tab to continue and autocomplete to get the full script name.

Introduces function nesting with `int(input("What's x?"))`.

#### Another type of data : float

`round()`
https://doc.python.org/3/library/functions.html#round
`round(number, ndigits=None)`

z = round(x + y)

Introduces int(), float(), round()

and...

this format string trick : `print(f"{z:,}")`


`print(f"{z:.2f}")` is the f-string approach of :
`z = round(x / y, 2)` then `print(z)`

### Functions

#### def

`def` is short for 'define'.

scope : refers to variable only existing in the context where you define it.

return :
