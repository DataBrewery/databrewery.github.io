Title: bogus 4
TextBox: box_dataobjects
Row: 2
Column: 2
Class: offset2
Type: half
Parent: index
Status: hidden

## Data Objects ##

Data object is an abstraction of a dataset. Data objects might have multiple
representations, such as SQL statement or python iterator. Data object
does not have to be backed by physical existence of data.

Principle of data object is to keep data in its natural "habitat" without
fetching them if not necessary.

## Operations ##

Data objects are processed using operations which try to operate on metadata
if possible. For example, if the data can be represented as SQL, then SQL
composition is used. This allows the best use of underlying technology
whenever it is possible.

## Pipeline ##

Data processing pipeline can be described as: 

<pre class="prettyprint">
p = Pipeline()

p.source_object("csv_source", "data.csv")
p.distinct("category")
p.pretty_print()

p.run()
</pre>

The steps are described as Python function calls, however they are just used
to construct a data processing pipeline graph. The graph is then executed by
`run()`. Different graph execution policies and contexts might be used.
