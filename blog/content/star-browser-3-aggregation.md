Title: Star Browser, Part 3: Aggregations and Cell Details
Date: 2012-05-12
Tags: cubes, olap
Category: cubes
Slug: star-browser-3-aggregation
Author: Stefan Urbanek
Summary: Star Browser, Part 3: Aggregations and Cell Details

<p>Last time I was talking about <a href="http://blog.databrewery.org/post/22214335636">joins and
denormalisation</a> in the Star
Browser.  This is the last part about the star browser where I will describe the aggregation and what has changed, compared to the old browser.</p>

<p>The Star Browser is new aggregation browser in for the Cubes – lightweight
Python OLAP Framework. Next version v0.9 will be released next week.</p>

<h1>Aggregation</h1>

<p><em>sum</em> is not the only aggregation. The new browser allows to have other
aggregate functions as well, such as <em>min</em>, <em>max</em>.</p>

<p>You can specify the aggregations for each measure separately:</p>

<pre class="prettyprint">
{
    "name": "amount",
    "aggregations": ["sum", "min", "max"]
}
</pre>

<p>The resulting aggregated attribute name will be constructed from the measure
name and aggregation suffix, for example the mentioned <em>amount</em> will have
three aggregates in the result: <code>amount_sum</code>, <code>amount_min</code> and <code>amount_max</code>.</p>

<p>Source code reference: <em>see StarQueryBuilder.aggregations_for_measure</em></p>

<h2>Aggregation Result</h2>

<p>Result of aggregation is a structure containing: <code>summary</code> - summary for the
aggregated cell, <code>drilldown</code> - drill down cells, if was desired, and
<code>total_cell_count</code> - total cells in the drill down, regardless of pagination.</p>

<h2>Cell Details</h2>

<p>When we are browsing the cube, the cell provides current browsing context. For
aggregations and selections to happen, only keys and some other internal
attributes are necessary. Those can not be presented to the user though. For
example we have geography path (<code>country</code>, <code>region</code>) as <code>['sk', 'ba']</code>,
however we want to display to the user <code>Slovakia</code> for the country and
<code>Bratislava</code> for the region. We need to fetch those values from the data
store.  Cell details is basically a human readable description of the current
cell.</p>

<p>For applications where it is possible to store state between aggregation
calls, we can use values from previous aggregations or value listings. Problem
is with web applications - sometimes it is not desirable or possible to store
whole browsing context with all details. This is exact the situation where
fetching cell details explicitly might come handy.</p>

<p>Note: The Original browser added cut information in the summary, which was ok
when only point cuts were used. In other situations the result was undefined
and mostly erroneous.</p>

<p>The cell details are now provided separately by method
<code>AggregationBrowser.cell_details(cell)</code> which has Slicer HTTP equivalent
<code>/details</code> or <code>{"query":"detail", ...}</code> in <code>/report</code> request. The result is
a list of</p>

<p>For point cuts, the detail is a list of dictionaries for each level. For
example our previously mentioned path <code>['sk', 'ba']</code> would have details
described as:</p>

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

<p>You might have noticed the two redundant keys: <code>_key</code> and <code>_label</code> - those
contain values of a level key attribute and level label attribute
respectively. It is there to simplify the use of the details in presentation
layer, such as templates. Take for example doing only one-dimensional
browsing and compare presentation of &#8220;breadcrumbs&#8221;:</p>

<pre class="prettyprint">
labels = [detail["_label"] for detail in cut_details]
</pre>

<p>Which is equivalent to:</p>

<pre class="prettyprint">
levels = dimension.hierarchy.levels()
labels = []
for i, detail in enumerate(cut_details):
    labels.append(detail[level[i].label_attribute.full_name()])
</pre>

<p>Note that this might change a bit: either full detail will be returned or just
key and label, depending on an option argument (not yet decided).</p>

<h2>Pre-aggregation</h2>

<p>The Star Browser is being created with SQL pre-aggregation in mind. This is
not possible in the old browser, as it is not flexible enough. It is planned
to be integrated when all basic features are finished.</p>

<p>Proposed access from user&#8217;s perspective will be through configuration options:
<code>use_preaggregation</code>, <code>preaggregation_prefix</code>, <code>preaggregation_schema</code> and
a method for cube pre-aggregation will be available through the slicer tool.</p>

<h1>Summary</h1>

<p>The new browser has better internal structure resulting in increased
flexibility for future extensions. It fixes not so good architectural
decisions of the old browser.</p>

<p>New and fixed features:</p>

<ul><li>direct star/snowflake schema browsing</li>
<li>improved mappings - more transparent and understandable process</li>
<li>ability to explicitly specify database schemas</li>
<li>multiple aggregations</li>
</ul><p>The new backend sources are
<a href="https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/star.py">here</a>
and the mapper is
<a href="https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/mapper.py">here</a>.</p>

<h2>To do</h2>

<p>To be done in the near future:</p>

<ul><li>DDL generator for denormalized schema, corresponding logical schema and
physical schema</li>
<li>explicit list of attributes to be selected (instead of all)</li>
<li>selection of aggregations per-request (now all specified in model are used)</li>
</ul><h1>Links</h1>

<p>See also <a href="https://github.com/Stiivi/cubes">Cubes at github</a>,
<a href="http://packages.python.org/cubes/">Cubes Documentation</a>,
<a href="http://groups.google.com/group/cubes-discuss/">Mailing List</a>
and <a href="https://github.com/Stiivi/cubes/issues">Submit issues</a>. Also there is an 
IRC channel <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on
irc.freenode.net</p>