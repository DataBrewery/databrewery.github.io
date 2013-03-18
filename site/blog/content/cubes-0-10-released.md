Title: Cubes 0.10 Released
Date: 2012-10-05
Tags: cubes, release, olap
Category: cubes
Slug: cubes-0-10-released
Author: Stefan Urbanek
Summary: Cubes 0.10 Released

<p>After a while, here is an update to Cubes - Python Lightweight OLAP framework for multidimensional modeling. There are some changes included that were mentioned in the <a href="http://www.slideshare.net/Stiivi/cubes-lightweight-python-olap">EruoPython talk</a> such as <code>table_rows</code> and <code>cross_table</code>.</p>

<p>I recommend to look at updated <a href="https://github.com/Stiivi/cubes/tree/master/examples">examples</a> in the Github repository. The <a href="http://flask.pocoo.org">Flask</a> example is now &#8220;real&#8221; example instead of &#8220;sandbox&#8221; example and you can see how to generate a simple table for dimension hierarchy browsing.</p>

<p>There is also a more complex example with star-like schema dataset in the <a href="https://github.com/Stiivi/cubes-examples">cubes-examples</a> github repository. Follow the instructions in README files how to make it running.</p>

<p>There are some backward incompatible changes in this release – until 1.0 the &#8220;point&#8221; releases will contain this kind of changes, as it is still evolving. You can find more information below.</p>

<h2>Quick Summary</h2>

<ul><li>Way how model is constructed has changed. Designated methods are <code>create_model()</code> or <code>load_model()</code></li>
<li>Dimension defition can have a &#8220;template&#8221;. For example:</li>
</ul><pre class="prettyprint">
    {
      "name": "contract_date",
      "template": "date"
    }
</pre>

<ul><li>added <code>table_rows()</code> and <code>cross_table()</code> to aggregation result for more convenient table creation. The <code>table_rows</code> takes care of providing appropriate dimension key and label for browsed level.</li>
<li>added <code>simple_model(cube_name, dimension_names, measures)</code></li>
</ul><p><em>Incompatibilities:</em>  use <code>create_model()</code> instead of <code>Model(**dict)</code>, if you
  were using just <code>load_model()</code>, you are fine.</p>

<h2>New Features</h2>

<ul><li>To address issue <a href="https://github.com/Stiivi/cubes/issues/8">#8</a>
<code>create_model(dict)</code> was added as replacement for <code>Model(**dict)</code>. <code>Model()</code> from
now on will expect correctly constructed model objects. <code>create_model()</code> will
be able to handle various simplifications and defaults during the
construction process.</li>
<li>added <code>info</code> attribute to all model objects. It can be used to store custom,
application or front-end specific information</li>
<li>preliminary implementation of <code>cross_table()</code> (interface might be changed)</li>
<li><code>AggregationResult.table_rows()</code> - new method that iterates through
drill-down rows and returns a tuple with key, label, path, and rest of the
fields.</li>
<li>dimension in model description can specify another template dimension – all
properties from the template will be inherited in the new dimension. All
dimension properties specified in the new dimension completely override the
template specification</li>
<li>added <code>point_cut_for_dimension</code></li>
<li>added <code>simple_model(cube_name, dimensions, measures)</code> – creates a single-cube
model with flat dimensions from a list of dimension names and measures from
a list of measure names. For example:</li>
</ul><pre class="prettyprint">
model = simple_model("contracts", ["year","contractor", "type"], ["amount"])
</pre>

<p><em>Slicer Server:</em></p>

<ul><li><code>/cell</code> – return cell details (replaces <code>/details</code>)</li>
</ul><h2>Changes</h2>

<ul><li>creation of a model from dictionary through <code>Model(dict)</code> is depreciated, use
<code>create_model(dict)</code> instead. All initialization code will be moved there.
Depreciation warnings were added. Old functionality retained for the time
being. (<strong>important</strong>)</li>
<li>Replaced <code>Attribute.full_name()</code> with <code>Attribute.ref()</code></li>
<li>Removed <code>Dimension.attribute_reference()</code> as same can be achieved with
<code>dim(attr).ref()</code></li>
<li><code>AggregationResult.drilldown</code> renamed to <code>AggregationResults.cells</code> (<strong>important</strong>)</li>
</ul><p>Planned Changes:</p>

<ul><li><code>str(Attribute)</code> will return ref() instead of attribute name as it is more
useful</li>
</ul><h2>Fixes</h2>

<ul><li>order of dimensions is now preserved in the Model</li>
</ul><h2>Links</h2>

<p>Sources can be found on <a href="https://github.com/Stiivi/cubes">github</a>.
Read the <a href="http://packages.python.org/cubes/">documentation</a>.</p>

<p>Join the <a href="http://groups.google.com/group/cubes-discuss">Google Group</a> for discussion, problem solving and announcements.</p>

<p>Submit issues and suggestions <a href="https://github.com/Stiivi/cubes/issues">on github</a></p>

<p>IRC channel <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on irc.freenode.net</p>

<p>If you have any questions, comments, requests, do not hesitate to ask.</p>