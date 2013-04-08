Title: Cubes 0.8 Released
Date: 2012-03-09
Tags: cubes, announcement, olap
Category: cubes
Slug: cubes-0-8-released
Author: Stefan Urbanek
Summary: Cubes 0.8 Released

Another minor release of Cubes - Light Weight Python OLAP framework is out. Main change is that backend is no longer hard-wired in the [Slicer server](http://packages.python.org/cubes/server.html) and can be selected through configuration file.

There were lots of documentation changes, for example [the reference](http://packages.python.org/cubes/api/index.html) was separated from the rest of docs. [Hello World! example](https://github.com/Stiivi/cubes/tree/master/examples/hello_world) was added.

The news, changes and fixes are:

New Features
------------

* Started writing [StarBrowser](https://github.com/Stiivi/cubes/blob/master/cubes/backends/sql/star_browser.py) - another SQL aggregation browser with different 
  approach (see code/docs)

[Slicer Server](http://packages.python.org/cubes/server.html#configuration):

* added configuration option `modules` under `[server]` to load additional 
  modules
* added ability to specify backend module
* backend configuration is in [backend] by default, for SQL it stays in [db]
* added server config option for default `prettyprint` value (useful for 
  demontration purposes)

[Documentation](http://packages.python.org/cubes):

* [Changed license](http://blog.databrewery.org/post/18142294411) to MIT + small addition. Please refer to the LICENSE file.
* Updated documentation - added missing parts, made reference more readable, 
  moved class and function reference docs from descriptive part to reference 
  (API) part.
* added backend documentation 
* Added "[Hello World!](https://github.com/Stiivi/cubes/tree/master/examples/hello_world)" example

Changed Features
----------------

* removed default SQL backend from the server
* moved worskpace creation into the backend module

Fixes
-----

* Fixed create_view to handle not materialized properly (thanks to deytao)
* Slicer tool header now contains #!/usr/bin/env python

Links
-----

* github  **sources**: https://github.com/Stiivi/cubes
* **Documentation**: http://packages.python.org/cubes/
* **Mailing List**: http://groups.google.com/group/cubes-discuss
* Submit **issues** here: https://github.com/Stiivi/cubes/issues
* IRC channel: [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net

If you have any questions, comments, requests, do not hesitate to ask.
