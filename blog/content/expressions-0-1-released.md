Title: Introducing Expressions 0.1 for Python
Date: 2013-08-02
Tags: announcement, release, expressions
Category: announcement
Slug: python-expressions-0-1-released
Author: Stefan Urbanek
Summary: Expressions 0.1 for Python Released

Expressions is a lightweight arithmetic expression parser for creating simple
arithmetic expression compilers.

Goal is to provide minimal and understandable interface for handling
arithmetic expressions of the same grammar but slightly different dialects
(see below).  The framework will stay lightweight and it is unlikely that it
will provide any more complex gramatical constructs.

Parser is hand-written to avoid any dependencies. The only requirement is
Python 3.

Source: [github.com/Stiivi/expressions](https://github.com/Stiivi/expressions)

Features
--------

The expression is expected to be an infix expression that might contain:

* numbers and strings (literals)
* variables
* binary and unary operators
* function calls with variable number of arguments

The compiler is then used to build an object as a result of the compilation of
each of the tokens.

Dialects
--------

Grammar of the expression is fixed. Slight differences can be specified using
a `dialect` structure which contains:

* list of operators, their precedence and associativeness
* case sensitivity (currently used only for keyword based operators)

Planned options of a dialect that will be included in the future releases:

* string quoting characters (currently single `'` and double `"` quotes)
* identifier quoting characters (currently unsupported)
* identifier characters (currently `_` and alpha-numeric characters)
* decimal separator (currently `.`)
* function argument list separator (currently comma `,`)

Use
---

Intended use is embedding of customized expression evaluation into an
application.

Example uses:

* Variable checking compiler with an access control to variables.
* Unified expression language where various other backends are possible.
* Compiler for custom object structures, such as for frameworks providing
  functional-programing like interface.

How-to
------

Write a custom compiler class and implement methods:

* `compile_literal` taking a number or a string object
* `compile_variable` taking a variable name
* `compile_operator` taking a binary operator and two operands
* `compile_unary` taking an unary operator and one operand
* `compile_function` taking a function name and list of arguments

Every method receives a compilation context which is a custom object passed to
the compiler in `compile(expression, context)` call.

The following compiler re-compiles an expression back into it's original form
with optional access restriction just to certain variables specified as the
compilation context:

<pre class="prettyprint">
class AllowingCompiler(Compiler):
    def compile_literal(self, context, literal):
        return repr(literal)

    def compile_variable(self, context, variable):
        """Returns the variable if it is allowed in the `context`"""

        if context and variable not in context:
            raise ExpressionError("Variable %s is not allowed" % variable)

        return variable

    def compile_operator(self, context, operator, op1, op2):
        return "(%s %s %s)" % (op1, operator, op2)

    def compile_function(self, context, function, args):
        arglist = ", " % args
        return "%s(%s)" % (function, arglist)
</pre>

Create a compiler instance and try to get the result:

<pre class="prettyprint">
compiler = AllowingCompiler()

result = compiler.compile("a + b", context=["a", "b"])
a = 1
b = 1
print(eval(result))
</pre>

The output would be `2` as expected. The following will fail:

<pre class="prettyprint">
result = compiler.compile("a + c")
</pre>

For more examples, such as building a [SQLAlchemy structure](https://github.com/Stiivi/expressions/blob/master/examples/sqlalchemy_compiler.py)
from an expression, see the [examples folder](https://github.com/Stiivi/expressions/tree/master/examples). 


Summary
-------

Source: [github.com/Stiivi/expressions](https://github.com/Stiivi/expressions)

If you have any questions, comments, requests, do not hesitate to ask.
