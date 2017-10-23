qrnr
====

`qrnr` is a tool that enables us to write parameterized queries in [the named paramstyle](https://www.python.org/dev/peps/pep-0249/) with help of [SQLAlchemy](http://www.sqlalchemy.org/develop.html), regardless of the database type.

Installation
------------

You can install this through `pip` package manager:

``` shell
$ pip install qrnr
```

You may further want to install database specific engines to use SQLAlchemy dialects. So if you want to use postgresql, you may want to run:

```shell
$ pip install psycopg2
```


Usage
-----

You can pass 3 options to `qrnr` command: `--url`, `--query` and `--parameters`:

- `--url` option (required): the SQLAlchemy URL of a database to connect to.
- `--query` option (required): the path to a file that contains SQL statements to run.
- `--parameters` option: the parameters to be used in running the query. The supplied argument must be in the following form: `name1:type1=value1[;name2:type2=value2;...]`
  See the following for the supported parameter types:


Parameter Types
---------------

Currently the following types are supported:

- int: the value supplied is parsed with `int` builtin
- double: parsed with `float` builtin
- text: parsed with `str` builtin
- date: parsed with the following function `lambda s: datetime.strptime(s, "%Y-%m-%d")`
- iso_ts: parsed with the following function: `lambda s: datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")`


Example
-------

Let's say we have the following statements in a single file:

``` sql
CREATE TABLE low_sales AS
SELECT
  *
FROM
  products
WHERE
    num_sold < :upper_limit
  AND
    created_date = :dt
;
```

The following would run the sql with two parameters `:upper_limit` and `:dt` substituted for an int `10` and a datetime object `2017-01-01`, respectively:

``` shell
$ qrnr --url ${url_for_db} --query /path/to/sql_above.sql --parameters 'dt:date=2017-01-01;upper_limit:int=10'
```


Motivation
----------

One may ask, "we can do this with command line tools that come with database distribution packages. What's the point?" The answer is:

Although we can do a similar thing with database CLI tools, it can be difficult to manage these queries (and jobs that use them) since each of the CLI tools uses a different way of specifying parameters. With this tool, we can always rely on the `named` paramstyle and can use the same interface for any database that has a SQLAlchemy dialect.
