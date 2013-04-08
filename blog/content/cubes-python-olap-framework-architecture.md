Title: Cubes - Python OLAP Framework Architecture
Date: 2012-02-21
Tags: cubes, olap
Category: cubes
Slug: cubes-python-olap-framework-architecture
Author: Stefan Urbanek
Summary: Cubes - Python OLAP Framework Architecture

<p>What is inside the Cubes Python OLAP Framework? Here is a brief overview of the core modules, their purpose and functionality.</p>

<p>The lightweight framework Cubes is composed of four public modules:</p>

<p><img src="http://media.tumblr.com/tumblr_lzr33cGIx41qgmvbu.png" alt=""/></p>

<ul><li><em>model</em> - Description of data (<em>metadata</em>): dimensions, hierarchies, attributes, labels, localizations.</li>
<li><em>browser</em> - Aggregation browsing, slicing-and-dicing, drill-down.</li>
<li><em>backends</em> - Actual aggregation implementation and utility functions.</li>
<li><em>server</em> - WSGI HTTP server for Cubes</li>
</ul><h1>Model</h1>

<p>Logical model describes the data from user’s or analyst’s perspective: data how they are being measured, aggregated and reported. Model is independent of physical implementation of data. This physical independence makes it easier to focus on data instead on ways of how to get the data in understandable form.</p>

<p>Cubes model is described by:</p>

<p><img src="http://media.tumblr.com/tumblr_lzr33wXsWd1qgmvbu.png" alt=""/></p>

<ul><li>model object (<a href="http://packages.python.org/cubes/model.html#cubes.model.Model">doc</a>)</li>
<li>list of cubes</li>
<li>dimensions of cubes (they are shared with all cubes within model) (<a href="http://packages.python.org/cubes/api/cubes.html#cubes.Dimension">doc</a>) (<a href="http://packages.python.org/cubes/api/cubes.html#cubes.Dimension">doc</a>)</li>
<li>hierarchies (<a href="http://packages.python.org/cubes/api/cubes.html#cubes.Hierarchy">doc</a>) and hierarchy levels (<a href="http://packages.python.org/cubes/api/cubes.html#cubes.Level">doc</a>) of dimensions (such as <em>category-subcategory</em>, <em>country-region-city</em>)</li>
<li>optional mappings from logical model to the physical model (<a href="http://packages.python.org/cubes/model.html#attribute-mappings">doc</a>)</li>
<li>optional join specifications for star schemas, used by the SQL denormalizing backend (<a href="http://packages.python.org/cubes/model.html#joins">doc</a>)</li>
</ul><p>There is a utility function provided for loading the model from a JSON file: <code>load_model</code>.</p>

<p>The model module object are capable of being localized (see <a href="http://packages.python.org/cubes/localization.html">Model Localization</a> for more information). The cubes provides localization at the metadata level (the model) and functionality to have localization at the data level.</p>

<p>See also: <a href="http://packages.python.org/cubes/model.html">Model Documentation</a></p>

<h1>Browser</h1>

<p>Core of the Cubes analytics functionality is the aggregation browser. The <code>browser</code> module contains utility classes and functions for the browser to work.</p>

<p><img src="http://media.tumblr.com/tumblr_lzr34qlXN11qgmvbu.png" alt=""/></p>

<p>The module components are:</p>

<ul><li><strong>Cell</strong> - specification of the portion of the cube to be explored, sliced or drilled down. Each cell is specified by a set of cuts. A cell without any cuts represents whole cube.</li>
<li><strong>Cut</strong> - definition where the cell is going to be sliced through single dimension. There are three types of cuts: point, range and set.</li>
</ul><p>The types of cuts:</p>

<ul><li><strong>Point Cut</strong> - Defines one single point on a dimension where the cube is going to be sliced. The point might be at any level of hierarchy. The point is specified by &#8220;path&#8221;. Examples of point cut: <code>[2010]</code> for <em>year</em> level of Date dimension, <code>[2010,1,7]</code> for full date point.</li>
<li><strong>Range Cut</strong> - Defines two points (dimension paths) on a sortable dimension between whose the cell is going to be sliced from cube.</li>
<li><strong>Set Cut</strong> - Defines list of multiple points (dimension paths) which are going to be included in the sliced cell.</li>
</ul><p>Example of point cut effect:</p>

<p><img src="http://media.tumblr.com/tumblr_lzr35pNwxo1qgmvbu.png" alt=""/></p>

<p>The module provides couple utility functions:</p>

<ul><li><code>path_from_string</code> - construct a dimension path (point) from a string</li>
<li><code>string_from_path</code> - get a string representation of a dimension path (point)</li>
<li><code>string_from_cuts</code> and <code>cuts_from_string</code> are for conversion between string and list of cuts. (Currently only list of point cuts are supported in the string representation)</li>
</ul><p>The aggregation browser can:</p>

<ul><li>aggregate a cell (<code>aggregate(cell)</code>)</li>
<li>drill-down through multiple dimensions and aggregate (<code>aggregate(cell, drilldown="date")</code>)</li>
<li>get all detailed facts within the cell (<code>facts(cell)</code>)</li>
<li>get single fact (<code>fact(id)</code>)</li>
</ul><p>There is convenience function <code>report(cell, report)</code> that can be implemented by backend in more efficient way to get multiple aggregation queries in single call.</p>

<p>More about aggregated browsing can be found in the <a href="http://packages.python.org/cubes/api/cubes.html#aggregate-browsing">Cubes documentation</a>.</p>

<h1>Backends</h1>

<p>Actual aggregation is provided by the backends. The backend should implement aggregation browser interface.</p>

<p><img src="http://media.tumblr.com/tumblr_lzr37ayQWJ1qgmvbu.png" alt=""/></p>

<p>Cubes comes with built-in <a href="http://en.wikipedia.org/wiki/ROLAP">ROLAP</a> backend which uses SQL database through SQLAlchemy. The backend has two major components:</p>

<ul><li><em>aggregation browser</em> that works on single denormalized view or a table</li>
<li><em>SQL denormalizer</em> helper class that converts <a href="http://en.wikipedia.org/wiki/Star_schema">star schema</a> into a denormalized view or table (kind of materialisation).</li>
</ul><p>There was an attempt to write a <a href="https://github.com/Stiivi/cubes/tree/master/cubes/backends/mongo">Mongo DB backend</a>, but it does not work any more, it is included in the sources only as reminder, that there should be a mongo backend sometime in the future.</p>

<p>Anyone can write a backend. If you are interested, drop me a line.</p>

<h1>Server</h1>

<p>Cubes comes with Slicer - a WSGI HTTP OLAP server with API for most of the cubes framework functionality. The server is based on the Werkzeug framework.</p>

<p><img src="http://media.tumblr.com/tumblr_lzr37v5B6G1qgmvbu.png" alt=""/></p>

<p>Intended use of the slicer is basically as follows:</p>

<ul><li>application prepares the cell to be aggregated, drilled, listed&#8230; The <em>cell</em> might be whole cube.</li>
<li>HTTP request is sent to the server</li>
<li>the server uses appropriate aggregation browser backend (note that currently there is only one: SQL denormalized) to compute the request</li>
<li>Slicer returns a JSON reply to the application</li>
</ul><p>For more information, please refer to the Cubes <a href="http://packages.python.org/cubes/server.html">Slicer server documentation</a>.</p>

<h1>One more thing&#8230;</h1>

<p>There are plenty things to get improved, of course. Current focus is not on performance, but on achieving simple usability.</p>

<p>The Cubes sources can be found on Github: <a href="https://github.com/stiivi/cubes">https://github.com/stiivi/cubes</a> . There is also a IRC channel #databrewery on irc.freenode.net (I try to be there during late evening CET). Issues can be reported on the <a href="https://github.com/stiivi/cubes/issues?sort=created&amp;direction=desc&amp;state=open">github project page</a>.</p>

<p>If you have any questions, suggestions, recommendations, just let me know.</p>

<p><a href="http://news.ycombinator.com/item?id=3617672"><em>HackerNews Thread</em></a></p>