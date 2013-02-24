Title: Overview
Date: 2013-02-24 17:00
Tags: cubes, python, framework
Category: cubes
Slug: overview
Author: Andrej Sykora
Summary: Overview of Cubes, Python data-analysis framework

<div class = "row content">

	<div class = "span12">
			<p class = "highlight">Light-weight Python framework and OLAP HTTP server for easy development of reporting applications and aggregate browsing of multi-dimensionally modeled data.</p>
		</div>

</div>

<!-- FEATURE BOXES -->
<div class = "row content">

<div class = "span5">
	<h2>Model</h2>
		<p>business and analyst's point of view on data</p>
		<ul>
			<li>Dimensions with multiple hierarchies</li>
			<li>User oriented metadata</li>
			<li>Dimension templates - define complex dimensions</li>
			<li>Localization of model and data</li>
		</ul>
		<p>
			<a href = "">[Read more]</a>
		</p>
</div>

<div class = "span5 offset2">
	<h2>Aggregated Browsing</h2>
	<p>easy development of exploration tools</p>
	<ul>
		<li>Slice and dice through dimensions</li>
		<li>Drill-down through any hierarchy</li>
		<li>Automatic next level selection, if desired</li>
		<li>Get dimension values or all facts within a cut</li>
	</ul>
	<p><a href = "">[Read more]</a></p>
</div>

</div>

<div class = "row content">

<div class = "span5">
	<h2>Backend and SQL</h2>
	<p>One of the backends shipped with the 
	framework is SQL. It is powered by the 
	SQLAlchemy which supports multiple 
	databases including PostgreSQL, MySQL, 
	Oracle, simple sqlite and many others.</p>
	<p>Features:</p>
	<p>Easy to prototype on top of existing, arbitrary 
	star or snowflake looking schemas.</p>
	<p>Logical-to-physical mapping that supports 
	multiple database schemas in databases 
	such as PostgreSQL or Oracle.</p>
	<p>Denormalization by view or materialized by 
	table.</p>
</div>

<div class = "span5 offset2">
	<h2>Slicer</h2>
	<p>Slicer - HTTP OLAP server for aggregation 
	queries</p>
	<p>Easy drilling-down, slicing and dicing
	Serves aggregates, dimension details, facts 
	and provides all necessary metadata for 
	reporting application</p>
	<p>Structured responses in JSON format with 
	rich metadata for easier application 
	development</p>
	<p>GET /aggregate?drilldown=date<br>
	GET /facts?cut=date:2010</p>
	<p><a href = "">[Read more]</a></p>
</div>

</div>