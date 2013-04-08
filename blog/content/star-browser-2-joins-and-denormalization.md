Title: Star Browser, Part 2: Joins and Denormalization
Date: 2012-05-01
Tags: cubes, olap
Category: cubes
Slug: star-browser-2-joins-and-denormalization
Author: Stefan Urbanek
Summary: Star Browser, Part 2: Joins and Denormalization

<p>Last time I was talking about how <a href="http://blog.databrewery.org/post/22119118550">logical attributes are mapped to the
physical table columns</a> in the
Star Browser. Today I will describe how joins are formed and how
denormalization is going to be used.</p>

<p>The Star Browser is new aggregation browser in for the
<a href="https://github.com/Stiivi/cubes">Cubes</a> – lightweight Python OLAP Framework.</p>

<h1>Star, Snowflake, Master and Detail</h1>

<p>Star browser supports a star:</p>

<p><img src="http://media.tumblr.com/tumblr_m3ajfbXcHo1qgmvbu.png" alt=""/></p>

<p>&#8230; and snowflake database schema:</p>

<p><img src="http://media.tumblr.com/tumblr_m3ajfn8QYt1qgmvbu.png" alt=""/></p>

<p>The browser should know how to construct the star/snowflake and that is why
you have to specify the joins of the schema. The join specification is very
simple:</p>

<pre class="prettyprint">
"joins" = [
    { "master": "fact_sales.product_id", "detail": "dim_product.id" }
]
</pre>

<p>Joins support only single-column keys, therefore you might have to create
surrogate keys for your dimensions.</p>

<p>As in mappings, if you have specific needs for explicitly mentioning database
schema or any other reason where <code>table.column</code> reference is not enough, you
might write:</p>

<pre class="prettyprint">
"joins" = [
    { 
        "master": "fact_sales.product_id",
        "detail": {
            "schema": "sales",
            "table": "dim_products",
            "column": "id"
        }
]
</pre>

<p>What if you need to join same table twice? For example, you have list of
organizations and you want to use it as both: supplier and service consumer.
It can be done by specifying alias in the joins:</p>

<pre class="prettyprint">
"joins" = [
    {
        "master": "contracts.supplier_id", 
        "detail": "organisations.id",
        "alias": "suppliers"
    },
    {
        "master": "contracts.consumer_id", 
        "detail": "organisations.id",
        "alias": "consumers"
    }
]
</pre>

<p>In the mappings you refer to the table by alias specified in the joins, not by
real table name:</p>

<pre class="prettyprint">
"mappings": {
    "supplier.name": "suppliers.org_name",
    "consumer.name": "consumers.org_name"
}
</pre>

<p><img src="http://media.tumblr.com/tumblr_m3ajian3sA1qgmvbu.png" alt=""/></p>

<h2>Relevant Joins and Denormalization</h2>

<p>The new mapper joins only tables that are relevant for given query. That is,
if you are browsing by only one dimension, say <em>product</em>, then only product
dimension table is joined.</p>

<p>Joins are slow, expensive and the denormalization can be
helpful:</p>

<p><img src="http://media.tumblr.com/tumblr_m3ajglKwV11qgmvbu.png" alt=""/></p>

<p>The old browser is based purely on the denormalized view. Despite having a
performance gain, it has several disadvantages. From the
join/performance perspective the major one is, that the denormalization is
required and it is not possible to browse data in a database that was
&#8220;read-only&#8221;. This requirements was also one unnecessary step for beginners,
which can be considered as usability problem.</p>

<p>Current implementation of the <em>Mapper</em> and <em>StarBrowser</em> allows
denormalization to be integrated in a way, that it might be used based on
needs and situation:</p>

<p><img src="http://media.tumblr.com/tumblr_m3d4ctMm6K1qgmvbu.png" alt=""/></p>

<p>It is not yet there and this is what needs to be done:</p>

<ul><li>function for denormalization - similar to the old one: will take cube and
view name and will create denormalized view (or a table)</li>
<li>make mapper accept the view and ignore joins</li>
</ul><p>Goal is not just to slap denormalization in, but to make it a configurable
alternative to default star browsing. From user&#8217;s perspective, the workflow
will be:</p>

<ol><li>browse star/snowflake until need for denormalization arises</li>
<li>configure denormalization and create denormalized view</li>
<li>browse the denormalized view</li>
</ol><p>The proposed options are: <code>use_denormalization</code>, <code>denormalized_view_prefix</code>,
<code>denormalized_view_schema</code>.</p>

<p>The Star Browser is half-ready for the denormalization, just few changes are
needed in the mapper and maybe query builder. These changes have to be
compatible with another, not-yet-included feature: SQL pre-aggregation.</p>

<h1>Conclusion</h1>

<p>The new way of joining is very similar to the old one, but has much more
cleaner code and is separated from mappings. Also it is more transparent. New
feature is the ability to specify a database schema. Planned feature to be
integrated is automatic join detection based on foreign keys.</p>

<p>In the next post (the last post in this series) about the new <em>StarBrowser</em>, I am going to
explain <a href="http://blog.databrewery.org/post/22904157693">aggregation improvements and changes</a>.</p>

<h1>Links</h1>

<p>Relevant source code is <a href="https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/mapper.py">this one</a> (github).</p>

<p>See also <a href="https://github.com/Stiivi/cubes">Cubes at github</a>,
<a href="http://packages.python.org/cubes/">Cubes Documentation</a>,
<a href="http://groups.google.com/group/cubes-discuss/">Mailing List</a>
and <a href="https://github.com/Stiivi/cubes/issues">Submit issues</a>. Also there is an 
IRC channel <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on
irc.freenode.net</p>