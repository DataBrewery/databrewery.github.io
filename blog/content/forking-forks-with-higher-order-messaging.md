Title: Forking Forks with Higher Order Messaging
Date: 2011-03-28
Tags: feature, howto, brewery
Category: feature
Slug: forking-forks-with-higher-order-messaging
Author: Stefan Urbanek
Summary: Forking Forks with Higher Order Messaging

<p>New way of constructing streams has been implemented which uses &#8220;higher order messaging&#8221;. What does that mean? Instead of constructing the stream from nodes and connections, you &#8220;call&#8221; functions that process your data. You pretend in your script that you work with data using functions:</p>

<pre class="prettyprint">
...
main.csv_source("data.csv")
main.sample(1000)
main.aggregate(keys = ["year"])
main.formatted_printer()
...
</pre>

<p>Executing the functions as written in a script might be be very expensive from time and memory perspective. What is in fact happening is that instead of executing the data processing functions a stream network is being constructed.</p>

<h1>Construction</h1>

<p>Construction is being done by using <em>forked branches</em>. You create an empty forked branch by forking an empty stream:</p>

<pre class="prettyprint">
from brewery.streams import *

stream = Stream()
main = stream.fork()
...
</pre>

<p>Now you have fork <code>main</code>. Each function call on <code>main</code> will append new processing node to the fork and the new node will be connected to the previous node of the fork.</p>

<p><img src="http://databrewery.org/images/fork-construction01.png" alt="Fork Construction"/></p>

<p>Function names are based on node names in most of the cases. There might be custom function names for some nodes in the future, but now there is just simple rule:</p>

<ol><li>decamelize node name: <code>CSVSourceNode</code> to <code>csv source node</code></li>
<li>replace spaces with underscores: <code>csv_source_node</code></li>
<li>remove &#8216;node&#8217; suffix: <code>csv_source</code></li>
</ol><p>Arguments to the function are the same as arguments for node constructor. If you want to do more node configuration you can access current node with <code>node</code> attribute of the fork:</p>

<pre class="prettyprint">
main.node.keys = ["country"]
</pre>

<h1>Running</h1>

<p>Run the stream as if it was constructed manually from nodes and connections:</p>

<pre class="prettyprint">
stream.run()
</pre>

<h1>Forking</h1>

<p>So far you are able to construct single simple stream from a source to a target. There are plenty of situations where linear processing is not sufficient and you will need to have branches. To create another branch, you <code>fork()</code> a fork. For example, to attach data audit to the stream insert following code right after the node you want to audit:</p>

<pre class="prettyprint">
# we are in main at node after which we want to have multiple branches

audit = main.fork()
audit.audit()
audit.value_threshold(...)
audit.formatted_printer(...)

# continue main.* branch here...
</pre>

<h1>Example</h1>

<p>Here is full example how to use forking with HOM in Brewery:</p>

<pre class="prettyprint">
# Create the stream and empty fork
stream = Stream()
main = stream.fork()

# Start adding nodes by pretending that we are processing using functions
main.csv_source("data.csv", read_header = True, encoding = "utf-8")
main.coalesce_value_to_type()

# Create another fork for data audit:
audit = main.fork()
audit.audit(distinct_threshold = None)
audit.value_threshold(thresholds = [ ["null_record_ratio", 0.01] ],
                        bin_names = ("ok", "fail"))

audit.formatted_printer()
audit.node.header = u"field                            nulls     status   distinct\n" \
                         "------------------------------------------------------------"
audit.node.format = u"{field_name:7.2%} {null_record_ratio_bin:&gt;10} {distinct_count:&gt;10}"

# ...and we continue in main branch
main.database_table_target(url = "postgres://localhost/sandbox", 
                            table = "data",
                            create = True,
                            replace = True,
                            add_id_key = True)

# Run the stream and pretty-print the exception
try:
    stream.run()
except pipes.StreamRuntimeError, e:
    e.print_exception()
</pre>

<p>The constructed stream looks like this:</p>

<p><img src="http://databrewery.org/images/fork-construction02.png" alt="Fork Example Stream"/></p>