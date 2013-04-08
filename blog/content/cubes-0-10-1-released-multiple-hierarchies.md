Title: Cubes 0.10.1 Released - Multiple Hierarchies
Date: 2012-12-09
Tags: cubes, olap, release
Category: cubes
Slug: cubes-0-10-1-released-multiple-hierarchies
Author: Stefan Urbanek
Summary: Cubes 0.10.1 Released - Multiple Hierarchies

Quick Summary:

* multiple hierarchies:
  * Python: `cut = PointCut("date", [2010,15], hierarchy='ywd')` ([docs](http://packages.python.org/cubes/aggregate.html#multiple-hierarchies))
  * Server: `GET /aggregate?cut=date@ywd:2010,15` (see [docs](http://packages.python.org/cubes/server.html) - look for `aggregate` documentation)
  * Server drilldown: `GET /aggregate?drilldown=date@ywd:week`
* added result formatters (experimental! API might change)
* added pre-aggregations (experimental!)

New Features
------------

* added support for multiple hierarchies
* added `dimension_schema` option to star browser – use this when you have
  all dimensions grouped in a separate schema than fact table 
* added `HierarchyError` - used for example when drilling down deeper than
  possible within that hierarchy
* added result formatters: simple_html_table, simple_data_table, text_table
* added create_formatter(formatter_type, options ...)
* `AggregationResult.levels` is a new dictionary containing levels that the
  result was drilled down to. Keys are dimension names, values are levels.
* `AggregationResult.table_rows()` output has a new variable `is_base` to denote
  whether the row is base or not in regard to table_rows dimension.
* added `create_server(config_path)` to simplify wsgi script

* added aggregates: avg, stddev and variance (works only in databases that
  support those aggregations, such as PostgreSQL)

* added preliminary implemenation of pre-aggregation to sql worskspace:
  * `create_conformed_rollup()`
  * `create_conformed_rollups()`
  * `create_cube_aggregate()`

Server:

* multiple drilldowns can be specified in single argument:
  `drilldown=date,product`
* there can be multiple `cut` arguments that will be appended into single cell
* added requests: `GET /cubes` and `GET /cube/NAME/dimensions`


Changes
-------

* **Important:** Changed string representation of a set cut: now using
  semicolon ';' as a separator instead of a plus symbol '+'
* aggregation browser subclasses should now fill result's `levels` variable
  with `coalesced_drilldown()` output for requested drill-down levels.
* Moved coalesce_drilldown() from star browser to cubes.browser module to be
  reusable by other browsers. Method might be renamed in the future.
* if there is only one level (default) in a dimension, it will have same label
  as the owning dimension
* hierarchy definition errors now raise ModelError instead of generic
  exception

Fixes
-----

* order of joins is preserved
* fixed ordering bug
* fixed bug in generating conditions from range cuts
* `AggregationResult.table_rows` now works when there is no point cut
* get correct reference in `table_rows` – now works when simple denormalized
  table is used
* raise model exception when a table is missing due to missing join
* search in slicer updated for latest changes
* fixed bug that prevented using cells with attributes in aliased joined
  tables


Links
-----

Sources can be found on [github](https://github.com/Stiivi/cubes).
Read the [documentation](http://packages.python.org/cubes/).

Join the [Google Group](http://groups.google.com/group/cubes-discuss) for discussion, problem solving and announcements.

Submit issues and suggestions [on github](https://github.com/Stiivi/cubes/issues)

IRC channel [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net

If you have any questions, comments, requests, do not hesitate to ask.