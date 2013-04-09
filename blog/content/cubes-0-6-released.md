Title: Cubes 0.6 released
Date: 2011-04-25
Tags: announcement, cubes, olap
Category: announcement
Slug: cubes-0-6-released
Author: Stefan Urbanek
Summary: Cubes 0.6 released

<p>New version of Cubes - <em>Python OLAP framework and server</em> - was released.</p>

<p>Cubes is a framework for:</p>

<ul><li>Online Analytical Processing - OLAP, mostly relational DB based - ROLAP</li>
<li>multidimensional analysis</li>
<li><p>star and snowflake schema denormalisation</p></li>
<li><p>Source: <a href="https://bitbucket.org/Stiivi/cubes">https://bitbucket.org/Stiivi/cubes</a></p></li>
<li>Documentation: <a href="http://packages.python.org/cubes">http://packages.python.org/cubes</a></li>
<li>Python Package page: <a href="http://pypi.python.org/pypi/cubes">http://pypi.python.org/pypi/cubes</a></li>
</ul><h2>Notable changes:</h2>

<ul><li>added &#8216;details&#8217; to <a href="http://packages.python.org/cubes/model.html#cubes">cube metadata</a> - attributes that might contain fact details which are not relevant to aggregation, but might be interesting when displaying facts (such as contract name or notes)</li>
<li>added ordering of facts in aggregation browser</li>
</ul><h2>SQL</h2>

<ul><li><a href="http://packages.python.org/cubes/api/backends.html#cubes.backends.SQLDenormalizer">SQL denormalizer</a> can now, by request, automatically add indexes to level key columns</li>
<li>one detail table can be used more than once in SQL denomralizer (such as an organisation for both -  supplier and requestor), added key <code>alias</code> to <code>joins</code> in model description, see <a href="http://packages.python.org/cubes/model.html#joins">joins documentation</a> for more information.</li>
</ul><h2>Slicer server</h2>

<ul><li>added <code>log</code> a and <code>log_level</code> <a href="http://packages.python.org/cubes/server.html#configuration">configuration options</a> (under <code>[server]</code>)</li>
<li>added <code>format=</code> parameter to <code>/facts</code>, accepts <code>json</code> and <code>csv</code></li>
<li>added <code>fields=</code> parameter to <code>/facts</code> - comma separated list of returned fields in CSV (see <a href="http://packages.python.org/cubes/server.html#api">API</a>)</li>
<li>limit number of facts returned in JSON (configurable by <code>json_record_limit</code> in <code>[server]</code> section), CSV can return whole dataset and will do it iteratively (we do not want to consume all of our memory, do we?)</li>
</ul><p>Also many bugs were fixed, including localization in fact(s) retrieval and pagination. Sharing of single SQLAlchemy engine and model within server thread was added for performance reasons.</p>

<p>Enjoy.</p>