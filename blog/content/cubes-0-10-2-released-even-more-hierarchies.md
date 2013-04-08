Title: Cubes 0.10.2 Released - Even More Hierarchies, Formatters and Docs
Date: 2013-02-20
Tags: cubes, olap, release
Category: cubes
Slug: cubes-0-10-2-released-even-more-hierarchies
Author: Stefan Urbanek
Summary: Cubes 0.10.2 Released - Even More Hierarchies, Formatters and Docs

After few months and gloomy winter nights, here is a humble update of the
Cubes light weight analytical framework. No major feature additions nor
changes this time, except some usability tweaks and fixes.

Documentation was updated to contain relational database patterns for SQL
backend. See the schemas, models and illustrations in the [official
documentation](http://pythonhosted.org/cubes/schemas.html).

Also improvements in cross-referencing various documentation parts through
see-also for having relevant information at-hand.

Thanks and credits for support and patches goes to:

* Jose Juan Montes (@jjmontesl) 
* Andrew Zeneski
* Reinier Reisy Quevedo Batista (@rquevedo)

Summary
=======

* many improvements in handling multiple hierarchies
* more support of multiple hierarchies in the slicer server either as
  parameter or with syntax `dimension@hierarchy`:
  - dimension values: `GET /dimension/date?hierarchy=dqmy`
  - cut: get first quarter of 2012 `?cut=date@dqmy:2012,1`
  - drill-down on hierarchy with week on implicit (next) level: `?drilldown=date@ywd`
  - drill-down on hierarchy with week with exlpicitly specified week level:
    `?drilldown=date@ywd:week`
* order and order attribute can now be specified for a Level
* optional safe column aliases (see docs for more info) for databases that
  have non-standard requirements for column labels even when quoted

New Features
------------

* added `order` to Level object - can be `asc`, `desc` or None for unspecified
  order (will be ignored)
* added `order_attribute` to Level object - specifies attribute to be used for
  ordering according to `order`. If not specified, then first attribute is
  going to be used.
* added hierarchy argument to `AggregationResult.table_rows()`
* `str(cube)` returns cube name, useful in functions that can accept both cube
  name and cube object
* added cross table formatter and its HTML variant 
* `GET /dimension` accepts hierarchy parameter
* added `create_workspace_from_config()` to simplify workspace creation
  directly from slicer.ini file (this method might be slightly changed in the
  future)
* `to_dict()` method of model objects now has a flag `create_label` which
  provides label attribute derived from the object's name, if label is missing
* Issue #95: Allow charset to be specified in Content-Type header


SQL:

* added option to SQL workspace/browser `safe_labels` to use safe column
  labels for databases that do not support characters like `.` in column names
  even when quoted (advanced feature, does not work with denormalization)
* browser accepts include_cell_count and include_summary arguments to
  optionally disable/enable inclusion of respective results in the aggregation
  result object
* added implicit ordering by levels to aggregate and dimension values methods
  (for list of facts it is not yet decided how this should work)
* Issue #97: partially implemented sort_key, available in `aggregate()` and
  `values()` methods 

Server:

* added comma separator for `order=` parameter
* reflected multiple search backend support in slicer server

Other:

* added vim syntax highlighting goodie

Changes
-------

* AggregationResult.cross_table is depreciated, use cross table formatter
  instead
* `load_model()` loads and applies translations
* slicer server uses new localization methods (removed localization code from
  slicer)
* workspace context provides proper list of locales and new key 'translations'
* added base class Workspace which backends should subclass; backends should
  use workspace.localized_model(locale)
* `create_model()` accepts list of translations

Fixes
-----

* browser.set_locale() now correctly changes browser's locale
* Issue #97: Dimension values call cartesians when cutting by a different
  dimension
* Issue #99: Dimension "template" does not copy hierarchies


Links
-----

Sources can be found on [github](https://github.com/Stiivi/cubes).
Read the [documentation](http://packages.python.org/cubes/).

Join the [Google Group](http://groups.google.com/group/cubes-discuss) for
discussion, problem solving and announcements.

Submit issues and suggestions [on github](https://github.com/Stiivi/cubes/issues)

IRC channel [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net

If you have any questions, comments, requests, do not hesitate to ask.
