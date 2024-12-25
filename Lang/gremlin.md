## summary
Structure
![[https://tinkerpop.apache.org/docs/3.6.1/images/provider-integration.png]]
- gremlin server
- gremlin traversal language
- core API
- Graph DB(OLTP), Graph Processor(OLAP): spark

### Gremlin
gremlin이라는 traversal language 사용
- groovy 문법 (java, python, javascript, c# 포팅 용이함)
- general한 수준의 그래프 질의 가능 (traverse, centrality 등) https://tinkerpop.apache.org/docs/3.6.1/recipes/
- step이라는 function 파이프라인으로 traversing에 특화 (traversing에 있어선 cypher 보다 단계별 세밀한 설정이 가능할 듯)

### DB
- 크게 OLTP(Graph db), OLAP(Graph computer, (ex) spark) 두가지로 나뉘고 여러 DB 지원중 https://tinkerpop.apache.org/providers.html
- 기본으로는 tinkergraph라는 간단한 in-memory graph db 내장

#### tinkergraph
- no multilabel
-

### getting started
- tutorial
  - compendium https://tinkerpop.apache.org/docs/current/
    - getting started https://tinkerpop.apache.org/docs/3.6.1/tutorials/getting-started/
    - console: exmaple 3개
    - anatomy
    - recipes: centrality, detection
- documentation https://tinkerpop.apache.org/docs/current/reference/
  - 사용가능한 graph system https://tinkerpop.apache.org/providers.html
- learn practical
- explore more

gremlin console
- framework: tinkerpop
- lang: gremlin (groovy)
- engine: tinkergraph: in-memory, small handful, useful for subgraph from large graph

## usage
gremlin console 설치 https://www.apache.org/dyn/closer.lua/tinkerpop/3.6.1/apache-tinkerpop-gremlin-console-3.6.1-bin.zip

### gremlin lang
groovy 문법 (c#, java, javascript, python 포팅 용이)
```groovy
- Graph graph
  GraphFactory.open(...)
  TinkerGraph.open(...)         // 
  TinkerFactory. createClassic(),createModern(),createTheCrew() // example graph
- GraphTraversalSource g
  g = traversal().withEmbedded(graph)           //local OLTP
  g = traversal().withRemote(DriverRemoteConnection.using("Localhost",8182))  //remote
  g = traversal().withEmbedded(graph).withComputer(SparkGraphComputer.class)  //distributed OLAP

- cond: gt(v), within(v1,v2), neq(v), is(v)
- label: "multple::label"

- Steps (GraphTraversal instance)
  - Start steps
    - V([id]) - in()=inE().outV(), out()=outE().inV(), inE(), outE(), bothE()
    - E([id]) - inV(), outV()
    - addE(label).from(v1).to(v2), addV(label), inject(obj)
  - Terminal Steps
    - hasNExt(), next([num]), tryNext()
    - toList(), toKBulkSet(), fill(), iterate()   
  - general
    - map(), filter()
      - ex) map(it.get().value(prop)) == values(prop)
      - ex) properties(), property(key,val), values(), 
      - has([label,] prop, {cond}), hasLabel()
  - as(var)
  - and(), or(), not()
- Step Modulator: modify behavior of step
  - by()
- Anonymous Traversing
  - label() == __.label() == org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.label()
  - inV()
- 
  - list
    - mean()
    - where({cond})
    - group().by(label)
  - select(var1,var2,var3)
```
tinkerpop has no index management abstraction, utilize native API

cypher애서 안되는 것? [local step](https://tinkerpop.apache.org/docs/current/reference/#local-step)

### java library 사용 가능
``` groovy
import java.time.Year
Year.now()
```

centrality
```
```

```groovy
graph = TinkerGraph.open()
graph.createIndex('num', Vertex.class)
g = traversal().withEmbedded(graph)

new File('num_1m.csv').eachLine {
  (num, l, prop) = it.split('\t')
  g.addV(l).property('num', num).property('dummy', prop).next()
}
```

## neo4j 연동
### embedded
[Neo4j-Gremlin](https://tinkerpop.apache.org/docs/current/reference/#neo4j-gremlin)

```
# dependency 오류가 있는듯: lucene 부터 설치
:install org.apache.lucene lucene-backward-codecs 5.5.0
:install org.apache.tinkerpop neo4j-gremlin 3.6.1
:plugin use tinkerpop.neo4j
```
```groovy
graph = Neo4jGraph.open('/tmp/neo4j')
g = traversal().withEmbedded(graph)

new File('num_1m.csv').eachLine {
  (num, l, prop) = it.split('\t')
  g.addV(l).property('num', num).property('dummy', prop).next()
}
```

### remote(bolt)
neo4j-gremlin-bolt [maven](https://mvnrepository.com/artifact/com.steelbridgelabs.oss/neo4j-gremlin-bolt)
steelbridgelab이라는 곳에서 만든게 있는데, 현재 closed source인지 개발 안하는지 github 없어지고 fork만 남음

:install com.steelbridgelabs.oss neo4j-gremlin-bolt 0.2.27
//:install com.steelbridgelabs.oss neo4j-gremlin-bolt 0.4.6

```groovy
import static org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.__.*;
import com.steelbridgelabs.oss.neo4j.structure.*;
import com.steelbridgelabs.oss.neo4j.structure.providers.*;
import org.neo4j.driver.v1.*;

driver = GraphDatabase.driver("bolt://read-replica.napoli-ukg-dev.svc.cr1.io.navercorp.com:7687")
driver = GraphDatabase.driver("bolt://original.test54.svc.ad1.io.navercorp.com:7687")
driver = GraphDatabase.driver("bolt://localhost:7687", AuthTokens.basic('ongdb','test'))

a = ElementIdStrategy.build().create()
b = ElementIdStrategy.build().create()

vertexIdProvider = new Neo4JNativeElementIdProvider()
edgeIdProvider = new Neo4JNativeElementIdProvider()
graph = new Neo4JGraph(driver, vertexIdProvider, edgeIdProvider)
g = graph.traversal()

g.V(175524)
g.V(8342)

```

> :remote connect tinkerpop.server conf/remote.yaml


