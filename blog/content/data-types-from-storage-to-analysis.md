Title: Data Types: From Storage to Analysis 
Date: 2012-08-14
Tags: brewery, data, metadata
Category: brewery
Slug: data-types-from-storage-to-analysis
Author: Stefan Urbanek
Summary: Data Types: From Storage to Analysis 

What is the data type of 10? Depends on who you are, what are you going to do with it. I would expect my software friends to say that it is an "integer". Why this information might not be sufficient or not relevant? How analysts see the data?

Storage Data Type
-----------------

If we say "data type", engineers would name types they know from typed programming languages: small integer, double precision float, character. This data type comes from how the data are stored in memory. The type specifies what operations can be done with the data stored at that particuliar place and how much memory is taken. To add two integers on an Intel processor there is an instruction called `ADD`, to add two floats there is a different instruction called `FADD` (Dear kids: this used to be on a separate chip in PCs!). To add an integer with an float, there has to be a conversion done. Database people would say `decimal`, `date` or `string`. Same as with memory data types, each type has it's allowed set of operations and size it takes in the database. They both are of one kinds of data types: _storage data types_.

_Storage data type_, as the name suggests, is used by software (compiler, database system) to know how much memory it takes to store the value of that type and to select appropriate operations (or operation variants).

Concrete vs. Generic
--------------------

The number of storage data types and their differentiation is exhausting. To name a few:

* [C language](http://en.wikipedia.org/wiki/C_data_types) has more than 25 concrete numeric types and differentiates by floatness, size and sign flag
* [PostgreSQL](http://www.postgresql.org/docs/9.1/static/datatype-numeric.html#DATATYPE-INT) has 9 numeric types, differentiates by size and floatness
* [NumPy](http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html) differentiates not only by size and sign, but also by byte order

Do I need all taht information about data type when working with data? In most cases I don't, it is information for machine, not for me as data analyst/scientist. There are cases when knowing about data types might be handy, like optimisation (for memory consumption for example) or error prevention (of some kind) by type checking in typed languages.

For simplification, some tools use generic data types and hide the concrete storage type: `integer`, `float` (or `real`), `string`, ... No storage size, no byte order. Those are low level details.

For reading the data, no input from user is required, as `short int` is integer and `double` is real. Problem with generic data types is that there might be multiple options how to store a generic `integer`. 


Analytical Data Types
---------------------

When doing data analysis I think about variable values and what I can do with them. In data analysis adding two integers or two floats is the same. It is just `a + b`. There is only one kind of addition: `+` (remember the `ADD` and `FADD`?). However, there might be numbers that adding them together will have no meaning, like adding two invoice numbers or years together.

To specify how the values should be treated during data analysis, there is another kind of data type: _analytical data type_ or also called _variable types_. They are:

**Set** (or Nominal Variable)
:   Values represent categories, like colors or contract. types. Fields of
this type might be numbers which represent for example group numbers, but have
no mathematical interpretation. For example addition of years 1989 and 2012
has no meaning.

**Ordered Set** (or Ordinal Variable)
:   Similar to set field type, but values can be ordered in a meaningful order.

**Flag** (or Binary)
:    Special case of set type where values can be one of two types, such as 1 or 0, ‘yes’ or ‘no’, ‘true’ or ‘false’.

**Discrete**
:   Set of integers - values can be ordered and one can perform arithmetic operations on them, such as: 1 apple + 2 apples = 3 apples.

**Range**
:    Numerical value, such as financial amount, temperature

The analytical data types are disstinct from storage data types. Take for example just an integer: it can be from a set without any arithmetic operations (ID, year), can be a discrete number (count of something), a flag with binary values of `40` and `50`. Integer as a set can be ordered as set of product sizes or unordered as kind of IDs or category numbers where categories are ordered by their names rather.

In addition to the mentioned data types, it is sometimes useful to specify that the tool or algorithm should just ignore a field/column/variable. For that purpose **typeless** analytical data type might be used.

Here is an example of storage and analytical data types:

![](static/images/data-types-from-storage-to-analysis-data_types.png)

The idea behind analytical data types is described for example in nice introductory data mining book [1] or also in [2]. [1] differentiates measures as interval-scaled variables and ratio-scaled variables. Interesting that [2] describes the "set", which they call "categorical variable" as "generalization of the binary in that it can take one more than two states", not the other way around.

[1] Max Bramer: [_Principles of Datamining_](http://books.google.sk/books?id=xVW7NslHNHsC&amp;lpg=PP1&amp;ots=WjUU2gy5Zn&amp;dq=principles%20of%20data%20mining&amp;hl=sk&amp;pg=PP1#v=onepage&amp;q=principles%20of%20data%20mining&amp;f=false), Springer Verlag London United 2007, p12.

[2] Jaiwen Wan and Micheline Kamber: [_Data Mining - concepts and techniques_](http://books.google.sk/books?id=AfL0t-YzOrEC&amp;lpg=PP1&amp;ots=UvWVzPetD2&amp;dq=Data%20Mining%20-%20concepts%20and%20techniques&amp;pg=PP1#v=onepage&amp;q=Data%20Mining%20-%20concepts%20and%20techniques&amp;f=false), Elsevier 2006, p392.

Keep the metadata with you
--------------------------

As data are passed through algorithms, blocks of processing code, data types (along with other relevant metadata) should be passed with them. Data types can be in some cases guessed from data stream or explicitly expressed by a user, sometimes they can be reflected (like in a database). It is good to keep them, even if sometimes it is not possible to maintain accuracy or compatibility of data types between data sources and targets.

If done right, even after couple of transformations, one can say to an analytical metadata accepting function/algorithm: "get averages of this dataset" and it will understand it as "get averages of amounts in this dataset".

Basic metadata that should be considered when creating data processing or data analysing interfaces are:

* number of fields
* field names (as analyst I rather refer by name than index, as field position might differ among source chunks sometimes)
* field order (for tabular data it is implicit, for document based databases it should be specified)
* storage data types (at least generic, concrete if available or possible)
* analytical datatype

The minimal metadata structure for a dataset relevant to both: analysts who use data and engineers who prepare data would therefore be a list of tuples: (_name_, _storage type_, _analytical type_).

Conclusion
----------

Typeless programming languages allow programmers to focus on structuring the data and remove the necessity of fiddling with physical storage implementation. Hiding concrete storage types from data analysts allows them to focus on properties of their data relevant to analysis. Less burden on mind definitely helps our thinking process.

Nevertheless, there are more kinds...

Links
-----

Data Brewery [documentation](http://packages.python.org/brewery/metadata.html) of metadata structures.
