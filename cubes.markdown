---
layout:       default
body_id:      cubes
title:        Cubes
tagline:      online analytical processing (OLAP)
links:
    -
        title: Documentation
        url: http://packages.python.org/cubes
        icon: info_8x16.png
    -
        title: Sources at github
        url: https://github.com/stiivi/brewery
        icon: github_favicon.ico
    - 
        title: Google Group (mailing list)
        url: http://groups.google.com/group/cubes-discuss
        icon: chat_16x16.png
    -
        title: Report Issues
        url: https://github.com/stiivi/cubes/issues

---

Cubes is a light-weight framework for online analytical processing (OLAP). Main features are
multidimensional analysis and star and snowflake schema preparation and abstraction.

Cubes comes with a HTTP OLAP server Slicer which provides API for multidimensional data browsing.

Modular architecture of cubes allows to write any kind of OLAP backend. Currently provided backend is SQL
star/snowflake browser for ROLAP and Slicer backend as example for abstracting over another Slicer server.

_Focus on data analysis, not on physical data structure_

Framework features:

* **model** — Logical Model - description of how data are being analysed and reported, independent of physical data implementation
* **hierarchical dimensions** (attributes that have hierarchical dependencies, such as category-subcategory or country-region)
* **localizable metadata** and data Localization

Introduction:
<div>
<iframe src="http://www.slideshare.net/slideshow/embed_code/7781602?rel=0" width="340" height="284" frameborder="0" marginwidth="0" marginheight="0" scrolling="no">&nbsp;</iframe>
</div>
