Title: Star Browser, Part 3: Aggregations and Cell Details
Date: 2012-05-12
Tags: cubes, olap
Category: cubes
Slug: star-browser-3-aggregation
Author: Stefan Urbanek
Summary: Star Browser, Part 3: Aggregations and Cell Details

Last time I was talking about [joins and
denormalisation](http://blog.databrewery.org/post/22214335636) in the Star
Browser.  This is the last part about the star browser where I will describe the aggregation and what has changed, compared to the old browser.

The Star Browser is new aggregation browser in for the Cubes – lightweight
Python OLAP Framework. Next version v0.9 will be released next week.

Aggregation
===========

*sum* is not the only aggregation. The new browser allows to have other
aggregate functions as well, such as *min*, *max*.

You can specify the aggregations for each measure separately:

<pre class="prettyprint">
{
    "name": "amount",
    "aggregations": ["sum", "min", "max"]
}
</pre>

The resulting aggregated attribute name will be constructed from the measure
name and aggregation suffix, for example the mentioned *amount* will have
three aggregates in the result: `amount_sum`, `amount_min` and `amount_max`.

Source code reference: *see StarQueryBuilder.aggregations_for_measure*

Aggregation Result
------------------

Result of aggregation is a structure containing: `summary` - summary for the
aggregated cell, `drilldown` - drill down cells, if was desired, and
`total_cell_count` - total cells in the drill down, regardless of pagination. 

Cell Details
------------

When we are browsing the cube, the cell provides current browsing context. For
aggregations and selections to happen, only keys and some other internal
attributes are necessary. Those can not be presented to the user though. For
example we have geography path (`country`, `region`) as ``['sk', 'ba']``,
however we want to display to the user `Slovakia` for the country and
`Bratislava` for the region. We need to fetch those values from the data
store.  Cell details is basically a human readable description of the current
cell.

For applications where it is possible to store state between aggregation
calls, we can use values from previous aggregations or value listings. Problem
is with web applications - sometimes it is not desirable or possible to store
whole browsing context with all details. This is exact the situation where
fetching cell details explicitly might come handy.

Note: The Original browser added cut information in the summary, which was ok
when only point cuts were used. In other situations the result was undefined
and mostly erroneous.

The cell details are now provided separately by method
`AggregationBrowser.cell_details(cell)` which has Slicer HTTP equivalent
``/details`` or `{"query":"detail", ...}` in `/report` request. The result is
a list of

For point cuts, the detail is a list of dictionaries for each level. For
example our previously mentioned path ``['sk', 'ba']`` would have details
described as:

<pre class="prettyprint">
[
    {
        "geography.country_code": "sk",
        "geography.country_name": "Slovakia",
        "geography.something_more": "..."
        "_key": "sk",
        "_label": "Slovakia"
    },
    {
        "geography.region_code": "ba",
        "geography.region_name": "Bratislava",
        "geography.something_even_more": "...",
        "_key": "ba",
        "_label": "Bratislava"
    }
]
</pre>
    
You might have noticed the two redundant keys: `_key` and `_label` - those
contain values of a level key attribute and level label attribute
respectively. It is there to simplify the use of the details in presentation
layer, such as templates. Take for example doing only one-dimensional
browsing and compare presentation of "breadcrumbs":

<pre class="prettyprint">
labels = [detail["_label"] for detail in cut_details]
</pre>

Which is equivalent to:

<pre class="prettyprint">
levels = dimension.hierarchy.levels()
labels = []
for i, detail in enumerate(cut_details):
    labels.append(detail[level[i].label_attribute.full_name()])
</pre>

Note that this might change a bit: either full detail will be returned or just
key and label, depending on an option argument (not yet decided).

Pre-aggregation
---------------

The Star Browser is being created with SQL pre-aggregation in mind. This is
not possible in the old browser, as it is not flexible enough. It is planned
to be integrated when all basic features are finished.

Proposed access from user's perspective will be through configuration options:
`use_preaggregation`, `preaggregation_prefix`, `preaggregation_schema` and
a method for cube pre-aggregation will be available through the slicer tool.

Summary
=======

The new browser has better internal structure resulting in increased
flexibility for future extensions. It fixes not so good architectural
decisions of the old browser.

New and fixed features:

* direct star/snowflake schema browsing
* improved mappings - more transparent and understandable process
* ability to explicitly specify database schemas
* multiple aggregations

The new backend sources are
[here](https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/star.py)
and the mapper is
[here](https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/mapper.py).

To do
-----

To be done in the near future:

* DDL generator for denormalized schema, corresponding logical schema and
  physical schema
* explicit list of attributes to be selected (instead of all)
* selection of aggregations per-request (now all specified in model are used)

Links
=====

See also [Cubes at github](https://github.com/Stiivi/cubes),
[Cubes Documentation](http://packages.python.org/cubes/),
[Mailing List](http://groups.google.com/group/cubes-discuss/)
and [Submit issues](https://github.com/Stiivi/cubes/issues). Also there is an 
IRC channel [#databrewery](irc://irc.freenode.net/#databrewery) on
irc.freenode.net
