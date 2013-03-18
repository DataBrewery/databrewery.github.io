Title: Data Types: From Storage to Analysis 
Date: 2012-08-14
Tags: brewery, data, metadata
Category: brewery
Slug: data-types-from-storage-to-analysis
Author: Stefan Urbanek
Summary: Data Types: From Storage to Analysis 

<p>What is the data type of 10? Depends on who you are, what are you going to do with it. I would expect my software friends to say that it is an &#8220;integer&#8221;. Why this information might not be sufficient or not relevant? How analysts see the data?</p>

<h2>Storage Data Type</h2>

<p>If we say &#8220;data type&#8221;, engineers would name types they know from typed programming languages: small integer, double precision float, character. This data type comes from how the data are stored in memory. The type specifies what operations can be done with the data stored at that particuliar place and how much memory is taken. To add two integers on an Intel processor there is an instruction called <code>ADD</code>, to add two floats there is a different instruction called <code>FADD</code> (Dear kids: this used to be on a separate chip in PCs!). To add an integer with an float, there has to be a conversion done. Database people would say <code>decimal</code>, <code>date</code> or <code>string</code>. Same as with memory data types, each type has it&#8217;s allowed set of operations and size it takes in the database. They both are of one kinds of data types: <em>storage data types</em>.</p>

<p><em>Storage data type</em>, as the name suggests, is used by software (compiler, database system) to know how much memory it takes to store the value of that type and to select appropriate operations (or operation variants).</p>

<h2>Concrete vs. Generic</h2>

<p>The number of storage data types and their differentiation is exhausting. To name a few:</p>

<ul><li><a href="http://en.wikipedia.org/wiki/C_data_types">C language</a> has more than 25 concrete numeric types and differentiates by floatness, size and sign flag</li>
<li><a href="http://www.postgresql.org/docs/9.1/static/datatype-numeric.html#DATATYPE-INT">PostgreSQL</a> has 9 numeric types, differentiates by size and floatness</li>
<li><a href="http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html">NumPy</a> differentiates not only by size and sign, but also by byte order</li>
</ul><p>Do I need all taht information about data type when working with data? In most cases I don&#8217;t, it is information for machine, not for me as data analyst/scientist. There are cases when knowing about data types might be handy, like optimisation (for memory consumption for example) or error prevention (of some kind) by type checking in typed languages.</p>

<p>For simplification, some tools use generic data types and hide the concrete storage type: <code>integer</code>, <code>float</code> (or <code>real</code>), <code>string</code>, &#8230; No storage size, no byte order. Those are low level details.</p>

<p>For reading the data, no input from user is required, as <code>short int</code> is integer and <code>double</code> is real. Problem with generic data types is that there might be multiple options how to store a generic <code>integer</code>.</p>

<h2>Analytical Data Types</h2>

<p>When doing data analysis I think about variable values and what I can do with them. In data analysis adding two integers or two floats is the same. It is just <code>a + b</code>. There is only one kind of addition: <code>+</code> (remember the <code>ADD</code> and <code>FADD</code>?). However, there might be numbers that adding them together will have no meaning, like adding two invoice numbers or years together.</p>

<p>To specify how the values should be treated during data analysis, there is another kind of data type: <em>analytical data type</em> or also called <em>variable types</em>. They are:</p>

<dl><dt><strong>Set</strong> (or Nominal Variable)</dt>
<dd>Values represent categories, like colors or contract. types. Fields of
this type might be numbers which represent for example group numbers, but have
no mathematical interpretation. For example addition of years 1989 and 2012
has no meaning.</dd>

<dt><strong>Ordered Set</strong> (or Ordinal Variable)</dt>
<dd>Similar to set field type, but values can be ordered in a meaningful order.</dd>

<dt><strong>Flag</strong> (or Binary)</dt>
<dd>Special case of set type where values can be one of two types, such as 1 or 0, ‘yes’ or ‘no’, ‘true’ or ‘false’.</dd>

<dt><strong>Discrete</strong></dt>
<dd>Set of integers - values can be ordered and one can perform arithmetic operations on them, such as: 1 apple + 2 apples = 3 apples.</dd>

<dt><strong>Range</strong></dt>
<dd>Numerical value, such as financial amount, temperature</dd>
</dl><p>The analytical data types are disstinct from storage data types. Take for example just an integer: it can be from a set without any arithmetic operations (ID, year), can be a discrete number (count of something), a flag with binary values of <code>40</code> and <code>50</code>. Integer as a set can be ordered as set of product sizes or unordered as kind of IDs or category numbers where categories are ordered by their names rather.</p>

<p>In addition to the mentioned data types, it is sometimes useful to specify that the tool or algorithm should just ignore a field/column/variable. For that purpose <strong>typeless</strong> analytical data type might be used.</p>

<p>Here is an example of storage and analytical data types:</p>

<p><img src="http://media.tumblr.com/tumblr_m8pz2eAz8i1qgmvbu.png" alt=""/></p>

<p>The idea behind analytical data types is described for example in nice introductory data mining book [1] or also in [2]. [1] differentiates measures as interval-scaled variables and ratio-scaled variables. Interesting that [2] describes the &#8220;set&#8221;, which they call &#8220;categorical variable&#8221; as &#8220;generalization of the binary in that it can take one more than two states&#8221;, not the other way around.</p>

<p>[1] Max Bramer: <a href="http://books.google.sk/books?id=xVW7NslHNHsC&amp;lpg=PP1&amp;ots=WjUU2gy5Zn&amp;dq=principles%20of%20data%20mining&amp;hl=sk&amp;pg=PP1#v=onepage&amp;q=principles%20of%20data%20mining&amp;f=false"><em>Principles of Datamining</em></a>, Springer Verlag London United 2007, p12.</p>

<p>[2] Jaiwen Wan and Micheline Kamber: <a href="http://books.google.sk/books?id=AfL0t-YzOrEC&amp;lpg=PP1&amp;ots=UvWVzPetD2&amp;dq=Data%20Mining%20-%20concepts%20and%20techniques&amp;pg=PP1#v=onepage&amp;q=Data%20Mining%20-%20concepts%20and%20techniques&amp;f=false"><em>Data Mining - concepts and techniques</em></a>, Elsevier 2006, p392.</p>

<h2>Keep the metadata with you</h2>

<p>As data are passed through algorithms, blocks of processing code, data types (along with other relevant metadata) should be passed with them. Data types can be in some cases guessed from data stream or explicitly expressed by a user, sometimes they can be reflected (like in a database). It is good to keep them, even if sometimes it is not possible to maintain accuracy or compatibility of data types between data sources and targets.</p>

<p>If done right, even after couple of transformations, one can say to an analytical metadata accepting function/algorithm: &#8220;get averages of this dataset&#8221; and it will understand it as &#8220;get averages of amounts in this dataset&#8221;.</p>

<p>Basic metadata that should be considered when creating data processing or data analysing interfaces are:</p>

<ul><li>number of fields</li>
<li>field names (as analyst I rather refer by name than index, as field position might differ among source chunks sometimes)</li>
<li>field order (for tabular data it is implicit, for document based databases it should be specified)</li>
<li>storage data types (at least generic, concrete if available or possible)</li>
<li>analytical datatype</li>
</ul><p>The minimal metadata structure for a dataset relevant to both: analysts who use data and engineers who prepare data would therefore be a list of tuples: (<em>name</em>, <em>storage type</em>, <em>analytical type</em>).</p>

<h2>Conclusion</h2>

<p>Typeless programming languages allow programmers to focus on structuring the data and remove the necessity of fiddling with physical storage implementation. Hiding concrete storage types from data analysts allows them to focus on properties of their data relevant to analysis. Less burden on mind definitely helps our thinking process.</p>

<p>Nevertheless, there are more kinds&#8230;</p>

<h2>Links</h2>

<p>Data Brewery <a href="http://packages.python.org/brewery/metadata.html">documentation</a> of metadata structures.</p>