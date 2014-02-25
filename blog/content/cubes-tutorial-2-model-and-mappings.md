Title: Cubes Tutorial 2 - Model and Mappings
Date: 2011-11-24
Tags: cubes, tutorial
Category: cubes
Slug: cubes-tutorial-2-model-and-mappings
Author: Stefan Urbanek
Summary: Cubes Tutorial 2 - Model and Mappings

<p>In the <a href="http://blog.databrewery.org/post/12966527920/cubes-tutorial-1-getting-started">first tutorial</a> we talked about how to construct model programmatically and how to do basic aggregations.</p>

<p>In this tutorial we are going to learn:</p>

<ul><li>how to use model description file</li>
<li>why and how to use logical to physical mappings</li>
</ul><p>Data used are the same as in the first tutorial,  <a href="https://raw.github.com/Stiivi/cubes/master/tutorial/data/IBRD_Balance_Sheet__FY2010.csv">IBRD Balance Sheet</a> taken from <a href="https://finances.worldbank.org/Accounting-and-Control/IBRD-Balance-Sheet-FY2010/e8yz-96c6">The World Bank</a>. However, for purpose of this tutorial, the  file was little bit manually edited: the column &#8220;Line Item&#8221; is split into two:
<em>Subcategory</em> and <em>Line Item</em> to provide two more levels to total of three levels of hierarchy.</p>

<h2>Logical Model</h2>

<p>The Cubes framework uses a logical model. Logical model describes the data from user’s or analyst’s
perspective: data how they are being measured, aggregated and reported. Model creates an abstraction layer
therefore making reports independent of physical structure of the data. More information can be found in the
<a href="http://packages.python.org/cubes/model.html">framework documentation</a></p>

<p>The model description file is a JSON file containing a dictionary:</p>

<pre class="prettyprint">
{
    "dimensions": [  ...  ],
    "cubes": { ... }
}
</pre>

<p>First we define the dimensions. They might be shared by multiple cubes, therefore they belong to the model
space. There are two dimensions: <em>item</em> and <em>year</em> in our dataset. The <em>year</em> dimension is flat, contains only one
level and has no details. The dimension <em>item</em> has three levels: <em>category</em>, <em>subcategory</em> and <em>line item</em>.
It looks like this:</p>

<p><img src="http://media.tumblr.com/tumblr_lv67lezyq31qgmvbu.png" alt=""/></p>

<p>We define them as:</p>

<pre class="prettyprint">
{
    "dimensions": [
        {"name":"item",
         "levels": ["category", "subcategory", "line_item"]
        },
        {"name":"year"}
    ],
    "cubes": {...}
}
</pre>

<p>The levels of our tutorial dimensions are simple, with no details. There is little bit of implicit
construction going on behind the scenes of dimension initialization, but that will be described later. In
short: default hierarchy is created and for each level single attribute is created with the same name as the
level.</p>

<p>Next we define the cubes. The cube is in most cases specified by list of dimensions and measures:</p>

<pre class="prettyprint">
{
    "dimensions": [...],
    "cubes": [
        {
            "name": "irbd_balance",
            "dimensions": ["item", "year"],
            "measures": ["amount"]
        }
    ]
}
</pre>

<p>And we are done: we have dimensions and a cube. Well, almost done: we have to tell the framework, which
attributes are going to be used.</p>

<h2>Attribute Naming</h2>

<p>As mentioned before, cubes uses logical model to describe the data used in the reports. To assure
consistency with dimension attribute naming, cubes uses sheme: <code>dimension.attribute</code> for non-flat
dimensions. Why? Firstly, it decreases doubt to which dimension the attribute belongs. Secondly the
<code>item.category</code> will always be <code>item.category</code> in the report, regardless of how the
field will be named in the source and in which table the field exists.</p>

<p>Imagine a snowflake schema: fact table in the middle with references to multiple tables containing various
dimension data. There might be a dimension spanning through multiple tables, like product category in one
table, product subcategory in another table. We should not care about what table the attribute comes from,
we should care only that the attribute is called <code>category</code> and belongs to a dimension
<code>product</code> for example.</p>

<p>Another reason is, that in localized data, the analyst will use <code>item.category_label</code> and
appropriate localized physical attribute will be used. Just to name few reasons.</p>

<p>Knowing the naming scheme we have following cube attribute names:</p>

<ul><li><code>year</code> (it is flat dimension)</li>
<li><code>item.category</code></li>
<li><code>item.subcategory</code></li>
<li><code>item.line_item</code></li>
</ul><p>Problem is, that the table does not have the columns with the names. That is what mapping is for: maps
logical attributes in the model into physical attributes in the table.</p>

<h1>Mapping</h1>

<p>The source table looks like this:</p>

<p><img src="http://media.tumblr.com/tumblr_lv67uvnhtJ1qgmvbu.png" alt=""/></p>

<p>We have to tell how the dimension attributes are mapped to the table columns. It is a simple dictionary
where keys are dimension attribute names and values are physical table column names.</p>

<pre class="prettyprint">
{
    ...
    "cubes": [
        {
            "name":"irbd_balance",
            ...
            "mappings": { "item.line_item": "line_item",
                          "item.subcategory": "subcategory",
                          "item.category": "category" }
        }
    ]
}
</pre>

<p><em>Note:</em> The mapping values might be backend specific. They are physical table column names for the current
implementation of the SQL backend.</p>

<p>Full model looks like this:</p>

<pre class="prettyprint">
{
    "dimensions": [
        {"name":"item",
         "levels": ["category", "subcategory", "line_item"]
        },
        {"name":"year"}
    ],
    "cubes": [
        {
            "name":"irbd_balance",
            "dimensions": ["item", "year"],
            "measures": ["amount"],
            "mappings": { "item.line_item": "line_item",
                          "item.subcategory": "subcategory",
                          "item.category": "category" }
        }
        ]
    }
}
</pre>

<h1>Example</h1>

<p>Now we have the model, saved for example in the <code>models/model_02.json</code>. Let&#8217;s do some
preparation:</p>

<p>Define table names and a view name to be used later. The view is going to be used as logical abstraction.</p>

<pre class="prettyprint">
FACT_TABLE = "ft_irbd_balance"
FACT_VIEW = "vft_irbd_balance"
</pre>

<p>Load the data, as in the previous example, using the tutorial helper function (again, do not use that in
production):</p>

<pre class="prettyprint">
engine = sqlalchemy.create_engine('sqlite:///:memory:')
tutorial.create_table_from_csv(engine, 
                      "data/IBRD_Balance_Sheet__FY2010-t02.csv", 
                      table_name=FACT_TABLE, 
                      fields=[
                            ("category", "string"), 
                            ("subcategory", "string"), 
                            ("line_item", "string"),
                            ("year", "integer"), 
                            ("amount", "integer")],
                      create_id=True    
                        
                        )
connection = engine.connect()
</pre>

<p>The new data sheet is in the <a href="https://github.com/Stiivi/cubes/raw/master/tutorial/data/IBRD_Balance_Sheet__FY2010-t02.csv">github
repository</a>.</p>

<p>Load the model, get the cube and specify where cube&#8217;s source data comes from:</p>

<pre class="prettyprint">
workspace = cubes.Workspace()
workspace.import_model("models/model_02.json")
cube = workspace.cube("irbd_balance")
cube.fact = FACT_TABLE
</pre>

<p>We have to prepare the logical structures used by the browser. Currenlty provided is simple data
denormalizer: creates one wide view with logical column names (optionally with localization). Following
code initializes the denomralizer and creates a view for the cube:</p>

<pre class="prettyprint">
dn = cubes.backends.sql.SQLDenormalizer(cube, connection)

dn.create_view(FACT_VIEW)
</pre>

<p>And from this point on, we can continue as usual:</p>

<pre class="prettyprint">
browser = cubes.backends.sql.SQLBrowser(cube, connection, view_name = FACT_VIEW)

cell = cubes.Cell(cube)
result = browser.aggregate(cell)

print "Record count: %d" % result.summary["record_count"]
print "Total amount: %d" % result.summary["amount_sum"]
</pre>

<p>The tutorial sources can be found in the <a href="https://github.com/Stiivi/cubes/tree/master/tutorial">Cubes github
repository</a>. Requires current git clone.</p>

<p>Next: Drill-down through deep hierarchy.</p>

<p>If you have any questions, suggestions, comments, let me know.</p>
