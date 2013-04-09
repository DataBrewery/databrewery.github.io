Title: Brewery 0.7 Released
Date: 2011-06-25
Tags: announcement, release, brewery
Category: announcement
Slug: brewery-0-7-released
Author: Stefan Urbanek
Summary: Brewery 0.7 Released

<p>New small release is out with quite nice addition of documentation. It does not bring too many new features, but contains a refactoring towards better package structure, that breaks some compatibility.</p>

<p><strong>Documentation updates</strong></p>

<ul><li><a href="http://packages.python.org/brewery/install.html">installation instructions</a> with list of optional dependencies</li>
<li>information about <a href="http://packages.python.org/brewery/metadata.html">fields and metadata</a></li>
<li>included documentation about <a href="http://packages.python.org/brewery/stores.html">data store classes</a></li>
<li>included text from previous blog post about <a href="http://packages.python.org/brewery/streams.html#forking-forks-with-higher-order-messaging">Higher Order Messaging</a></li>
</ul><p><strong>Framework Changes</strong></p>

<ul><li>added soft (optional) <a href="http://packages.python.org/brewery/install.html#requirements">dependencies</a> on backend libraries. Exception with useful information will be raised when functionality that depends on missing package is used. Example: &#8220;Exception: Optional package &#8216;sqlalchemy&#8217; is not installed. Please install the package from <a href="http://www.sqlalchemy.org/">http://www.sqlalchemy.org/</a> to be able to use: SQL streams. Recommended version is &gt; 0.7&#8221;</li>
<li>field related classes and functions were moved from &#8216;ds&#8217; module to <a href="http://packages.python.org/brewery/metadata.html">&#8216;metadata&#8217;</a> and included in brewery top-level: Field, FieldList, expand_record, collapse_record</li>
<li>added <a href="http://packages.python.org/brewery/probes.html">probes</a></li>
</ul><p><strong>Depreciated functions</strong></p>

<ul><li>brewery.ds.field_name() - use str(field) instead</li>
<li>brewery.ds.fieldlist() - use <a href="http://packages.python.org/brewery/metadata.html#brewery.metadata.FieldList">brewery.metadata.FieldList()</a> instead</li>
</ul><p><strong>Streams</strong></p>

<ul><li>new node: <a href="http://packages.python.org/brewery/node_reference.html#derive-node">DeriveNode</a> - derive new field with callables or string formula (python expression)</li>
<li>new <a href="http://packages.python.org/brewery/node_reference.html#select">SelectNode</a> implementation: accepts callables or string with python code</li>
<li>former SelectNode renamed to <a href="http://packages.python.org/brewery/node_reference.html#function-select">FunctionSelectNode</a></li>
</ul><p>Enjoy!</p>

<h2>Links</h2>

<ul><li><a href="https://bitbucket.org/Stiivi/brewery/overview">BitBucket repository</a></li>
<li><a href="https://github.com/stiivi/brewery">github repository</a></li>
<li><a href="http://groups.google.com/group/databrewery">Mailing list</a></li>
</ul>