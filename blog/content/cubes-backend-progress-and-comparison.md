Title: Cubes Backend Progress and Comparison
Date: 2012-04-29
Tags: cubes, sql
Category: cubes
Slug: cubes-backend-progress-and-comparison
Author: Stefan Urbanek
Summary: Cubes Backend Progress and Comparison

I've been working on a new SQL backend for cubes called StarBrowser. Besides
new features and fixes, it is going to be more polished and maintainable. 

Current Backend Comparison
==========================

In the following table you can see comparison of backends (or rather
aggregation browsers). Current backend is `sql.browser` which reqiures
denormalized table as a source. Future preferred backend will be `sql.star`.

<iframe width="500" height="300" frameborder="0" src="https://docs.google.com/spreadsheet/pub?key=0AsH8n-1Zd5PadGxpVDAxdDhVNHdrUFZkT0pJR2JZamc&amp;single=true&amp;gid=0&amp;range=a1%3Ag26&amp;output=html&amp;widget=true"></iframe>

[Document link](https://docs.google.com/spreadsheet/ccc?key=0AsH8n-1Zd5PadGxpVDAxdDhVNHdrUFZkT0pJR2JZamc) at Google Docs.

Star Browser state
==================

More detailed description with schemas and description of what is happening
behind will be published once the browser will be useable in most of the
important features (that is, no sooner than drill-down is implemented). Here
is a peek to the new browser features.

* separated attribute mapper - doing the logical-to-physical mapping. or in
  other words: knows what column in which table represents what dimension
  attribute or a measure
* more intelligent join building - uses only joins that are relevant to the
  retrieved attributes, does not join the whole star/snowflake if not necessary
* allows tables to be stored in different database schemas (previously
  everything had to be in one schema)

There is still some work to be done, including drill-down and ordering
of results.

You can try limited feature set of the browser by using `sql.star` backend
name. Do not expect much at this time, however if you find a bug, I would be
glad if report it through [github
issues](https://github.com/Stiivi/cubes/issues). The source is in the
`cubes/backends/sql/star.py` and `cubes/backends/sql/common.py` (or
[here](https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/star.py)).

New and improved
----------------

Here is a list of features you can expect (not yet fully implemented, if at
all started):

* more SQL aggregation types and way to specify what aggregations
  should be used by-default for each measure
* DDL schema generator for: denormalized table, logical model - star schema,
  physical model
* model tester - tests whether all attributes and joins are valid in the
  physical model

Also the new implementation of star browser will allow easier integration of
 pre-aggregated store (planned) and various other optimisations.
