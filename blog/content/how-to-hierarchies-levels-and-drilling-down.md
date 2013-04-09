Title: How-to: hierarchies, levels and drilling-down
Date: 2011-11-28
Tags: cubes, tutorial, olap, howto
Category: cubes
Slug: how-to-hierarchies-levels-and-drilling-down
Author: Stefan Urbanek
Summary: How-to: hierarchies, levels and drilling-down

<p>In this Cubes OLAP how-to we are going to learn:</p>

<ul><li>how to create a hierarchical dimension</li>
<li>how to do drill-down through a hierarchy</li>
<li>detailed level description</li>
</ul><p>In the <a href="http://blog.databrewery.org/post/13255558153/cubes-tutorial-2-model-and-mappings">previous
tutorial</a> we learned how
to use model descriptions in a JSON file and how to do physical to logical mappings.</p>

<p>Data used are similar as in the second tutorial, manually modified <a href="https://raw.github.com/Stiivi/cubes/master/tutorial/data/IBRD_Balance_Sheet__FY2010-t03.csv">IBRD Balance
Sheet</a> taken
from <a href="https://finances.worldbank.org/Accounting-and-Control/IBRD-Balance-Sheet-FY2010/e8yz-96c6">The World
Bank</a>.
Difference between second tutorial and this one is added two columns: category code and sub-category code.
They are simple letter codes for the categories and subcategories.</p>

<h2>Hierarchy</h2>

<p>Some dimensions can have multiple levels forming a hierarchy. For example dates have year, month, day;
geography has country, region, city; product might have category, subcategory and the product.</p>

<p>Note: Cubes supports multiple hierarchies, for example for date you might have year-month-day or
year-quarter-month-day. Most dimensions will have one hierarchy, thought.</p>

<p>In our example we have the <code>item</code> dimension with three levels of hierarchy: <em>category</em>, <em>subcategory</em> and
<em>line item</em>:</p>

<p><img src="http://media.tumblr.com/tumblr_lvdr0nIHgl1qgmvbu.png" alt=""/></p>

<p>The levels are defined in the model:</p>

<pre class="prettyprint">
"levels": [
    {
        "name":"category",
        "label":"Category",
        "attributes": ["category"]
    },
    {
        "name":"subcategory",
        "label":"Sub-category",
        "attributes": ["subcategory"]
    },
    {
        "name":"line_item",
        "label":"Line Item",
        "attributes": ["line_item"]
    }
]
</pre>

<p>You can see a slight difference between this model description and the previous one: we didn&#8217;t just specify
level names and didn&#8217;t let cubes to fill-in the defaults. Here we used explicit description of each level.
<code>name</code> is level identifier, <code>label</code> is human-readable label of the level that can be
used in end-user applications and <code>attributes</code> is list of attributes that belong to the level.
The first attribute, if not specified otherwise, is the key attribute of the level.</p>

<p>Other level description attributes are <code>key</code> and <code>label_attribute</code>. The
<code>key</code> specifies attribute name which contains key for the level. Key is an id number, code or
anything that uniquely identifies the dimension level. <code>label_attribute</code> is name of an attribute
that contains human-readable value that can be displayed in user-interface elements such as tables or
charts.</p>

<h2>Preparation</h2>

<p>In this how-to we are going to skip all off-topic code, such as data initialization. The full example can
be found in the <a href="https://github.com/Stiivi/cubes/tree/master/tutorial">tutorial sources</a> with suffix
<code>03</code>.</p>

<p>In short we need:</p>

<ul><li>data in a database</li>
<li>logical model (see <code>model_03.json</code>) prepared with appropriate mappings</li>
<li>denormalized view for aggregated browsing (for current simple SQL browser implementation)</li>
</ul><h2>Drill-down</h2>

<p>Drill-down is an action that will provide more details about data. Drilling down through a dimension
hierarchy will expand next level of the dimension. It can be compared to browsing through your directory
structure.</p>

<p>We create a function that will recursively traverse a dimension hierarchy and will print-out aggregations
(count of records in this example) at the actual browsed location.</p>

<p><strong>Attributes</strong></p>

<ul><li>cell - cube cell to drill-down</li>
<li>dimension - dimension to be traversed through all levels</li>
<li>path - current path of the <code>dimension</code></li>
</ul><p>Path is list of dimension points (keys) at each level. It is like file-system path.</p>

<pre class="prettyprint">
def drill_down(cell, dimension, path = []):
</pre>

<p>Get dimension&#8217;s default hierarchy. Cubes supports multiple hierarchies, for example for date you might
have year-month-day or year-quarter-month-day. Most dimensions will have one hierarchy, thought.</p>

<pre class="prettyprint">
    hierarchy = dimension.default_hierarchy
</pre>

<p><em>Base path</em> is path to the most detailed element, to the leaf of a tree, to the fact. Can we go deeper in
the hierarchy?</p>

<pre class="prettyprint">
    if hierarchy.path_is_base(path):
        return
</pre>

<p>Get the next level in the hierarchy. <code>levels_for_path</code> returns list of levels according to
provided path. When <code>drilldown</code> is set to <code>True</code> then one more level is returned.</p>

<pre class="prettyprint">
    levels = hierarchy.levels_for_path(path,drilldown=True)
    current_level = levels[-1]
</pre>

<p>We need to know name of the level key attribute which contains a path component. If the model does not
explicitly specify key attribute for the level, then first attribute will be used:</p>

<pre class="prettyprint">
    level_key = dimension.attribute_reference(current_level.key)
</pre>

<p>For prettier display, we get name of attribute which contains label to be displayed
for the current level. If there is no label attribute, then key attribute is used.</p>

<pre class="prettyprint">
    level_label = dimension.attribute_reference(current_level.label_attribute)
</pre>

<p>We do the aggregation of the cell&#8230; Think of <code>ls $CELL</code> command in commandline, where
<code>$CELL</code> is a directory name. In this function we can think of <code>$CELL</code> to be same as
current working directory (<code>pwd</code>)</p>

<pre class="prettyprint">
    result = browser.aggregate(cell, drilldown=[dimension])

    for record in result.drilldown:
        print "%s%s: %d" % (indent, record[level_label], record["record_count"])
        ...
</pre>

<p>And now the drill-down magic. First, construct new path by key attribute value appended to the current
path:</p>

<pre class="prettyprint">
        drill_path = path[:] + [record[level_key]]
</pre>

<p>Then get a new cell slice for current path:</p>

<pre class="prettyprint">
        drill_down_cell = cell.slice(dimension, drill_path)
</pre>

<p>And do recursive drill-down:</p>

<pre class="prettyprint">
        drill_down(drill_down_cell, dimension, drill_path)
</pre>

<p>The function looks like this:</p>

<p><img src="http://media.tumblr.com/tumblr_lvdrsbS5VW1qgmvbu.png" alt=""/></p>

<p>Working function example <code>03</code> can be found in the <a href="https://github.com/Stiivi/cubes/blob/master/tutorial/tutorial_03.py">tutorial
sources</a>.</p>

<p>Get the full cube (or any part of the cube you like):</p>

<pre class="prettyprint">
cell = browser.full_cube()
</pre>

<p>And do the drill-down through the item dimension:</p>

<pre class="prettyprint">
drill_down(cell, cube.dimension("item"))
</pre>

<p>The output should look like this:</p>

<pre>
a: 32
    da: 8
        Borrowings: 2
        Client operations: 2
        Investments: 2
        Other: 2
    dfb: 4
        Currencies subject to restriction: 2
        Unrestricted currencies: 2
    i: 2
        Trading: 2
    lo: 2
        Net loans outstanding: 2
    nn: 2
        Nonnegotiable, nonintrest-bearing demand obligations on account of subscribed capital: 2
    oa: 6
        Assets under retirement benefit plans: 2
        Miscellaneous: 2
        Premises and equipment (net): 2
</pre>

<p>Note that because we have changed our source data, we see level codes instead of level names. We will fix
that later. Now focus on the drill-down.</p>

<p>See that nice hierarchy tree?</p>

<p>Now if you slice the cell through year 2010 and do the exact same drill-down:</p>

<pre class="prettyprint">
    cell = cell.slice("year", [2010])
    drill_down(cell, cube.dimension("item"))
</pre>

<p>you will get similar tree, but only for year 2010 (obviously).</p>

<h2>Level Labels and Details</h2>

<p>Codes and ids are good for machines and programmers, they are short, might follow some scheme, easy to
handle in scripts. Report users have no much use of them, as they look cryptic and have no meaning for the
first sight.</p>

<p>Our source data contains two columns for category and for subcategory: column with code and column with
label for user interfaces. Both columns belong to the same dimension and to the same level. The key column
is used by the analytical system to refer to the dimension point and the label is just decoration.</p>

<p>Levels can have any number of detail attributes. The detail attributes have no analytical meaning and are
just ignored during aggregations. If you want to do analysis based on an attribute, make it a separate
dimension instead.</p>

<p>So now we fix our model by specifying detail attributes for the levels:</p>

<p><img src="http://media.tumblr.com/tumblr_lvdr2aHJRJ1qgmvbu.png" alt=""/></p>

<p>The model description is:</p>

<pre class="prettyprint">
"levels": [
        {
            "name":"category",
            "label":"Category",
            "label_attribute": "category_label",
            "attributes": ["category", "category_label"]
        },
        {
            "name":"subcategory",
            "label":"Sub-category",
            "label_attribute": "subcategory_label",
            "attributes": ["subcategory", "subcategory_label"]
        },
        {
            "name":"line_item",
            "label":"Line Item",
            "attributes": ["line_item"]
        }
    ]
}
</pre>

<p>Note the <code>label_attribute</code> keys. They specify which attribute contains label to be displayed.
Key attribute is by-default the first attribute in the list. If one wants to use some other attribute it
can be specified in <code>key_attribute</code>.</p>

<p>Because we added two new attributes, we have to add mappings for them:</p>

<pre class="prettyprint">
"mappings": { "item.line_item": "line_item",
              "item.subcategory": "subcategory",
              "item.subcategory_label": "subcategory_label",
              "item.category": "category",
              "item.category_label": "category_label" 
             }
</pre>

<p>In the example tutorial, which can be found in the Cubes sources under <code>tutorial/</code> directory,
change the model file from <code>model/model_03.json</code> to <code>model/model_03-labels.json</code>
and run the code again. Or fix the file as specified above.</p>

<p>Now the result will be:</p>

<pre>
Assets: 32
    Derivative Assets: 8
        Borrowings: 2
        Client operations: 2
        Investments: 2
        Other: 2
    Due from Banks: 4
        Currencies subject to restriction: 2
        Unrestricted currencies: 2
    Investments: 2
        Trading: 2
    Loans Outstanding: 2
        Net loans outstanding: 2
    Nonnegotiable: 2
        Nonnegotiable, nonintrest-bearing demand obligations on account of subscribed capital: 2
    Other Assets: 6
        Assets under retirement benefit plans: 2
        Miscellaneous: 2
        Premises and equipment (net): 2
</pre>

<h2>Implicit hierarchy</h2>

<p>Try to remove the last level <em>line_item</em> from the model file and see what happens. Code still works, but
displays only two levels. What does that mean? If metadata - logical model - is used properly in an
application, then application can handle most of the model changes without any application modifications.
That is, if you add new level or remove a level, there is no need to change your reporting application.</p>

<h2>Summary</h2>

<ul><li>hierarchies can have multiple levels</li>
<li>a hierarchy level is identifier by a key attribute</li>
<li>a hierarchy level can have multiple detail attributes and there is one special detail attribute: label attribute used for display in user interfaces</li>
</ul><p>Next: slicing and dicing or slicer server, not sure yet.</p>

<p>If you have any questions, suggestions, comments, let me know.</p>