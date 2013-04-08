Title: Cubes 0.7.1 released
Date: 2011-12-05
Tags: cubes, olap, announcement, release
Category: cubes
Slug: cubes-0-7-1-released
Author: Stefan Urbanek
Summary: Cubes 0.7.1 released

I am glad to announce new minor release of Cubes - Light Weight Python OLAP framework for multidimensional data aggregation and browsing. The news, changes and fixes are:
    
New Features
------------

* New method: Dimension.attribute_reference: returns full reference to an attribute
* str(cut) will now return constructed string representation of a cut as it can be used by Slicer

Slicer server:

* added /locales to slicer
* added locales key in /model request
* added Access-Control-Allow-Origin for JS/jQuery

Changes
-------

* Allow dimensions in cube to be a list, noy only a dictionary (internally it is ordered dictionary)
* Allow cubes in model to be a list, noy only a dictionary (internally it is ordered dictionary)

Slicer server:

* slicer does not require default cube to be specified: if no cube is in the request then try default from
  config or get first from model

Fixes
-----

* Slicer not serves right localization regardless of what localization was used first after server was
  launched (changed model localization copy to be deepcopy (as it should be))
* Fixes some remnants that used old Cell.foo based browsing to Browser.foo(cell, ...) only browsing 
* fixed model localization issues; once localized, original locale was not available
* Do not try to add locale if not specified. Fixes #11: https://github.com/Stiivi/cubes/issues/11

Tutorials
---------

Added tutorials in tutorials/ with models in tutorials/models/ and data in tutorials/data/:

* [Tutorial 1](http://blog.databrewery.org/post/12966527920/cubes-tutorial-1-getting-started): 
    * how to build a model programatically
    * how to create a model with flat dimensions
    * how to aggregate whole cube
    * how to drill-down and aggregate through a dimension
* [Tutorial 2](http://blog.databrewery.org/post/13255558153/cubes-tutorial-2-model-and-mappings): 
    * how to create and use a model file
    * mappings
* [Tutorial 3](http://blog.databrewery.org/post/13457860520/how-to-hierarchies-levels-and-drilling-down): 
    * how hierarhies work
    * drill-down through a hierarchy
* Tutorial 4 (not blogged about it yet):
    * how to launch slicer server


Links
-----

* github  **sources**: https://github.com/Stiivi/cubes
* **Documentation**: http://packages.python.org/cubes/
* **Mailing List**: http://groups.google.com/group/cubes-discuss
* Submit **issues** here: https://github.com/Stiivi/cubes/issues

If you have any questions, comments, requests, do not hesitate to ask.
