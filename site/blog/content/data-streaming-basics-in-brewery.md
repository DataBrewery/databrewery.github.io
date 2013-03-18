Title: Data Streaming Basics in Brewery
Date: 2012-04-13
Tags: brewery
Category: brewery
Slug: data-streaming-basics-in-brewery
Author: Stefan Urbanek
Summary: Data Streaming Basics in Brewery

<p>How to build and run a data analysis stream? Why streams? I am going to talk about
how to use brewery from command line and from Python scripts.</p>

<p><a href="https://github.com/Stiivi/brewery">Brewery</a> is a Python framework and a way of analysing and auditing data. Basic
principle is flow of structured data through processing and analysing nodes.
This architecture allows more transparent, understandable and maintainable
data streaming process.</p>

<p>You might want to use brewery when you:</p>

<ul><li>want to learn more about data</li>
<li>encounter unknown datasets and/or you do not know what you have in your
datasets</li>
<li>do not know exactly how to process your data and you want to play-around
without getting lost</li>
<li>want to create alternative analysis paths and compare them</li>
<li>measure data quality and feed data quality results into the data processing
process</li>
</ul><p>There are many approaches and ways how to the data analysis. Brewery brings a certain workflow to the analyst:</p>

<ol><li>examine data</li>
<li>prototype a stream (can use data sampling, not to overheat the machine)</li>
<li>see results and refine stream, create alternatives (at the same time)</li>
<li>repeat 3. until satisfied</li>
</ol><p>Brewery makes the steps 2. and 3. easy - quick prototyping, alternative
branching, comparison. Tries to keep the analysts workflow clean and understandable.</p>

<h1>Building and Running a Stream</h1>

<p>There are two ways to create a stream: programmatic in Python and command-line
without Python knowledge requirement. Both ways have two alternatives: quick
and simple, but with limited feature set. And the other is full-featured but
is more verbose.</p>

<p>The two programmatic alternatives to create a stream are: <em>basic construction</em>
and <em>&#8220;HOM&#8221;</em> or <em>forking construction</em>. The two command line ways to run a
stream: <em>run</em> and <em>pipe</em>. We are now going to look closer at them.</p>

<p><img src="http://media.tumblr.com/tumblr_m2f46vi6Po1qgmvbu.png" alt=""/></p>

<p>Note regarding Zen of Python: this does not go against &#8220;There should be one –
and preferably only one – obvious way to do it.&#8221; There is only one way: the
raw construction. The others are higher level ways or ways in different
environments.</p>

<p>In our examples below we are going to demonstrate simple linear (no branching)
stream that reads a CSV file, performs very basic audit and &#8220;pretty prints&#8221;
out the result. The stream looks like this:</p>

<p><img src="http://media.tumblr.com/tumblr_m2f49jBpOK1qgmvbu.png" alt=""/></p>

<h2>Command line</h2>

<p>Brewery comes with a command line utility <code>brewery</code> which can run streams
without needing to write a single line of python code. Again there are two
ways of stream description: json-based and plain linear pipe.</p>

<p>The simple usage is with <code>brewery pipe</code> command:</p>

<pre><code>brewery pipe csv_source resource=data.csv audit pretty_printer
</code></pre>

<p>The <code>pipe</code> command expects list of nodes and <code>attribute=value</code> pairs for node
configuration. If there is no source pipe specified, CSV on standard input is
used. If there is no target pipe, CSV on standard output is assumed:</p>

<pre><code>cat data.csv | brewery pipe audit
</code></pre>

<p>The actual stream with implicit nodes is:</p>

<p><img src="http://media.tumblr.com/tumblr_m2f47oLuwZ1qgmvbu.png" alt=""/></p>

<p>The <code>json</code> way is more verbose but is full-featured: you can create complex
processing streams with many branches. <code>stream.json</code>:</p>

<pre class="prettyprint">
    {
        "nodes": { 
            "source": { "type":"csv_source", "resource": "data.csv" },
            "audit":  { "type":"audit" },
            "target": { "type":"pretty_printer" }
        },
        "connections": [
            ["source", "audit"],
            ["audit", "target"]
        ]
    }
</pre>

<p>And run:</p>

<pre><code>$ brewery run stream.json
</code></pre>

<p>To list all available nodes do:</p>

<pre><code>$ brewery nodes
</code></pre>

<p>To get more information about a node, run <code>brewery nodes &lt;node_name&gt;</code>:</p>

<pre><code>$ brewery nodes string_strip
</code></pre>

<p>Note that data streaming from command line is more limited than the python
way. You might not get access to nodes and node features that require python
language, such as python storage type nodes or functions.</p>

<h2>Higher order messaging</h2>

<p>Preferred programming way of creating streams is through <em>higher order
messaging</em> (HOM), which is, in this case, just fancy name for pretending doing
something while in fact we are preparing the stream.</p>

<p>This way of creating a stream is more readable and maintainable. It is easier
to insert nodes in the stream and create forks while not losing picture of the
stream. Might be not suitable for very complex streams though. Here is an
example:</p>

<pre class="prettyprint">
    b = brewery.create_builder()
    b.csv_source("data.csv")
    b.audit()
    b.pretty_printer()
</pre>

<p>When this piece of code is executed, nothing actually happens to the data
stream. The stream is just being prepared and you can run it anytime:</p>

<pre class="prettyprint">
    b.stream.run()
</pre>

<p>What actually happens? The builder <code>b</code> is somehow empty object that accepts
almost anything and then tries to find a node that corresponds to the method
called. Node is instantiated, added to the stream and connected to the
previous node.</p>

<p>You can also create branched stream:</p>

<pre class="prettyprint">
    b = brewery.create_builder()
    b.csv_source("data.csv")
    b.audit()

    f = b.fork()
    f.csv_target("audit.csv")

    b.pretty_printer()
</pre>

<h2>Basic Construction</h2>

<p>This is the lowest level way of creating the stream and allows full
customisation and control of the stream. In the <em>basic construction</em> method
the programmer prepares all node instance objects and connects them
explicitly, node-by-node. Might be a too verbose, however it is to be used by
applications that are constructing streams either using an user interface or
from some stream descriptions. All other methods are using this one.</p>

<pre class="prettyprint">
    from brewery import Stream
    from brewery.nodes import CSVSourceNode, AuditNode, PrettyPrinterNode

    stream = Stream()

    # Create pre-configured node instances
    src = CSVSourceNode("data.csv")
    stream.add(src)

    audit = AuditNode()
    stream.add(audit)

    printer = PrettyPrinterNode()
    stream.add(printer)

    # Connect nodes: source -&gt; target
    stream.connect(src, audit)
    stream.connect(audit, printer)

    stream.run()
</pre>

<p>It is possible to pass nodes as dictionary and connections as list of tuples
<em>(source, target)</em>:</p>

<pre class="prettyprint">
    stream = Stream(nodes, connections)
</pre>

<h1>Future plans</h1>

<p>What would be lovely to have in brewery?</p>

<p><strong>Probing and data quality indicators</strong> – tools for simple data probing and
easy way of creating data quality indicators. Will allow something like
&#8220;test-driven-development&#8221; but for data. This is the next step.</p>

<p><strong>Stream optimisation</strong> – merge multiple nodes into single processing unit
before running the stream. Might be done in near future.</p>

<p><strong>Backend-based nodes and related data transfer between backend nodes</strong> – For
example, two SQL nodes might pass data through a database table instead of
built-in data pipe or two numpy/scipy-based nodes might use numpy/scipy
structure to pass data to avoid unnecessary streaming. Not very soon, but
foreseeable future.</p>

<p><strong>Stream compilation</strong> – compile a stream to an optimised script. Not too
soon, but like to have that one.</p>

<p>Last, but not least: Currently there is little performance cost because of the
nature of brewery implementation. This penalty will be explained in another
blog post, however to make long story short, it has to do with threads, Python
GIL and non-optimalized stream graph. There is no future prediction for this
one, as it might be included step-by-step. Also some Python 3 features look
promising, such as <code>yield from</code> in Python 3.3 (<a href="http://www.python.org/dev/peps/pep-0380/">PEP 308</a>).</p>

<h2>Links</h2>

<ul><li><a href="https://github.com/Stiivi/brewery">Brewery at github</a></li>
<li><a href="http://packages.python.org/brewery/">Documentation</a> and <a href="http://packages.python.org/brewery/node_reference.html">Node Reference</a></li>
<li><a href="https://github.com/Stiivi/brewery/tree/master/examples">Examples at github</a></li>
<li><a href="https://groups.google.com/forum/?fromgroups#!forum/databrewery">Google Group</a></li>
</ul>