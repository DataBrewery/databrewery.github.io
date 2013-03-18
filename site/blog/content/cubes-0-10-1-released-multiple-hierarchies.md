Title: Cubes 0.10.1 Released - Multiple Hierarchies
Date: 2012-12-09
Tags: cubes, olap, release
Category: cubes
Slug: cubes-0-10-1-released-multiple-hierarchies
Author: Stefan Urbanek
Summary: Cubes 0.10.1 Released - Multiple Hierarchies

<p>Quick Summary:</p>

<ul><li>multiple hierarchies:

<ul><li>Python: <code>cut = PointCut("date", [2010,15], hierarchy='ywd')</code> (<a href="http://packages.python.org/cubes/aggregate.html#multiple-hierarchies">docs</a>)</li>
<li>Server: <code>GET /aggregate?cut=date@ywd:2010,15</code> (see <a href="http://packages.python.org/cubes/server.html">docs</a> - look for <code>aggregate</code> documentation)</li>
<li>Server drilldown: <code>GET /aggregate?drilldown=date@ywd:week</code></li>
</ul></li>
<li>added result formatters (experimental! API might change)</li>
<li>added pre-aggregations (experimental!)</li>
</ul><h2>New Features</h2>

<ul><li>added support for multiple hierarchies</li>
<li>added <code>dimension_schema</code> option to star browser - use this when you have
all dimensions grouped in a separate schema than fact table </li>
<li>added <code>HierarchyError</code> - used for example when drilling down deeper than
possible within that hierarchy</li>
<li>added result formatters: simple_html_table, simple_data_table, text_table</li>
<li>added create_formatter(formatter_type, options &#8230;)</li>
<li><code>AggregationResult.levels</code> is a new dictionary containing levels that the
result was drilled down to. Keys are dimension names, values are levels.</li>
<li><code>AggregationResult.table_rows()</code> output has a new variable <code>is_base</code> to denote
whether the row is base or not in regard to table_rows dimension.</li>
<li><p>added <code>create_server(config_path)</code> to simplify wsgi script</p></li>
<li><p>added aggregates: avg, stddev and variance (works only in databases that
support those aggregations, such as PostgreSQL)</p></li>
<li><p>added preliminary implemenation of pre-aggregation to sql worskspace:</p>

<ul><li><code>create_conformed_rollup()</code></li>
<li><code>create_conformed_rollups()</code></li>
<li><code>create_cube_aggregate()</code></li>
</ul></li>
</ul><p>Server:</p>

<ul><li>multiple drilldowns can be specified in single argument:
<code>drilldown=date,product</code></li>
<li>there can be multiple <code>cut</code> arguments that will be appended into single cell</li>
<li>added requests: <code>GET /cubes</code> and <code>GET /cube/NAME/dimensions</code></li>
</ul><h2>Changes</h2>

<ul><li><strong>Important:</strong> Changed string representation of a set cut: now using
semicolon &#8216;;&#8217; as a separator instead of a plus symbol &#8216;+&#8217;</li>
<li>aggregation browser subclasses should now fill result&#8217;s <code>levels</code> variable
with <code>coalesced_drilldown()</code> output for requested drill-down levels.</li>
<li>Moved coalesce_drilldown() from star browser to cubes.browser module to be
reusable by other browsers. Method might be renamed in the future.</li>
<li>if there is only one level (default) in a dimension, it will have same label
as the owning dimension</li>
<li>hierarchy definition errors now raise ModelError instead of generic
exception</li>
</ul><h2>Fixes</h2>

<ul><li>order of joins is preserved</li>
<li>fixed ordering bug</li>
<li>fixed bug in generating conditions from range cuts</li>
<li><code>AggregationResult.table_rows</code> now works when there is no point cut</li>
<li>get correct reference in <code>table_rows</code> - now works when simple denormalized
table is used</li>
<li>raise model exception when a table is missing due to missing join</li>
<li>search in slicer updated for latest changes</li>
<li>fixed bug that prevented using cells with attributes in aliased joined
tables</li>
</ul><h2>Links</h2>

<p>Sources can be found on <a href="https://github.com/Stiivi/cubes">github</a>.
Read the <a href="http://packages.python.org/cubes/">documentation</a>.</p>

<p>Join the <a href="http://groups.google.com/group/cubes-discuss">Google Group</a> for discussion, problem solving and announcements.</p>

<p>Submit issues and suggestions <a href="https://github.com/Stiivi/cubes/issues">on github</a></p>

<p>IRC channel <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on irc.freenode.net</p>

<p>If you have any questions, comments, requests, do not hesitate to ask.</p>