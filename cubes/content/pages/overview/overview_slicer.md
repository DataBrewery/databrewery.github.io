Title: overview_slicer
TextBox: box_slicer
Row: 3
Column: 1
Type: half
Parent: index
Status: hidden

## Slicer ##

Slicer is a HTTP [OLAP cube](http://en.wikipedia.org/wiki/OLAP_cube) server
for aggregation queries.

* Easy drilling-down
* Slicing and dicing
* Serves aggregates, dimension details, facts
* Provides all necessary metadata for a reporting application

Structured responses are in JSON format with rich metadata for easier
reporting application development or reporting integration.

Example queries:

    GET /aggregate?drilldown=date\
    GET /facts?cut=date:2010


[[Read more]](http://pythonhosted.org/cubes/server.html)
