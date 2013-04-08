Title: bogus 3
TextBox: box_streams
Row: 2
Type: half
Parent: index
Status: hidden

## Streams ##

Data are treated as file-like objects where structured data is being passed instead of bytes.

* Comma separated values (CSV) file/URI resource
* MS Excel spreadsheet
* Google Spreadsheet
* Relational database table
* MongoDB database collection
* Directory containing yaml files - one file per record

[Read more](http://pythonhosted.org/brewery/stores.html) about stores.

### Streams and Higher Order Messaging ###

Processing network is described as Stream composed of connected processing nodes. Besides traditional network construction there is an option to use higher order messaging to construct a stream:

<pre class="prettyprint">
audit = Stream().fork()

audit.sample(1000)
audit.audit()
audit.formatted_printer()

audit.run()
</pre>
