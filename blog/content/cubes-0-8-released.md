Title: Cubes 0.8 Released
Date: 2012-03-09
Tags: cubes, announcement, olap
Category: cubes
Slug: cubes-0-8-released
Author: Stefan Urbanek
Summary: Cubes 0.8 Released

<p>Another minor release of Cubes - Light Weight Python OLAP framework is out. Main change is that backend is no longer hard-wired in the <a href="http://packages.python.org/cubes/server.html">Slicer server</a> and can be selected through configuration file.</p>

<p>There were lots of documentation changes, for example <a href="http://packages.python.org/cubes/api/index.html">the reference</a> was separated from the rest of docs. <a href="https://github.com/Stiivi/cubes/tree/master/examples/hello_world">Hello World! example</a> was added.</p>

<p>The news, changes and fixes are:</p>

<h2>New Features</h2>

<ul><li>Started writing <a href="https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/star_browser.py">StarBrowser</a> - another SQL aggregation browser with different 
approach (see code/docs)</li>
</ul><p><a href="http://packages.python.org/cubes/server.html#configuration">Slicer Server</a>:</p>

<ul><li>added configuration option <code>modules</code> under <code>[server]</code> to load additional 
modules</li>
<li>added ability to specify backend module</li>
<li>backend configuration is in [backend] by default, for SQL it stays in [db]</li>
<li>added server config option for default <code>prettyprint</code> value (useful for 
demontration purposes)</li>
</ul><p><a href="http://packages.python.org/cubes">Documentation</a>:</p>

<ul><li><a href="http://blog.databrewery.org/post/18142294411">Changed license</a> to MIT + small addition. Please refer to the LICENSE file.</li>
<li>Updated documentation - added missing parts, made reference more readable, 
moved class and function reference docs from descriptive part to reference 
(API) part.</li>
<li>added backend documentation </li>
<li>Added &#8220;<a href="https://github.com/Stiivi/cubes/tree/master/examples/hello_world">Hello World!</a>&#8221; example</li>
</ul><h2>Changed Features</h2>

<ul><li>removed default SQL backend from the server</li>
<li>moved worskpace creation into the backend module</li>
</ul><h2>Fixes</h2>

<ul><li>Fixed create_view to handle not materialized properly (thanks to deytao)</li>
<li>Slicer tool header now contains #!/usr/bin/env python</li>
</ul><h2>Links</h2>

<ul><li>github  <strong>sources</strong>: <a href="https://github.com/Stiivi/cubes">https://github.com/Stiivi/cubes</a></li>
<li><strong>Documentation</strong>: <a href="http://packages.python.org/cubes/">http://packages.python.org/cubes/</a></li>
<li><strong>Mailing List</strong>: <a href="http://groups.google.com/group/cubes-discuss">http://groups.google.com/group/cubes-discuss</a></li>
<li>Submit <strong>issues</strong> here: <a href="https://github.com/Stiivi/cubes/issues">https://github.com/Stiivi/cubes/issues</a></li>
<li>IRC channel: <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on irc.freenode.net</li>
</ul><p>If you have any questions, comments, requests, do not hesitate to ask.</p>