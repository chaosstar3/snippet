# Mysql

install
mysql community https://dev.mysql.com/downloads/mysql/
> https://dev.mysql.com/get/Downloads/MySQL-8.3/mysql-8.3.0-macos14-arm64.tar.gz

init
```sh
mysqld --initialize
mysqld --skip-grant-tables
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY ''
```
start
```sh
MYSQL_PATH=
#MYSQL_OPT="--secure-file-priv="
$MYSQL_PATH/bin/mysqld_safe $MYSQL_OPT &
```
stop
```sh
$MYSQL_PATH/bin/mysqladmin -uroot shutdown
```

use
#mysql #ruby #cs
```ruby
require 'mysql2'
@mysql = Mysql2::Client.new(host: host, port: 11306, username: user, password: pw)
sql=<<-SQL
	SELECT 1
SQL
@mysql.query(sql)
```
#mysql #pyhon #cs 
```python
import pymysql
conn = pymysql.connect(host=host, user=user, password=pw, db=db, charset='utr8')
cursor = conn.cursor()
cursor.execute("""
	SELECT 1
""")
cursor.fetchone()
```

Query
- LOAD DATA
```mysql
#SHOW VARIABLES LIKE 'secure_file_priv';
#SELECT @@GLOBAL.secure_file_priv;

LOAD DATA INFILE 'file_path'
INTO TABLE table
COLUMNS TERMINATED BY '\t'

```

# MongoDB

install
mongodb community https://www.mongodb.com/try/download/community
> https://fastdl.mongodb.org/osx/mongodb-macos-arm64-7.0.8.tgz

start
```sh
MONGO_PATH=
$MONGO_PATH/bin/mongod --logpath $MONGO_PATH/logs/mongodb.log --dbpath $MONGO_PATH/data --logappend --fork
```
stop
```sh
MONGOSH_PATH=
$MONGOSH_PATH/bin/mongosh --eval "db.shutdownServer()"
```

#mongodb #ruby #cs 
```ruby
require 'mongo'
Mongo::Logger.logger.level = Logger::ERROR
@mongo = Mongo::Client.new([hosts], user: user, password: pw, database: db)
col = @mongo[collection]
col.find({})
col.update_one({}, {})
```
#mongodb #python #cs 
```python
from pymongo import MongoClient
mongo = MongoClient(host=[], port)
col = mongo[collection]
col.find({})
```