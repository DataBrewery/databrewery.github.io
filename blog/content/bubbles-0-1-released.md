Title: Introducing Bubbles – virtual data objects framework
Date: 2013-06-22
Tags: bubbles, release
Category: bubbles
Slug: bubbles-0-1-released
Author: Stefan Urbanek
Summary: Introducing Bubbles – virtual data objects framework

After a while of silence, here is first release of Bubbles – virtual data
objects framework.

Motto: _Focus on the process, not the data technology_

Here is a short presentation:

<iframe src="http://www.slideshare.net/slideshow/embed_code/22475745" width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC;border-width:1px 1px 0;margin-bottom:5px" allowfullscreen webkitallowfullscreen mozallowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="http://www.slideshare.net/Stiivi/data-brewery-2-data-objects" title="Bubbles – Virtual Data Objects" target="_blank">Bubbles – Virtual Data Objects</a> </strong> from <strong><a href="http://www.slideshare.net/Stiivi" target="_blank">Stefan Urbanek</a></strong> </div>

Introduction
------------

I have started collecting functionality from various private data frameworks
into one, cleaning the APIs in the process. 

Priorities of the framework are:

* understandability of the process
* auditability of the data being processed (frequent use of metadata)
* usability
* versatility

Working with data:

* keep data in their original form
* use native operations if possible
* performance provided by technology
* have options

Bubbles is performance agnostic at the low level of physical data
implementation. Performance should be assured by the data technology and
proper use of operations.

What bubbles is not?

* Numerical or statistical data tool. Use for example
  [Pandas](http://pandas.pydata.org) instead.
* Datamining tool. It might provide data mining functionality in some sense,
  but that will be provided by some other framework. For now, use 
* All-purpose SQL abstraction framework. It provides operations on top of SQL,
  but is not covering all the possibilities. Use [Scikit Learn](http://scikit-learn.org/)
  [SQLAlchemy](http://www.sqlalchemy.org) for special constructs.


Data Objects and Representations
--------------------------------

Data object might have one or multiple representations. A SQL table might act
as python iterator or might be composed as SQL statement. The more abstract
and more flexible representation, the better. If representations can be
composed or modified at metadta level, then it is much better than streaming
data all around the place.

Operations
----------

Functionality of Bubbles is provided by operations. Operation takes one or
more objects as operands and set of parameters that affect the operation.
There are multiple versions of the operation – for various object
representations. Which operation is used is decided during runtime. For
example: if there is a SQL and iterator version and operand is SQL, then SQL
statement composition will be used.

Implementing custom operations is easy through an `@operation` decorator.

I will be talking about them in detail in one of the upcoming blog posts.

Here is a list:

<p  style=" margin: 12px auto 6px auto; font-family: Helvetica,Arial,Sans-serif; font-style: normal; font-variant: normal; font-weight: normal; font-size: 14px; line-height: normal; font-size-adjust: none; font-stretch: normal; -x-system-font: none; display: block;">   <a title="View Bubbles (Brewery2) - Operations on Scribd" href="http://www.scribd.com/doc/147247069/Bubbles-Brewery2-Operations"  style="text-decoration: underline;" >Bubbles (Brewery2) - Operations</a> by <a title="View Stefan Urbanek's profile on Scribd" href="http://www.scribd.com/stiivi"  style="text-decoration: underline;" >Stefan Urbanek</a></p><iframe class="scribd_iframe_embed" src="http://www.scribd.com/embeds/147247069/content?start_page=1&view_mode=scroll&access_key=key-2mk2lly8c12xagaxz0uh&show_recommendations=false" data-auto-height="true" data-aspect-ratio="0.706896551724138" scrolling="no" id="doc_85251" width="null" height="null" frameborder="0"></iframe><script type="text/javascript">(function() { var scribd = document.createElement("script"); scribd.type = "text/javascript"; scribd.async = true; scribd.src = "http://www.scribd.com/javascripts/embed_code/inject.js"; var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(scribd, s); })();</script>

Epilogue
--------

Bubbles comes as Python 3.3 framework. There is no plan to have Python 2
back-port.

Bubbles will follow: _'provide mechanisms, not policies'_ rule as much as it
will be possible. Even some policies are introduced at the early stages of the
framework, such as operation dispatch or graph execution, they will be opened
later for custom replacement.

Version 0.2 is already planned and will contain:

* processing graph – connected nodes, like in the old Brewery
* more basic backends, at least Mongo and some APIs
* _bubbles_ command line tool

Links
-----

Sources can be found on [github](https://github.com/Stiivi/bubbles).
Read the [documentation](http://packages.python.org/bubbles/).

Join the [Google Group](http://groups.google.com/group/databrewery) for discussion, problem solving and announcements.

Submit issues and suggestions [on github](https://github.com/Stiivi/cubes/issues)

IRC channel [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net

If you have any questions, comments, requests, do not hesitate to ask.

