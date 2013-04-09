Title: Cubes Tutorial 1 - Getting started
Date: 2011-11-18
Tags: cubes, tutorial
Category: cubes
Slug: cubes-tutorial-1-getting-started
Author: Stefan Urbanek
Summary: Cubes Tutorial 1 - Getting started

<p>In this tutorial you are going to learn how to start with cubes. The example shows:</p>

<ul><li>how to build a model programatically</li>
<li>how to create a model with flat dimensions</li>
<li>how to aggregate whole cube</li>
<li>how to drill-down and aggregate through a dimension</li>
</ul><p>The example data used are <a href="https://raw.github.com/Stiivi/cubes/master/tutorial/data/IBRD_Balance_Sheet__FY2010.csv">IBRD Balance Sheet</a> taken from <a href="https://finances.worldbank.org/Accounting-and-Control/IBRD-Balance-Sheet-FY2010/e8yz-96c6">The World Bank</a></p>

<p>Create a tutorial directory and download the file:</p>

<pre>
curl -O <a href="https://raw.github.com/Stiivi/cubes/master/tutorial/data/IBRD_Balance_Sheet__FY2010.csv">https://raw.github.com/Stiivi/cubes/master/tutorial/data/IBRD_Balance_Sheet__FY2010.csv</a>
</pre>

<p>Create a <code>tutorial_01.py</code>:</p>

<pre class="prettyprint">
import sqlalchemy
import cubes
import cubes.tutorial.sql as tutorial
</pre>

<p>Cubes package contains tutorial helper methods. It is advised not to use them in production, they are provided just to simplify learner&#8217;s life.</p>

<p>Prepare the data using the tutorial helper methods:</p>

<pre class="prettyprint">

engine = sqlalchemy.create_engine('sqlite:///:memory:')
tutorial.create_table_from_csv(engine, 
                      "IBRD_Balance_Sheet__FY2010.csv", 
                      table_name="irbd_balance", 
                      fields=[
                            ("category", "string"), 
                            ("line_item", "string"),
                            ("year", "integer"), 
                            ("amount", "integer")],
                      create_id=True    
                        
                        )
</pre>

<p>Now, create a model:</p>

<pre class="prettyprint">
model = cubes.Model()
</pre>

<p>Add dimensions to the model. Reason for having dimensions in a model is, that they might be shared by multiple cubes.</p>

<pre class="prettyprint">
model.add_dimension(cubes.Dimension("category"))
model.add_dimension(cubes.Dimension("line_item"))
model.add_dimension(cubes.Dimension("year"))
</pre>

<p>Define a cube and specify already defined dimensions:</p>

<pre class="prettyprint">
cube = cubes.Cube(name="irbd_balance", 
                  model=model,
                  dimensions=["category", "line_item", "year"],
                  measures=["amount"]
                  )
</pre>

<p>Create a browser and get a cell representing the whole cube (all data):</p>

<pre class="prettyprint">
browser = cubes.backends.sql.SQLBrowser(cube, engine.connect(), view_name = "irbd_balance")

cell = browser.full_cube()
</pre>

<p>Compute the aggregate. Measure fields of aggregation result have aggregation suffix, currenlty only <code>_sum</code>. Also a total record count within the cell is included as <code>record_count</code>.</p>

<pre class="prettyprint">
result = browser.aggregate(cell)

print "Record count: %d" % result.summary["record_count"]
print "Total amount: %d" % result.summary["amount_sum"]
</pre>

<p>Now try some drill-down by category:</p>

<pre class="prettyprint">
print "Drill Down by Category"
result = browser.aggregate(cell, drilldown=["category"])

print "%-20s%10s%10s" % ("Category", "Count", "Total")
for record in result.drilldown:
    print "%-20s%10d%10d" % (record["category"], record["record_count"], record["amount_sum"])
</pre>

<p>Drill-dow by year:</p>

<pre class="prettyprint">
print "Drill Down by Year:"
result = browser.aggregate(cell, drilldown=["year"])
print "%-20s%10s%10s" % ("Year", "Count", "Total")
for record in result.drilldown:
    print "%-20s%10d%10d" % (record["year"], record["record_count"], record["amount_sum"])
</pre>

<p>All tutorials with example data and models will be stored together with <a href="https://github.com/Stiivi/cubes">cubes sources</a> under the <code>tutorial/</code> directory.</p>

<p>Next: Model files and hierarchies.</p>

<p>If you have any questions, comments or suggestions, do not hesitate to ask.</p>