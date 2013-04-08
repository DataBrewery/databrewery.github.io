Title: Cubes 0.9.1: Ranges, denormalization and query cell
Date: 2012-05-29
Tags: announcement, release, cubes, olap
Category: announcement
Slug: cubes-0-9-1-ranges-denormalization-query-cell
Author: Stefan Urbanek
Summary: Cubes 0.9.1: Ranges, denormalization and query cell

The new minor release of Cubes – light-weight [Python](http://www.python.org/)
[OLAP](http://en.wikipedia.org/wiki/Online_analytical_processing) framework –
brings range cuts,
[denormalization](http://packages.python.org/cubes/slicer.html#denormalize)
with the slicer tool and cells in `/report` query, together with fixes and
important changes.

See the second part of this post for the full list.

Range Cuts
----------

Range cuts were implemented in the SQL Star Browser. They are used as follows:

Python:

<pre class="prettyprint">
cut = RangeCut("date", [2010], [2012,5,10])
cut_hi = RangeCut("date", None, [2012,5,10])
cut_low = RangeCut("date", [2010], None)
</pre>

To specify a range in slicer server where keys are sortable:

<pre class="prettyprint lang-html">
    http://localhost:5000/aggregate?cut=date:2004-2005
    http://localhost:5000/aggregate?cut=date:2004,2-2005,5,1
</pre>

Open ranges:

<pre class="prettyprint lang-html">
    http://localhost:5000/aggregate?cut=date:2010-
    http://localhost:5000/aggregate?cut=date:2004,1,1-
    http://localhost:5000/aggregate?cut=date:-2005,5,10
    http://localhost:5000/aggregate?cut=date:-2012,5
</pre>

Denormalization with slicer Tool
--------------------------------

Now it is possible to denormalize tour data with the slicer tool. You do not
have to denormalize using python script. Data are denormalized in a way how
denormalized browser would expect them to be. You can tune the process using
command line switches, if you do not like the defaults.

Denormalize all cubes in the model:

<pre class="prettyprint lang-bash">
$ slicer denormalize slicer.ini
</pre>
    
Denormalize only one cube::

<pre class="prettyprint lang-bash">
$ slicer denormalize -c contracts slicer.ini
</pre> 

Create materialized denormalized view with indexes::

<pre class="prettyprint lang-bash">
$ slicer denormalize --materialize --index slicer.ini
</pre>

Example `slicer.ini`:

<pre class="prettyprint">
[workspace]
denormalized_view_prefix = mft_
denormalized_view_schema = denorm_views

# This switch is used by the browser:
use_denormalization = yes
</pre>

For more information see [Cubes slicer tool documentation](http://packages.python.org/cubes/slicer.html#denormalize)

Cells in Report
---------------

Use `cell` to specify all cuts (type can be `range`, `point` or `set`):

<pre class="prettyprint">
{
    "cell": [
        {
            "dimension": "date",
            "type": "range",
            "from": [2010,9],
            "to": [2011,9]
        }
    ],
    "queries": {
        "report": {
            "query": "aggregate",
            "drilldown": {"date":"year"}
        }
    }
}
</pre>

For more information see the [slicer server
documentation](http://packages.python.org/cubes/server.html#reports).

New Features
------------

* cut_from_string(): added parsing of range and set cuts from string;
  introduced requirement for key format: Keys should now have format
  "alphanumeric character or underscore" if they are going to be converted to
  strings (for example when using slicer HTTP server)
* cut_from_dict(): create a cut (of appropriate class) from a dictionary
  description
* Dimension.attribute(name): get attribute instance from name
* added exceptions: CubesError, ModelInconsistencyError, NoSuchDimensionError,
  NoSuchAttributeError, ArgumentError, MappingError, WorkspaceError and
  BrowserError

*StarBrowser:*

* implemented *RangeCut* conditions

*Slicer Server:*

* `/report` JSON now accepts `cell` with full cell description as dictionary,
  overrides URL parameters

*Slicer tool:*

* `denormalize` option for (bulk) denormalization of cubes (see the the slicer
  documentation for more information)

Changes
-------

* **important:** all `/report` JSON requests should now have queries wrapped in the key
  `queries`. This was originally intended way of use, but was not correctly
  implemented. A descriptive error message is returned from the server if the
  key `queries` is not present. Despite being rather a bug-fix, it is listed
  here as it requires your attention for possible change of your code.
* warn when no backend is specified during slicer context creation

Fixes
-----

* Better handling of missing optional packages, also fixes #57 (now works
  without slqalchemy and without werkzeug as expected)
* see change above about `/report` and `queries`
* push more errors as JSON responses to the requestor, instead of just failing
  with an exception

Links
-----

Sources can be found on [github](https://github.com/Stiivi/cubes).
Read the [documentation](http://packages.python.org/cubes/).

Join the [Google Group](http://groups.google.com/group/cubes-discuss) for discussion, problem solving and announcements.

Submit issues and suggestions [on github](https://github.com/Stiivi/cubes/issues)

IRC channel [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net

If you have any questions, comments, requests, do not hesitate to ask.
