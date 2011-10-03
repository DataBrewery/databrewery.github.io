---
layout:       default
body_id:      brewery
title:        Brewery
tagline:      data analysis and quality measurement
links:
    -
        title: Documentation
        url: http://packages.python.org/brewery
        icon: info_8x16.png
    -
        title: Node reference
        url: http://packages.python.org/brewery/node_reference.html
        icon: brewery-nodes.png
    -
        title: Sources at github
        url: https://github.com/stiivi/brewery
        icon: github_favicon.ico
    - 
        title: Google Group (mailing list)
        url: http://groups.google.com/group/databrewery
        icon: chat_16x16.png
    -
        title: Report Issues
        url: https://github.com/stiivi/brewery/issues
        
---

Brewery is a [Python](http://python.org) framework for data analysis and data quality measurement. The
framework uses streams of structured data that flow between processing nodes.

The framework consists of several modules:

* metadata – field types and field type operations, describe structure of data (available directly from the brewery package namespace)
* ds – structured data streams data sources and data targets
* streams – data processing streams
* nodes – analytical and processing stream nodes (see Node Reference)
* probes – analytical and quality data probes

Learn more:

* [Brewery Node reference](http://packages.python.org/brewery/node_reference.html "Node reference")
* [Brewery Examples](http://packages.python.org/brewery/examples/index.html "Brewery examples")
