- httpd.conf
`/etc/httpd/conf/httpd.conf`
> ProxyPass "/" "ajp://host.docker.internal:21001/"

- jk connector 
[[AJP#build with jk connector]]

- /etc/httpd/conf.d/
`jk.conf`
```xml jk.conf
LoadModule jk_module modules/mod_jk.so

<IfModule jk_module>
  JkWorkersFile conf.d/workers.properties
  JkLogFile logs/mod_jk.log
  JkLogLevel info
  JkShmFile run/mod_jk.shm
  JkMountFile conf.d/uriworkermap.properties
</IfModule>
```
`worker.properties`
```properties workers.properties
worker.list=worker1
worker.worker1.type=ajp13
worker.worker1.host=host.docker.internal
worker.worker1.port=21001
```
`uriworkermap.properties`
``` uriworkermap.properties
/*=worker1
```
