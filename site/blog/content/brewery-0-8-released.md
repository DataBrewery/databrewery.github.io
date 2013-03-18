Title: Brewery 0.8 Released
Date: 2012-04-04
Tags: brewery, release, announcement
Category: brewery
Slug: brewery-0-8-released
Author: Stefan Urbanek
Summary: Brewery 0.8 Released

<p>I&#8217;m glad to announce new release of <a href="https://github.com/Stiivi/brewery">Brewery</a> – stream based data auditing and analysis framework for Python.</p>

<p>There are quite a few updates, to mention the notable ones:</p>

<ul><li>new <code>brewery</code> <a href="http://packages.python.org/brewery/tools.html#brewery">runner</a> with commands <code>run</code> and <code>graph</code></li>
<li>new nodes: <em>pretty printer</em> node (for your terminal pleasure), <em>generator
function</em> node</li>
<li>many CSV updates and fixes</li>
</ul><p>Added several simple <a href="https://github.com/Stiivi/brewery/tree/master/examples">how-to
examples</a>, such as:
aggregation of remote CSV, basic audit of a CSV, how to use a generator
function. Feedback and questions are welcome. I&#8217;ll help you.</p>

<p>Note that there are couple changes that break compatibility, however they can
be updated very easily. I apologize for the inconvenience, but until 1.0 the
changes might happen more frequently. On the other hand, I will try to make
them as painless as possible.</p>

<p>Full listing of news, changes and fixes is below.</p>

<h1>Version 0.8</h1>

<h2>News</h2>

<ul><li>Changed license to MIT</li>
<li>Created new brewery runner commands: &#8216;run&#8217; and &#8216;graph&#8217;:

<ul><li>&#8216;brewery run stream.json&#8217; will execute the stream</li>
<li>&#8216;brewery graph stream.json&#8217; will generate graphviz data</li>
</ul></li>
<li>Nodes: Added pretty printer node - textual output as a formatted table</li>
<li>Nodes: Added source node for a generator function</li>
<li>Nodes: added analytical type to derive field node</li>
<li>Preliminary implementation of data probes (just concept, API not decided yet
for 100%)</li>
<li>CSV: added empty_as_null option to read empty strings as Null values</li>
<li><p>Nodes can be configured with node.configure(dictionary, protected). If 
&#8216;protected&#8217; is True, then protected attributes (specified in node info) can 
not be set with this method.</p></li>
<li><p>added node identifier to the node reference doc</p></li>
<li><p>added create_logger</p></li>
<li><p>added experimental retype feature (works for CSV only at the moment)</p></li>
<li>Mongo Backend - better handling of record iteration</li>
</ul><h2>Changes</h2>

<ul><li>CSV: resource is now explicitly named argument in CSV*Node</li>
<li>CSV: convert fields according to field storage type (instead of all-strings)</li>
<li>Removed fields getter/setter (now implementation is totally up to stream
subclass)</li>
<li>AggregateNode: rename <code>aggregates</code> to <code>measures</code>, added <code>measures</code> as
public node attribute</li>
<li>moved errors to brewery.common</li>
<li>removed <code>field_name()</code>, now str(field) should be used</li>
<li>use named blogger &#8216;brewery&#8217; instead of the global one</li>
<li>better debug-log labels for nodes (node type identifier + python object ID)</li>
</ul><p><strong>WARNING:</strong> Compatibility break:</p>

<ul><li>depreciate <code>__node_info__</code> and use plain <code>node_info</code> instead</li>
<li><code>Stream.update()</code> now takes nodes and connections as two separate arguments</li>
</ul><h2>Fixes</h2>

<ul><li>added SQLSourceNode, added option to keep ifelds instead of dropping them in 
FieldMap and FieldMapNode (patch by laurentvasseur @ bitbucket)</li>
<li>better traceback handling on node failure (now actually the traceback is
displayed)</li>
<li>return list of field names as string representation of FieldList</li>
<li>CSV: fixed output of zero numeric value in CSV (was empty string)</li>
</ul><h1>Links</h1>

<ul><li>github  <strong>sources</strong>: <a href="https://github.com/Stiivi/brewery">https://github.com/Stiivi/brewery</a></li>
<li><strong>Documentation</strong>: <a href="http://packages.python.org/brewery/">http://packages.python.org/brewery/</a></li>
<li><strong>Mailing List</strong>: <a href="http://groups.google.com/group/databrewery/">http://groups.google.com/group/databrewery/</a></li>
<li>Submit <strong>issues</strong> here: <a href="https://github.com/Stiivi/brewery/issues">https://github.com/Stiivi/brewery/issues</a></li>
<li>IRC channel: <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on irc.freenode.net</li>
</ul><p>If you have any questions, comments, requests, do not hesitate to ask.</p>