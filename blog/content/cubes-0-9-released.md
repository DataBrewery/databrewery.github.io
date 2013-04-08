Title: Cubes 0.9 Released
Date: 2012-05-14
Tags: cubes, announcement, release
Category: cubes
Slug: cubes-0-9-released
Author: Stefan Urbanek
Summary: Cubes 0.9 Released

<p>The new version of Cubes – light-weight <a href="http://www.python.org/">Python</a> <a href="http://en.wikipedia.org/wiki/Online_analytical_processing">OLAP</a> framework – brings new StarBrowser, which we discussed in previous blog posts:</p>

<ul><li><a href="http://blog.databrewery.org/post/22119118550">mappings</a>, see also <a href="http://packages.python.org/cubes/mapping.html">documentation</a></li>
<li><a href="http://blog.databrewery.org/post/22214335636">joins and denormalization</a></li>
<li><a href="http://blog.databrewery.org/post/22904157693">aggregations and new features</a>, see also <a href="http://packages.python.org/cubes/aggregate.html">documentation</a></li>
</ul><p>The new <a href="http://packages.python.org/cubes/api/backends.html">SQL backend</a> is written from scratch, it is much cleaner, transparent, configurable and open for future extensions. Also allows direct browsing of star/snowflake schema without denormalization, therefore you can use Cubes on top of a read-only database. See <a href="http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.mapper.DenormalizedMapper">DenormalizedMapper</a> and <a href="http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.mapper.SnowflakeMapper">SnowflakeMapper</a> for more information.</p>

<p><img src="http://media.tumblr.com/tumblr_m410f6IT8G1qgmvbu.png" alt=""/></p>

<p>Just to name a few new features: <a href="http://packages.python.org/cubes/aggregate.html#aggregations-and-aggregation-result">multiple aggregated computations</a> (min, max,&#8230;), <a href="http://packages.python.org/cubes/aggregate.html#cell-details">cell details</a>, optional/configurable <a href="http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.star.SQLStarWorkspace.create_denormalized_view">denormalization</a>.</p>

<h2>Important Changes</h2>

<p>Summary of most important changes that might affect your code:</p>

<p><strong>Slicer</strong>: Change all your slicer.ini configuration files to have [workspace]
section instead of old [db] or [backend]. Depreciation warning is issued, will
work if not changed.</p>

<p><strong>Model</strong>: Change <code>dimensions</code> in <code>model</code> to be an array instead of a
dictionary. Same with <code>cubes</code>. Old style: <code>"dimensions" = { "date" = ... }</code>
new style: <code>"dimensions" = [ { "name": "date", ... } ]</code>. Will work if not
changed, just be prepared.</p>

<p><strong>Python</strong>: Use Dimension.hierarchy() instead of Dimension.default_hierarchy.</p>

<h2>New Features</h2>

<ul><li>slicer_context() - new method that holds all relevant information from 
configuration. can be reused when creating tools that work in connected
database environment</li>
<li>added Hierarchy.all_attributes() and .key_attributes()</li>
<li>Cell.rollup_dim() - rolls up single dimension to a specified level. this might
later replace the Cell.rollup() method</li>
<li>Cell.drilldown() - drills down the cell</li>
<li>create_workspace(backend,model, **options) - new top-level method for creating a workspace by specifying backend name. Easier to create browsers (from
possible browser pool) programmatically. The backend name might be full
module name path or relative to the cubes.backends, for example
<code>sql.star</code> for new or <code>sql.browser</code> for old SQL browser.</li>
<li><p>get_backend() - get backend by name</p></li>
<li><p>AggregationBrowser.cell_details(): New method returning values of attributes
representing the cell. Preliminary implementation, return value might
change.</p></li>
<li><p>AggregationBrowser.cut_details(): New method returning values of attributes
representing a single cut. Preliminary implementation, return value might
change.</p></li>
<li><p>Dimension.validate() now checks whether there are duplicate attributes</p></li>
<li>Cube.validate() now checks whether there are duplicate measures or details</li>
</ul><p><strong>SQL backend:</strong></p>

<ul><li>new <a href="http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.star.StarBrowser">StarBrowser</a> implemented:

<ul><li>StarBrowser supports snowflakes or denormalization (optional)</li>
<li>for snowflake browsing no write permission is required (does not have to
be denormalized)</li>
</ul></li>
<li>new <a href="http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.mapper.DenormalizedMapper">DenormalizedMapper</a> for mapping logical model to denormalized view</li>
<li>new <a href="http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.mapper.SnowflakeMapper">SnowflakeMapper</a> for mapping logical model to a snowflake schema</li>
<li>ddl_for_model() - get schema DDL as string for model</li>
<li>join finder and attribute mapper are now just Mapper - class responsible for
finding appropriate joins and doing logical-to-physical mappings</li>
<li>coalesce_attribute() - new method for coalescing multiple ways of describing
a physical attribute (just attribute or table+schema+attribute)</li>
<li>dimension argument was removed from all methods working with attributes
(the dimension is now required attribute property)</li>
<li>added create_denormalized_view() with options: materialize, create_index,
keys_only</li>
</ul><p><strong>Slicer tool/server:</strong></p>

<ul><li>slicer ddl - generate schema DDL from model</li>
<li>slicer test - test configuration and model against database and report list 
of issues, if any</li>
<li>Backend options are now in [workspace], removed configurability of custom
backend section. Warning are issued when old section names [db] and
[backend] are used </li>
<li>server responds to /details which is a result of
AggregationBrowser.cell_details()</li>
</ul><p><strong>Examples:</strong></p>

<ul><li>added simple Flask based web example - dimension aggregation browser</li>
</ul><h2>Changes</h2>

<ul><li>in Model: dimension and cube dictionary specification during model
initialization is depreciated, list should be used (with explicitly
mentioned attribute &#8220;name&#8221;) &#8212; <strong>important</strong></li>
<li><strong>important</strong>: Now all attribute references in the model (dimension
attributes, measures, &#8230;) are required to be instances of Attribute() and
the attribute knows it&#8217;s dimension</li>
<li>removed <code>hierarchy</code> argument from <code>Dimension.all_attributes()</code> and <code>.key_attributes()</code></li>
<li>renamed builder to denormalizer</li>
<li>Dimension.default_hierarchy is now depreciated in favor of
Dimension.hierarchy() which now accepts no arguments or argument None -
returning default hierarchy in those two cases</li>
<li>metadata are now reused for each browser within one workspace - speed
improvement.</li>
</ul><h2>Fixes</h2>

<ul><li>Slicer version should be same version as Cubes: Original intention was to
have separate server, therefore it had its own versioning. Now there is no
reason for separate version, moreover it can introduce confusion.</li>
<li>Proper use of database schema in the Mapper</li>
</ul><h2>Links</h2>

<p>Sources can be found on <a href="https://github.com/Stiivi/cubes">github</a>.
Read the <a href="http://packages.python.org/cubes/">documentation</a>.</p>

<p>Join the <a href="http://groups.google.com/group/cubes-discuss">Google Group</a> for discussion, problem solving and announcements.</p>

<p>Submit issues and suggestions <a href="https://github.com/Stiivi/cubes/issues">on github</a></p>

<p>IRC channel <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on irc.freenode.net</p>

<p>If you have any questions, comments, requests, do not hesitate to ask.</p>