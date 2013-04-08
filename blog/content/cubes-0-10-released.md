Title: Cubes 0.10 Released
Date: 2012-10-05
Tags: cubes, release, olap
Category: cubes
Slug: cubes-0-10-released
Author: Stefan Urbanek
Summary: Cubes 0.10 Released

After a while, here is an update to Cubes - Python Lightweight OLAP framework for multidimensional modeling. There are some changes included that were mentioned in the [EruoPython talk](http://www.slideshare.net/Stiivi/cubes-lightweight-python-olap) such as `table_rows` and `cross_table`.

I recommend to look at updated [examples](https://github.com/Stiivi/cubes/tree/master/examples) in the Github repository. The [Flask](http://flask.pocoo.org) example is now "real" example instead of "sandbox" example and you can see how to generate a simple table for dimension hierarchy browsing.

There is also a more complex example with star-like schema dataset in the [cubes-examples](https://github.com/Stiivi/cubes-examples) github repository. Follow the instructions in README files how to make it running.

There are some backward incompatible changes in this release – until 1.0 the "point" releases will contain this kind of changes, as it is still evolving. You can find more information below.

Quick Summary
-------------

* Way how model is constructed has changed. Designated methods are `create_model()` or `load_model()`
* Dimension defition can have a "template". For example:

<pre class="prettyprint">
    {
      "name": "contract_date",
      "template": "date"
    }
</pre>
  
* added `table_rows()` and `cross_table()` to aggregation result for more convenient table creation. The `table_rows` takes care of providing appropriate dimension key and label for browsed level.
* added `simple_model(cube_name, dimension_names, measures)`

*Incompatibilities:*  use `create_model()` instead of `Model(**dict)`, if you
  were using just `load_model()`, you are fine.

New Features
------------

* To address issue [#8](https://github.com/Stiivi/cubes/issues/8)
  `create_model(dict)` was added as replacement for `Model(**dict)`. `Model()` from
  now on will expect correctly constructed model objects. `create_model()` will
  be able to handle various simplifications and defaults during the
  construction process.
* added `info` attribute to all model objects. It can be used to store custom,
  application or front-end specific information
* preliminary implementation of `cross_table()` (interface might be changed)
* `AggregationResult.table_rows()` - new method that iterates through
  drill-down rows and returns a tuple with key, label, path, and rest of the
  fields.
* dimension in model description can specify another template dimension – all
  properties from the template will be inherited in the new dimension. All
  dimension properties specified in the new dimension completely override the
  template specification
* added `point_cut_for_dimension`
* added `simple_model(cube_name, dimensions, measures)` – creates a single-cube
  model with flat dimensions from a list of dimension names and measures from
  a list of measure names. For example:

<pre class="prettyprint">
model = simple_model("contracts", ["year","contractor", "type"], ["amount"])
</pre>

*Slicer Server:*

* `/cell` – return cell details (replaces `/details`)

Changes
-------
* creation of a model from dictionary through `Model(dict)` is depreciated, use
  `create_model(dict)` instead. All initialization code will be moved there.
  Depreciation warnings were added. Old functionality retained for the time
  being. (**important**)
* Replaced `Attribute.full_name()` with `Attribute.ref()`
* Removed `Dimension.attribute_reference()` as same can be achieved with
  `dim(attr).ref()`
* `AggregationResult.drilldown` renamed to `AggregationResults.cells` (**important**)

Planned Changes:

* `str(Attribute)` will return ref() instead of attribute name as it is more
  useful
  
Fixes
-----

* order of dimensions is now preserved in the Model

Links
-----

Sources can be found on [github](https://github.com/Stiivi/cubes).
Read the [documentation](http://packages.python.org/cubes/).

Join the [Google Group](http://groups.google.com/group/cubes-discuss) for discussion, problem solving and announcements.

Submit issues and suggestions [on github](https://github.com/Stiivi/cubes/issues)

IRC channel [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net

If you have any questions, comments, requests, do not hesitate to ask.
