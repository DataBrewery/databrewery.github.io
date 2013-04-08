Title: Cubes and Slicer are going to EuroPython 2012
Date: 2012-06-12
Tags: cubes, olap, talk, announcement
Category: cubes
Slug: cubes-and-slicer-are-going-to-europython-2012
Author: Stefan Urbanek
Summary: Cubes and Slicer are going to EuroPython 2012

Cubes is going to [EuroPython 2012](https://ep2012.europython.eu/).

**EDIT:** Added [*"Need help?"*](#needhelp).

![](static/images/cubes-and-slicer-are-going-to-europython-2012-1.png)

There are going to be [two sessions](https://ep2012.europython.eu/p3/schedule/ep2012/). First there will be [talk](https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server) introducing to light-weight OLAP with Cubes and Slicer, on Friday at 9:45 in room Tagliatelle [(add to calendar)](http://databrewery.org/downloads/cubes-europython2012-talk.ics). Afterwards there will be longer, more in-depth and hands-on [training](https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server-1) about Slicing and Dicing with Cubes on Friday at 14:30 in room Pizza Napoli [(add to calendar)](http://databrewery.org/downloads/cubes-europython2012-training.ics)

In the [talk](https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server) I will introduce the framework and explain reasons for it's existence. Then I will dig into architecture, features and briefly show examples how to use it for slicing and dicing. Newbies are welcome.

The [training](https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server-1) will go into more details and the participants will learn:

* how to prepare data for aggregated browsing - star and snowflake schemas
* how to create a logical model, define cubes, dimensions and hierarchies
* how to browse aggregated data and how to slice and dice cubes from within
  Python
* how to create a WSGI OLAP server ("in 15 minutes" style) for aggregated data
  browsing and how to use it in your web application for providing (browsable)
  data to end-user reports
* how to provide localized reporting

If the time permits, we can look at the anatomy of the framework and see how
to implement a backend for another kind of data store.

I will be focusing on the existing SQL (relational OLAP) backend.

Customized examples
-------------------

You might use the training session (and not only the session) to solve your
problem - just bring your own sample data, if you like.

![](static/images/cubes-and-slicer-are-going-to-europython-2012-2.png)

Do you have any data that you would like to slice and dice? Have a database
schema and do not know how to create a logical model? You can send me a data
sample or a schema, so I can prepare examples based on problem you are
solving.

*Please, do not send any confidential data or schemas under NDA.*

<a name="needhelp" id="needhelp">&nbsp;</a>

Need help?
----------

If you have any questions or would like to help with your data: from data
preparation, through data modeling to slicing and dicing. You can grab me
during the whole event. If you can not find me, just tweet me:
[@Stiivi](https://twitter.com/#!/@stiivi).

Participation
-------------

If anyone is interested in participating in the project, he is welcome. Here are some features that are either out of scope of my skills and I would like to cooperate with someone more professional, or I do not have available resources to do that:

* [JavaScript](https://github.com/Stiivi/cubes.js) library
* [presenters, views and formatters](https://github.com/Stiivi/cubes/issues/53)
* backends for other data stores (MongoDB was requested couple of times)
* ...

I am also very open to new feature suggestions and feature change requests.
Just little note: Cubes is meant to be small and simple. At least for now.
There are plenty of complex and feature-rich solutions out there. If we can
make new, more complex features as non-critical, optional plug-ins, that would
be great.

Links and Calendar Events
-------------------------

You can add the talks to your calendar by following the links:

* Talk: [description](https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server), [event](http://databrewery.org/downloads/cubes-europython2012-talk.ics) (.ics file)
* Training: [description](https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server-1), [event](http://databrewery.org/downloads/cubes-europython2012-training.ics) (.ics file)

* [github](https://github.com/Stiivi/cubes) repository
* project [documentation](http://packages.python.org/cubes/)
* [Google Group](http://groups.google.com/group/cubes-discuss) for discussion, problem solving and announcements
* IRC channel: [#databrewery](irc://irc.freenode.net/#databrewery) on irc.freenode.net
