
#cheatsheet 

Embedded Tomcat
`TomcatConfig.java`
```java
package com.example.chipmunk;

import java.net.InetAddress;
import java.net.UnknownHostException;
import org.apache.catalina.connector.Connector;
import org.apache.coyote.ajp.AbstractAjpProtocol;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.*;
import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
import org.springframework.boot.web.servlet.server.ServletWebServerFactory;

@Configuration
public class TomcatConfig {

	private static final String PROTOCOL = "AJP/1.3";

	@Value("${tomcat.ajp.port}")
	private int ajpPort;

	@Bean
	public ServletWebServerFactory servletContainer() {

		TomcatServletWebServerFactory tomcat = new TomcatServletWebServerFactory ();

		Connector ajpConnector = new Connector(PROTOCOL);
		ajpConnector.setPort(ajpPort);
		ajpConnector.setAllowTrace(false);
		ajpConnector.setSecure(false);
		ajpConnector.setScheme("http");

		AbstractAjpProtocol<?> ajpProtocol = (AbstractAjpProtocol<?>) ajpConnector.getProtocolHandler();

		try {
			ajpProtocol.setAddress(InetAddress.getByName("0.0.0.0"));
		} catch (UnknownHostException e) {
			e.printStackTrace();
		}

		ajpProtocol.setSecretRequired(false);
		tomcat.addAdditionalTomcatConnectors(ajpConnector);
		return tomcat;
	}
}
```

tomcat.ajp.port=21001

`server.xml`
```
<Connector protocol="AJP/1.3" secret="" address="0.0.0.0" port="21001" redirectport="8443"
```

APACHE

config
- /etc/httpd
  - conf/httpd.conf
    - mod_proxy
      - ProxyPass "/", "ajp://host.docker.internal:port/"


### build with jk connector
```
sudo yum install httpd-devel automake

cd native
aclocal
automake
./configure --with-apxs=`which apxs`
aclocal
make

# apache-2.0/mod_jk.so
```

