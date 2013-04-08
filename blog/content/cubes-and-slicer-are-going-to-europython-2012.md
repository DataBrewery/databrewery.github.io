Title: Cubes and Slicer are going to EuroPython 2012
Date: 2012-06-12
Tags: cubes, olap, talk, announcement
Category: cubes
Slug: cubes-and-slicer-are-going-to-europython-2012
Author: Stefan Urbanek
Summary: Cubes and Slicer are going to EuroPython 2012

<p>Cubes is going to <a href="https://ep2012.europython.eu/">EuroPython 2012</a>.</p>

<p><strong>EDIT:</strong> Added <a href="#needhelp"><em>&#8220;Need help?&#8221;</em></a>.</p>

<p><img src="http://media.tumblr.com/tumblr_m5ih17hv6w1qgmvbu.png" alt=""/></p>

<p>There are going to be <a href="https://ep2012.europython.eu/p3/schedule/ep2012/">two sessions</a>. First there will be <a href="https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server">talk</a> introducing to light-weight OLAP with Cubes and Slicer, on Friday at 9:45 in room Tagliatelle <a href="http://databrewery.org/downloads/cubes-europython2012-talk.ics">(add to calendar)</a>. Afterwards there will be longer, more in-depth and hands-on <a href="https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server-1">training</a> about Slicing and Dicing with Cubes on Friday at 14:30 in room Pizza Napoli <a href="http://databrewery.org/downloads/cubes-europython2012-training.ics">(add to calendar)</a></p>

<p>In the <a href="https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server">talk</a> I will introduce the framework and explain reasons for it&#8217;s existence. Then I will dig into architecture, features and briefly show examples how to use it for slicing and dicing. Newbies are welcome.</p>

<p>The <a href="https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server-1">training</a> will go into more details and the participants will learn:</p>

<ul><li>how to prepare data for aggregated browsing - star and snowflake schemas</li>
<li>how to create a logical model, define cubes, dimensions and hierarchies</li>
<li>how to browse aggregated data and how to slice and dice cubes from within
Python</li>
<li>how to create a WSGI OLAP server (&#8220;in 15 minutes&#8221; style) for aggregated data
browsing and how to use it in your web application for providing (browsable)
data to end-user reports</li>
<li>how to provide localized reporting</li>
</ul><p>If the time permits, we can look at the anatomy of the framework and see how
to implement a backend for another kind of data store.</p>

<p>I will be focusing on the existing SQL (relational OLAP) backend.</p>

<h2>Customized examples</h2>

<p>You might use the training session (and not only the session) to solve your
problem - just bring your own sample data, if you like.</p>

<p><img src="http://media.tumblr.com/tumblr_m5ifuiIMtX1qgmvbu.png" alt=""/></p>

<p>Do you have any data that you would like to slice and dice? Have a database
schema and do not know how to create a logical model? You can send me a data
sample or a schema, so I can prepare examples based on problem you are
solving.</p>

<p><em>Please, do not send any confidential data or schemas under NDA.</em></p>

<p><a name="needhelp"> </a></p>

<h2>Need help?</h2>

<p>If you have any questions or would like to help with your data: from data
preparation, through data modeling to slicing and dicing. You can grab me
during the whole event. If you can not find me, just tweet me:
<a href="https://twitter.com/#!/@stiivi">@Stiivi</a>.</p>

<h2>Participation</h2>

<p>If anyone is interested in participating in the project, he is welcome. Here are some features that are either out of scope of my skills and I would like to cooperate with someone more professional, or I do not have available resources to do that:</p>

<ul><li><a href="https://github.com/Stiivi/cubes.js">JavaScript</a> library</li>
<li><a href="https://github.com/Stiivi/cubes/issues/53">presenters, views and formatters</a></li>
<li>backends for other data stores (MongoDB was requested couple of times)</li>
<li>&#8230;</li>
</ul><p>I am also very open to new feature suggestions and feature change requests.
Just little note: Cubes is meant to be small and simple. At least for now.
There are plenty of complex and feature-rich solutions out there. If we can
make new, more complex features as non-critical, optional plug-ins, that would
be great.</p>

<h2>Links and Calendar Events</h2>

<p>You can add the talks to your calendar by following the links:</p>

<ul><li>Talk: <a href="https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server">description</a>, <a href="http://databrewery.org/downloads/cubes-europython2012-talk.ics">event</a> (.ics file)</li>
<li><p>Training: <a href="https://ep2012.europython.eu/conference/talks/cubes-light-weight-olap-framework-and-server-1">description</a>, <a href="http://databrewery.org/downloads/cubes-europython2012-training.ics">event</a> (.ics file)</p></li>
<li><p><a href="https://github.com/Stiivi/cubes">github</a> repository</p></li>
<li>project <a href="http://packages.python.org/cubes/">documentation</a></li>
<li><a href="http://groups.google.com/group/cubes-discuss">Google Group</a> for discussion, problem solving and announcements</li>
<li>IRC channel: <a href="irc://irc.freenode.net/#databrewery">#databrewery</a> on irc.freenode.net</li>
</ul>