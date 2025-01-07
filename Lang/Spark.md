## Usage

### install
```sh
# https://spark.apache.org/downloads.html
wget https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3-scala2.13.tgz

# conf/spark-env.sh
export SPRAK_HOME=
export SPARK_DIST_CLASSPATH=<hadoop_path>
# https://spark.apache.org/docs/latest/configuration.html
```
### scala
> sbt new

`build.sbt`
```groovy build.sbt
val sparkVersion = "3.5.1"

lazy val root = (project in file("."))
	.settings(
		name := "App",
		libraryDependencies ++= Seq(
			"org.apache.spark" %% "spark-core" % sparkVersion,
			"org.apache.spark" %% "spark-sql" % sparkVersion,
			"org.scalameta" %% "munit" % "0.7.29" % Test,	
		),

		assembly / mainClass := Some("example.SparkApp"),
		assembly / assemblyJarName := s"${name.value}-${version.value}.jar"
		assembly / test := {},
	
		assembly assemblyMergeStrategy := {
			case "META-INF/MANIFEST.MF" => MergeStrategy.discard
			case _ => MergeStrategy.first
		},
	)
```
`plugin.sbt`
```groovy plugin.sbt
addSbtPlugin("com.eed3si9n" % sbt-assembly % "2.2.0")
```

```scala
package example
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.SparkSession

object SparkApp {
	def main(args: Array[String]): Unit = {
		val spark = SparkSession.builder().appName("MyApp").master("local[*]").getOrCreate()
		import spark.implicits._
		val df = List("Hello", "Spark").toDF()
		df.show(2, false)
	}
}
```
### run
> $SPARK_HOME/bin/spark-submit 
> 	--class com.example
> 	--name name 
> 	--master local[*]
> 	--deploy-mode client 
> 	test.jar
## overview
### background

- hadoop: 파일분할:HDFS + 분산처리:MapReduce + ClusterManger:yarn
- spark: process | RDD(Resilient Distributed Dataset): abstract
- Hive: warehouse, SQL on Hadoop

map/transform: input -> output
reduce: (map output 여러개, shuffle) -> result

mapreduce vs spark: 중간 단계를 파일로 저장 / 메모리

구조: https://spark.apache.org/docs/latest/cluster-overview.html
- Driver - SparkContext
- ClusterManager (hide)
- Worker Node - Executor(k8s, Yarn, Mesos) - task

API: SQL > DataFrame=Dataset\<Row> > Dataset > RDD / Streaming,MLlib,Graphs,SparkR,PySpark
lang: scala, java, python, R, SQL


실행
- spark-submit (shell)
> spark-submit --master=k8s
- SparkLauncher API
- Distributed SQL Engine: bin daemon
- 3rd party tool: zeppelin, jupyter

```scala
val sc = new SparkContext(conf)
rdd1 = sc.textFile
rdd2 = rdd1.map
rdd3 = rdd2.reduceByKey
```
### version
3.0 -> kerberos support -> hdfs
3.1 -> dynamic pvc (ceph)

### ETC
spark UI
### example
```scala
// RDD
val conf = new SparkConf().setAppName("name").setMaster("local")
val sc = new SparkContext()

var rdd = sc.textFile(path)
rdd.foreach(println)
rdd.saveAsTextFile(path) // -> directory part-

// Dataset
var spark = SparkSession.builder().appName("name").master("local").getOrCreate()
var ds = spark.read.textFile(path)
ds.show
ds.write.csv(path)
// import scala.implicits._ // encoder

// DataFrame
val df = spark.read.text(path)
df.show
df.write.csv(path)

// SQL
val df = spark.sql(sql)
df.createOrReplaceTempView("tmp")
sql("create table using `source` from tmp")
```

SparkSession.builder()
- appName = "name"
- master = `local[*]`, `local[50]` (50 task) 
- enableHiveSupport(): 자체 metastore

processing
- rdd.func(v -> )
- ds.func(v -> )
- df.func(row ->), df.selectExpr(expr)
- sql

dataset은 encoder 필요: import map(scala.implicits.\_, v)
dataframe은 row이므로 불필요

## Doc
### DataFrame

> import spark.implicits._
> import org.apache.spark.sql.functions._

RDD.map -> DF.select
Object -> Row
Function -> Expression(Column, Value)

r = Row(val1, val2, ..) //apply()
r.getInt(index)
StructType().add(StructField(name, Type)) -> GenericRowWithSchema

Encoder: internalRow로 수행 (spark 최적화)
> val encoder = ExpressionEncoder[(String, String, Int)]

df.hint() // join hint
df.explain

### RDD
Tip: create RDD

val data = List("1","2")
sc.parallelize(data) -> RDD
sc.range
sc.textFile

https://spark.apache.org/docs/latest/api/scala
API
- transform: RDD->RDD
	- map, mapPartitions, mapPartitionsWIthIndex, flatMap
- action: RDD->other
	- collect: collect(), take(), takeOrdered(), first(), top()
	- loop: foreach, foreachPartition
	- count: count, countByValue, countApporxDistinct, distinct, isEmpty
	- max,min
	- meta: id, context, toDebugString
	- cache: cache, persist, getStorageLevel, sc.setCheckpointDir, checkpoint
	- shuffle: getNumPartitions, partitions, repartition, coalesce

cache(): memory
checkpoint(): FS

partition

마지막에 compute()가 실행됨

### 구조
SparkContext - Job -> DAG Scheduler -> Stage -> Task


### stream
SparkStreaming
Structured Streaming: unbounded table

```scala
val df = spark.readStream
	.format("rate")//.option()
	.load()
//df.do_sth()
val query = df.writeStream
	.format("console")
	.start()
query.awaitTremination()
```

### tip
new CountDownLatch(1).await()
spark-shell --packages {dependency} --conf {conf}
## 3rd party
### zeppelin

코드로 html form 생성 가능

## Appendix 
### study
catalyst optimizer & project tungsten
