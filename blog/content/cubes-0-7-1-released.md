Title: Cubes 0.7.1 released
Date: 2011-12-05
Tags: cubes, olap, announcement, release
Category: cubes
Slug: cubes-0-7-1-released
Author: Stefan Urbanek
Summary: Cubes 0.7.1 released

<p>I am glad to announce new minor release of Cubes - Light Weight Python OLAP framework for multidimensional data aggregation and browsing. The news, changes and fixes are:</p>

<h2>New Features</h2>

<ul><li>New method: Dimension.attribute_reference: returns full reference to an attribute</li>
<li>str(cut) will now return constructed string representation of a cut as it can be used by Slicer</li>
</ul><p>Slicer server:</p>

<ul><li>added /locales to slicer</li>
<li>added locales key in /model request</li>
<li>added Access-Control-Allow-Origin for JS/jQuery</li>
</ul><h2>Changes</h2>

<ul><li>Allow dimensions in cube to be a list, noy only a dictionary (internally it is ordered dictionary)</li>
<li>Allow cubes in model to be a list, noy only a dictionary (internally it is ordered dictionary)</li>
</ul><p>Slicer server:</p>

<ul><li>slicer does not require default cube to be specified: if no cube is in the request then try default from
config or get first from model</li>
</ul><h2>Fixes</h2>

<ul><li>Slicer not serves right localization regardless of what localization was used first after server was
launched (changed model localization copy to be deepcopy (as it should be))</li>
<li>Fixes some remnants that used old Cell.foo based browsing to Browser.foo(cell, &#8230;) only browsing </li>
<li>fixed model localization issues; once localized, original locale was not available</li>
<li>Do not try to add locale if not specified. Fixes #11: <a href="https://github.com/Stiivi/cubes/issues/11">https://github.com/Stiivi/cubes/issues/11</a></li>
</ul><h2>Tutorials</h2>

<p>Added tutorials in tutorials/ with models in tutorials/models/ and data in tutorials/data/:</p>

<ul><li><a href="http://blog.databrewery.org/post/12966527920/cubes-tutorial-1-getting-started">Tutorial 1</a>: 

<ul><li>how to build a model programatically</li>
<li>how to create a model with flat dimensions</li>
<li>how to aggregate whole cube</li>
<li>how to drill-down and aggregate through a dimension</li>
</ul></li>
<li><a href="http://blog.databrewery.org/post/13255558153/cubes-tutorial-2-model-and-mappings">Tutorial 2</a>: 

<ul><li>how to create and use a model file</li>
<li>mappings</li>
</ul></li>
<li><a href="http://blog.databrewery.org/post/13457860520/how-to-hierarchies-levels-and-drilling-down">Tutorial 3</a>: 

<ul><li>how hierarhies work</li>
<li>drill-down through a hierarchy</li>
</ul></li>
<li>Tutorial 4 (not blogged about it yet):

<ul><li>how to launch slicer server</li>
</ul></li>
</ul><h2>Links</h2>

<ul><li>github  <strong>sources</strong>: <a href="https://github.com/Stiivi/cubes">https://github.com/Stiivi/cubes</a></li>
<li><strong>Documentation</strong>: <a href="http://packages.python.org/cubes/">http://packages.python.org/cubes/</a></li>
<li><strong>Mailing List</strong>: <a href="http://groups.google.com/group/cubes-discuss">http://groups.google.com/group/cubes-discuss</a></li>
<li>Submit <strong>issues</strong> here: <a href="https://github.com/Stiivi/cubes/issues">https://github.com/Stiivi/cubes/issues</a></li>
</ul><p>If you have any questions, comments, requests, do not hesitate to ask.</p>