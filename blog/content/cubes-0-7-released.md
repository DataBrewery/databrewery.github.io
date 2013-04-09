Title: Cubes 0.7 released
Date: 2011-09-29
Tags: announcement, release, cubes, olap
Category: announcement
Slug: cubes-0-7-released
Author: Stefan Urbanek
Summary: Cubes 0.7 released

<p>I am happy to announce another release of Cubes - Python OLAP framework for multidimensional data aggregation and browsing.</p>

<p>This release, besides some new features, renames Cuboid to more appropriate Cell. This introduces backward python API incompatibility.</p>

<p>Main <strong>source repository</strong> has changed to Github <a href="https://github.com/Stiivi/cubes">https://github.com/Stiivi/cubes</a></p>

<h2>Changes</h2>

<ul><li>Class &#8216;Cuboid&#8217; was renamed to more correct &#8216;Cell&#8217;. &#8216;Cuboid&#8217; is a part of cube with subset of dimensions.</li>
<li>all APIs with &#8216;cuboid&#8217; in their name/arguments were renamed to use &#8216;cell&#8217; instead</li>
<li>Changed initialization of model classes: Model, Cube, Dimension, Hierarchy, Level to be more &#8220;pythony&#8221;: instead of using initialization dictionary, each attribute is listed as parameter, rest is handled from variable list of key word arguments</li>
<li>Improved handling of flat and detail-less dimensions (dimensions represented just by one attribute which is also a key)</li>
</ul><p>Model Initialization Defaults:</p>

<ul><li>If no levels are specified during initialization, then dimension name is considered flat, with single attribute.</li>
<li>If no hierarchy is specified and levels are specified, then default hierarchy will be created from order of levels</li>
<li>If no levels are specified, then one level is created, with name <code>default</code> and dimension will be considered flat</li>
</ul><p><em>Note</em>: This initialization defaults might be moved into a separate utility function/class that will populate incomplete model (see <a href="https://github.com/Stiivi/cubes/issues/8">Issue #8</a> )</p>

<h2>New features</h2>

<p>Slicer server:</p>

<ul><li>changed to handle multiple cubes within model: you have to specify a cube for /aggregate, /facts,&#8230; in form: /cube/<cube_name>/<browser_action/></browser_action></cube_name></li>
<li>reflect change in configuration: removed <code>view</code>, added <code>view_prefix</code> and <code>view_suffix</code>, the cube view name will be constructed by concatenating <code>view prefix</code> + <code>cube name</code> + <code>view suffix</code></li>
<li>in aggregate drill-down: explicit dimension can be specified with drilldown=dimension:level, such as:
date:month</li>
</ul><p>This change is considered final and therefore we can mark it is as API version 1.</p>

<p>Links:</p>

<ul><li><strong>Issues:</strong> <a href="https://github.com/Stiivi/cubes/issues">https://github.com/Stiivi/cubes/issues</a></li>
<li><strong>Documentation:</strong> <a href="http://packages.python.org/cubes/">http://packages.python.org/cubes/</a></li>
</ul><p>If you have any questions, comments, requests, do not hesitate to ask.</p>