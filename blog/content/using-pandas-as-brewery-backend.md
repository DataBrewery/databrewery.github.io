Title: Using Pandas as Brewery Backend
Date: 2012-07-27
Tags: brewery, idea, rfc
Category: brewery
Slug: using-pandas-as-brewery-backend
Author: Stefan Urbanek
Summary: Using Pandas as Brewery Backend

**UPDATE:** Added info about caching.

First time I looked at [Pandas](http://pandas.pydata.org) (python data
analysis framework) I thought: that would be great backend/computation engine
for data Brewery.

To recap core principle of Brewery: it is flow based data streaming framework
with processing nodes connected by pipes. A typical node can have one or
multiple inputs and has output. Source nodes have no inputs, target nodes have
no outputs.

![](static/images/using-pandas-as-brewery-backend-brewery_concept.png)

Current brewery implementation uses one thread per node (was written in times
when Python was new to me and I did not know about GIL and stuff). Can be
considered just as prototype...

Had this idea in mind for quite a some time, however coming
from database world, the only potential implementation was through database
tables with nodes performing SQL operations on them. I was not happy by
requirement of some SQL DB server for data processing, not mentioning speed
and function set (well, ok, pandas is missing the non-numeric stuff).

Here is the draft of the idea, how to implement data transfer between nodes
in Brewery using tables. The requirements are

* follow data modeller's workflow
* do not rewrite data – I want to be able to see what was the result at each step
* have some kind of provenance (where this field comes from?)

![](static/images/using-pandas-as-brewery-backend-pandas_concept.png)

See larger image on [imgur](http://imgur.com/BXvoK).

*Table* represents a pipe: each pipe field is mapped to a table column. If node performs only field operation, then table can be shared between nodes. If node affects rows, then new table should be considered. Every "pipe" can be cached and stream can be run from the cached point, if the computation takes longer time than desired during model development process.

Pandas offers structure called [DataFrame](http://pandas.pydata.org/pandas-docs/dev/dsintro.html#dataframe), which holds data in a tabular form consisting
of series of [Series](http://pandas.pydata.org/pandas-docs/dev/dsintro.html#series) (fancier array objects). Each of the series
represents a collection of field's values for analytical/computational step.
Nodes that share same field structure and same records can share the series
which can be grouped in a table/DataFrame.

Node can:

* create completely new field structure (source node, aggregation, join, ...)
* add a field (various derive/compute nodes)
* remove a field (field filter, field replacement)

Just adding or removing a field does not affect the series, therefore nodes
can just point to series they "need". Aggregation or join nodes generate not
only new field structure, they affect number and representation of records as
well, therefore the field series differ form their respective source series
(compare: "year" in invoices and "year" in summary of invoices). For those
kind of nodes new table/DataFrame should be created.

Sampling nodes or selection nodes can generate additional Series with boolean
values based on selection. Each node can have hidden input column representing
the selection.

There are couple of things I am missing so far: DataFrame that will be a "view"
of another data frame – that is: DataFrame will not copy series, only reference them. Another feature is more custom metadata for a table column (DataFrame series), including "analytical datatype" (I will write about this later as it is not crucial in this case). They might be there, I just
did not discovered them yet.

I am not an expert in Pandas, I have just started exploring the framework. Looks
very promising for this kind of problem.
