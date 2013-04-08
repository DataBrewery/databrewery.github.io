Title: Cubes 0.9 Released
Date: 2012-05-14
Tags: cubes, announcement, release
Category: cubes
Slug: cubes-0-9-released
Author: Stefan Urbanek
Summary: Cubes 0.9 Released

The new version of Cubes – light-weight [Python](http://www.python.org/) [OLAP](http://en.wikipedia.org/wiki/Online_analytical_processing) framework – brings new StarBrowser, which we discussed in previous blog posts:

* [mappings](http://blog.databrewery.org/post/22119118550), see also [documentation](http://packages.python.org/cubes/mapping.html)
* [joins and denormalization](http://blog.databrewery.org/post/22214335636)
* [aggregations and new features](http://blog.databrewery.org/post/22904157693), see also [documentation](http://packages.python.org/cubes/aggregate.html)

The new [SQL backend](http://packages.python.org/cubes/api/backends.html) is written from scratch, it is much cleaner, transparent, configurable and open for future extensions. Also allows direct browsing of star/snowflake schema without denormalization, therefore you can use Cubes on top of a read-only database. See [DenormalizedMapper](http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.mapper.DenormalizedMapper) and [SnowflakeMapper](http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.mapper.SnowflakeMapper) for more information.

![](static/images/cubes-0-9-released.png)

Just to name a few new features: [multiple aggregated computations](http://packages.python.org/cubes/aggregate.html#aggregations-and-aggregation-result) (min, max,...), [cell details](http://packages.python.org/cubes/aggregate.html#cell-details), optional/configurable [denormalization](http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.star.SQLStarWorkspace.create_denormalized_view).

Important Changes
-----------------

Summary of most important changes that might affect your code:

**Slicer**: Change all your slicer.ini configuration files to have [workspace]
section instead of old [db] or [backend]. Depreciation warning is issued, will
work if not changed.

**Model**: Change `dimensions` in `model` to be an array instead of a
dictionary. Same with `cubes`. Old style: `"dimensions" = { "date" = ... }`
new style: `"dimensions" = [ { "name": "date", ... } ]`. Will work if not
changed, just be prepared.

**Python**: Use Dimension.hierarchy() instead of Dimension.default_hierarchy.

New Features
------------

* slicer_context() - new method that holds all relevant information from 
  configuration. can be reused when creating tools that work in connected
  database environment
* added Hierarchy.all_attributes() and .key_attributes()
* Cell.rollup_dim() - rolls up single dimension to a specified level. this might
  later replace the Cell.rollup() method
* Cell.drilldown() - drills down the cell
* create_workspace(backend,model, **options) - new top-level method for creating a workspace by specifying backend name. Easier to create browsers (from
  possible browser pool) programmatically. The backend name might be full
  module name path or relative to the cubes.backends, for example
  `sql.star` for new or `sql.browser` for old SQL browser.
* get_backend() - get backend by name

* AggregationBrowser.cell_details(): New method returning values of attributes
  representing the cell. Preliminary implementation, return value might
  change.
* AggregationBrowser.cut_details(): New method returning values of attributes
  representing a single cut. Preliminary implementation, return value might
  change.
  
* Dimension.validate() now checks whether there are duplicate attributes
* Cube.validate() now checks whether there are duplicate measures or details

**SQL backend:**

* new [StarBrowser](http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.star.StarBrowser) implemented:
    * StarBrowser supports snowflakes or denormalization (optional)
    * for snowflake browsing no write permission is required (does not have to
      be denormalized)
* new [DenormalizedMapper](http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.mapper.DenormalizedMapper) for mapping logical model to denormalized view
* new [SnowflakeMapper](http://packages.python.org/cubes/api/backends.html#cubes.backends.sql.mapper.SnowflakeMapper) for mapping logical model to a snowflake schema
* ddl_for_model() - get schema DDL as string for model
* join finder and attribute mapper are now just Mapper - class responsible for
  finding appropriate joins and doing logical-to-physical mappings
* coalesce_attribute() - new method for coalescing multiple ways of describing
  a physical attribute (just attribute or table+schema+attribute)
* dimension argument was removed from all methods working with attributes
  (the dimension is now required attribute property)
* added create_denormalized_view() with options: materialize, create_index,
  keys_only
  
**Slicer tool/server:**

* slicer ddl - generate schema DDL from model
* slicer test - test configuration and model against database and report list 
  of issues, if any
* Backend options are now in [workspace], removed configurability of custom
  backend section. Warning are issued when old section names [db] and
  [backend] are used 
* server responds to /details which is a result of
  AggregationBrowser.cell_details()

**Examples:**

* added simple Flask based web example - dimension aggregation browser

Changes
-------

* in Model: dimension and cube dictionary specification during model
  initialization is depreciated, list should be used (with explicitly
  mentioned attribute "name") -- **important**
* **important**: Now all attribute references in the model (dimension
  attributes, measures, ...) are required to be instances of Attribute() and
  the attribute knows it's dimension
* removed `hierarchy` argument from `Dimension.all_attributes()` and `.key_attributes()`
* renamed builder to denormalizer
* Dimension.default_hierarchy is now depreciated in favor of
  Dimension.hierarchy() which now accepts no arguments or argument None -
  returning default hierarchy in those two cases
* metadata are now reused for each browser within one workspace - speed
  improvement.

Fixes
-----

* Slicer version should be same version as Cubes: Original intention was to
  have separate server, therefore it had its own versioning. Now there is no
  reason for separate version, moreover it can introduce confusion.
* Proper use of database schema in the Mapper



Links
-----

Sources can be found on [github](https://github.com/Stiivi/cubes).
Read the [documentation](http://packages.python.org/cubes/).

Join the [Google Group](http://groups.google.com/group/cubes-discuss) for discussion, problem solving and announcements.

Submit issues and suggestions [on github](https://github.com/Stiivi/cubes/issues)

IRC channel [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net

If you have any questions, comments, requests, do not hesitate to ask.

