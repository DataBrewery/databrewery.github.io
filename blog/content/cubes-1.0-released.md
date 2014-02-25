Title: Cubes 1.0 Released - Pluggable Data Warehouse
Date: 2014-02-20
Tags: cubes, olap, release
Category: cubes
Slug: cubes-1-0beta-released
Author: Stefan Urbanek
Summary: Cubes 1.0 Released – Pluggable Data Warehouse
Status: draft

It has been a year since the last release of Cubes and quite a lot has changed
since then. 

The changes are major, sometimes backward incompatible, but necessary for the
future direction of the Cubes.

There will be blog posts in the upcoming weeks which will have some examples
and will go into more details of cubes features.

Summary:

1. Analytical Workspace and Model Providers
2. Model Objects Redesign
3. HTTP API changes
4. New Backends
5. New SQL Backend Features
6. Authentication and Authorization

Detailed list of changes can be found here:

	http://cubes.databrewery.org/doc/releases/1.0.html

Analytical Workspace
--------------------

The biggest change is the Workspace – new concept of pluggable data-warehouse.
You are no longer limited to one one model, one type of data store (database)
and one set of cubes. The new Workspace is now framework-level controller
object that manages models (model sources), cubes and datastores. To the
future more features will be added to the workspace.

* Multiple models per workspace/server instead of only one
* Multiple backends per workspace/server instead of only one
* Multiple data stores per workspace/server instead of only one

![](static/images/cubes-1_0-workspace.png)

Models can now be generated or converted on-the-fly from another service with
the new concept of [Model Providers](http://cubes.databrewery.org/doc/extensions/providers.html
).

See also:
[Workspace](http://cubes.databrewery.org/doc/workspace.html),
[Providers](http://cubes.databrewery.org/doc/extensions/providers.html)

Model Objects Redesign
----------------------

Notable change is addition of new object: *Measure Aggregate*. Cubes now
distinguishes between *measures* and *aggregates*. measure represents a
numerical fact property, aggregate represents aggregated value (applied
aggregate function on a property, or provided natively by the backend). This
new approach of aggregates makes development of backends and clients much
easier. There is no need to construct and guess aggregate measures or
splitting the names from the functions. Backends receive concrete objects with
sufficient information to perform the aggregation (either by a function or
fetch already computed value).

Now you can name the "record_count" as you like or you might not have it at
all, if you do not like it.

More info about model can be found in the
[model documentation](http://cubes.databrewery.org/doc/model.html).

Other model changes:

* *cardinality* - metadata that helps front-end to determine which kind of UI
  item to use or might restrict hich-cardinality queries
* *dimension linking* – cubes can specify how the dimensions are going to be
  linked: specify what hierarchies are relevant to the cube, how what is the
  cardinality of dimension in the context of the cube and more.
* *roles* dimensions and levels can have roles – metadata that might make
  dims/levels be handled in a special way. Currently only the `time` role is
  implemented.

HTTP API Changes
================

The server end-points have changed. Concept of global model was dropped, now
there is just list of cubes. The front-end should approach the server in two
steps:

1. Get list of cubes with `/cubes` – only basic information, no structure
metadata
2. Get full cube model with `/cube/NAME/model`

Other changes:

* Many actions now accept `format=` parameter, which can be `json`, `csv`
or `json_lines` (new-line separated JSON).
* Cuts for date dimension accepts named relative time references such as
  `cut=date:90daysago-today`
* Dimension path elements can contain special characters if they are escaped
  by a backslash such as `cut=city:Nové\ Mesto`

[More info](http://cubes.databrewery.org/doc/server.html)

Backends
========

New backends:

* MongoDB (thanks to Robin Thomas)
* full implementation of the Slicer backend
* Mixpanel
* Google Analytics

With model providers you can easily create a backend for any other service
which serves cube-like data and plug it into your data warehouse.

SQL Features
============

Notable addition to the SQL backend are outer joins (finally!): three types of
joins were added to the SQL backend: match (inner), master (left outer) and
detail (right outer).

More info:

	http://cubes.databrewery.org/doc/backends/sql.html

Non-additive
------------

Provisional semi-additive time dimension support was added. An aggregate can
specify that it is non-additive through the time dimension (such as account
amount snapshots) and the generated query will handle the situation by
choosing the latest entry used.

The initial metadata infrastructure is in place. More flexible implementation
that will include other dimensions and element selection functions will be
introduced in the future releases.

Credit goes to Robin Thomas for this feature.

Authentication and Authorization
================================

Authentication at the server level and authorization at the workspace level.
The interface is extensible, so you can implement any method you like. The
built-in methods are pretty simple:

permissive authentication methods: pass-parameter – just pass api_key
parameter in the URL or Basic HTTP proxy – using username, ignoring password
(there is one for testing purposes called "adminadmin" ...)

authorization: JSON configuration for roles (inheritable) and rights.

The authorization has two parts: access to the cube and restriction cell for a cube.

More info:
	http://cubes.databrewery.org/doc/auth.html

Info for developers:
	http://cubes.databrewery.org/doc/extensions/auth.html


Links
-----

Most recent sources can be found on [github](https://github.com/Stiivi/cubes).
Read the [development documentation](http://cubes.databrewery.org/dev/doc).

Questions, comments, suggestions for discussion can be posted to the
[Cubes Google Group](http://groups.google.com/group/cubes-discuss) for discussion, problem solving and announcements.

Submit issues and suggestions
[on github](https://github.com/Stiivi/cubes/issues)

IRC channel [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net

