Title: Cubes 0.9.1: Ranges, denormalization and query cell
Date: 2012-05-29
Tags: announcement, release, cubes, olap
Category: announcement
Slug: cubes-0-9-1-ranges-denormalization-query-cell
Author: Stefan Urbanek
Summary: Cubes 0.9.1: Ranges, denormalization and query cell

<p>The new minor release of Cubes – light-weight <a href="http://www.python.org/">Python</a>
<a href="http://en.wikipedia.org/wiki/Online_analytical_processing">OLAP</a> framework –
brings range cuts,
<a href="http://packages.python.org/cubes/slicer.html#denormalize">denormalization</a>
with the slicer tool and cells in <code>/report</code> query, together with fixes and
important changes.</p>

<p>See the second part of this post for the full list.</p>

<h2>Range Cuts</h2>

<p>Range cuts were implemented in the SQL Star Browser. They are used as follows:</p>

<p>Python:</p>

<pre class="prettyprint">
cut = RangeCut("date", [2010], [2012,5,10])
cut_hi = RangeCut("date", None, [2012,5,10])
cut_low = RangeCut("date", [2010], None)
</pre>

<p>To specify a range in slicer server where keys are sortable:</p>

<pre class="prettyprint lang-html">
    http://localhost:5000/aggregate?cut=date:2004-2005
    http://localhost:5000/aggregate?cut=date:2004,2-2005,5,1
</pre>

<p>Open ranges:</p>

<pre class="prettyprint lang-html">
    http://localhost:5000/aggregate?cut=date:2010-
    http://localhost:5000/aggregate?cut=date:2004,1,1-
    http://localhost:5000/aggregate?cut=date:-2005,5,10
    http://localhost:5000/aggregate?cut=date:-2012,5
</pre>

<h2>Denormalization with slicer Tool</h2>

<p>Now it is possible to denormalize tour data with the slicer tool. You do not
have to denormalize using python script. Data are denormalized in a way how
denormalized browser would expect them to be. You can tune the process using
command line switches, if you do not like the defaults.</p>

<p>Denormalize all cubes in the model:</p>

<pre class="prettyprint lang-bash">
$ slicer denormalize slicer.ini
</pre>

<p>Denormalize only one cube::</p>

<pre class="prettyprint lang-bash">
$ slicer denormalize -c contracts slicer.ini
</pre>

<p>Create materialized denormalized view with indexes::</p>

<pre class="prettyprint lang-bash">
$ slicer denormalize --materialize --index slicer.ini
</pre>

<p>Example <code>slicer.ini</code>:</p>

<pre class="prettyprint">
[workspace]
denormalized_view_prefix = mft_
denormalized_view_schema = denorm_views

# This switch is used by the browser:
use_denormalization = yes
</pre>

<p>For more information see <a href="http://packages.python.org/cubes/slicer.html#denormalize">Cubes slicer tool documentation</a></p>

<h2>Cells in Report</h2>

<p>Use <code>cell</code> to specify all cuts (type can be <code>range</code>, <code>point</code> or <code>set</code>):</p>

<pre class="prettyprint">
{
    "cell": [
        {
            "dimension": "date",
            "type": "range",
            "from": [2010,9],
            "to": [2011,9]
        }
    ],
    "queries": {
        "report": {
            "query": "aggregate",
            "drilldown": {"date":"year"}
        }
    }
}
</pre>

<p>For more information see the <a href="http://packages.python.org/cubes/server.html#reports">slicer server
documentation</a>.</p>

<h2>New Features</h2>

<ul><li>cut_from_string(): added parsing of range and set cuts from string;
introduced requirement for key format: Keys should now have format
&#8220;alphanumeric character or underscore&#8221; if they are going to be converted to
strings (for example when using slicer HTTP server)</li>
<li>cut_from_dict(): create a cut (of appropriate class) from a dictionary
description</li>
<li>Dimension.attribute(name): get attribute instance from name</li>
<li>added exceptions: CubesError, ModelInconsistencyError, NoSuchDimensionError,
NoSuchAttributeError, ArgumentError, MappingError, WorkspaceError and
BrowserError</li>
</ul><p><em>StarBrowser:</em></p>

<ul><li>implemented <em>RangeCut</em> conditions</li>
</ul><p><em>Slicer Server:</em></p>

<ul><li><code>/report</code> JSON now accepts <code>cell</code> with full cell description as dictionary,
overrides URL parameters</li>
</ul><p><em>Slicer tool:</em></p>

<ul><li><code>denormalize</code> option for (bulk) denormalization of cubes (see the the slicer
documentation for more information)</li>
</ul><h2>Changes</h2>

<ul><li><strong>important:</strong> all <code>/report</code> JSON requests should now have queries wrapped in the key
<code>queries</code>. This was originally intended way of use, but was not correctly
implemented. A descriptive error message is returned from the server if the
key <code>queries</code> is not present. Despite being rather a bug-fix, it is listed
here as it requires your attention for possible change of your code.</li>
<li>warn when no backend is specified during slicer context creation</li>
</ul><h2>Fixes</h2>

<ul><li>Better handling of missing optional packages, also fixes #57 (now works
without slqalchemy and without werkzeug as expected)</li>
<li>see change above about <code>/report</code> and <code>queries</code></li>
<li>push more errors as JSON responses to the requestor, instead of just failing
with an exception</li>
</ul><h2>Links</h2>

<p>Sources can be found on <a href="https://github.com/Stiivi/cubes">github</a>.
Read the <a href="http://packages.python.org/cubes/">documentation</a>.</p>

<p>Join the <a href="http://groups.google.com/group/cubes-discuss">Google Group</a> for discussion, problem solving and announcements.</p>

<p>Submit issues and suggestions <a href="https://github.com/Stiivi/cubes/issues">on github</a></p>

<p>IRC channel <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on irc.freenode.net</p>

<p>If you have any questions, comments, requests, do not hesitate to ask.</p>