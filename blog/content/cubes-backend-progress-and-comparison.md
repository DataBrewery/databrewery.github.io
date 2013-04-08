Title: Cubes Backend Progress and Comparison
Date: 2012-04-29
Tags: cubes, sql
Category: cubes
Slug: cubes-backend-progress-and-comparison
Author: Stefan Urbanek
Summary: Cubes Backend Progress and Comparison

<p>I&#8217;ve been working on a new SQL backend for cubes called StarBrowser. Besides
new features and fixes, it is going to be more polished and maintainable.</p>

<h1>Current Backend Comparison</h1>

<p>In the following table you can see comparison of backends (or rather
aggregation browsers). Current backend is <code>sql.browser</code> which reqiures
denormalized table as a source. Future preferred backend will be <code>sql.star</code>.</p>

<iframe width="500" height="300" frameborder="0" src="https://docs.google.com/spreadsheet/pub?key=0AsH8n-1Zd5PadGxpVDAxdDhVNHdrUFZkT0pJR2JZamc&amp;single=true&amp;gid=0&amp;range=a1%3Ag26&amp;output=html&amp;widget=true"></iframe>

<p><a href="https://docs.google.com/spreadsheet/ccc?key=0AsH8n-1Zd5PadGxpVDAxdDhVNHdrUFZkT0pJR2JZamc">Document link</a> at Google Docs.</p>

<h1>Star Browser state</h1>

<p>More detailed description with schemas and description of what is happening
behind will be published once the browser will be useable in most of the
important features (that is, no sooner than drill-down is implemented). Here
is a peek to the new browser features.</p>

<ul><li>separated attribute mapper - doing the logical-to-physical mapping. or in
other words: knows what column in which table represents what dimension
attribute or a measure</li>
<li>more intelligent join building - uses only joins that are relevant to the
retrieved attributes, does not join the whole star/snowflake if not necessary</li>
<li>allows tables to be stored in different database schemas (previously
everything had to be in one schema)</li>
</ul><p>There is still some work to be done, including drill-down and ordering
of results.</p>

<p>You can try limited feature set of the browser by using <code>sql.star</code> backend
name. Do not expect much at this time, however if you find a bug, I would be
glad if report it through <a href="https://github.com/Stiivi/cubes/issues">github
issues</a>. The source is in the
<code>cubes/backends/sql/star.py</code> and <code>cubes/backends/sql/common.py</code> (or
<a href="https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/star.py">here</a>).</p>

<h2>New and improved</h2>

<p>Here is a list of features you can expect (not yet fully implemented, if at
all started):</p>

<ul><li>more SQL aggregation types and way to specify what aggregations
should be used by-default for each measure</li>
<li>DDL schema generator for: denormalized table, logical model - star schema,
physical model</li>
<li>model tester - tests whether all attributes and joins are valid in the
physical model</li>
</ul><p>Also the new implementation of star browser will allow easier integration of
 pre-aggregated store (planned) and various other optimisations.</p>