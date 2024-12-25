1. Spring Initializer
https://start.spring.io/

Gradle Kotlin 2.4.2 Jar 11
- Spring Web
- Spring Boot DevTools

- Mustache
- Spring Data JPA
- H2 Database

2. build env
vscode Spring Boot Extension Pack

devtools auto restart command line
> gradle build --continuous
> gradle bootrun

livereload

## configs 

lombok
```groovy
// #!build.gradle
compileOnly 'org.projectlombok:lombok'
annotationProcessor 'org.projectlombok:lombok'

testCompileOnly 'org.projectlombok:lombok'
testAnnotationProcessor 'org.projectlombok:lombok'
```

batch
```groovy
// #!build.gradle
runtimeOnly 'com.h2database:h2'
```

test
```groovy
testRuntimeOnly 'org.junit.platform:junit-platform-launcher'
testImplementation 'org.assertj:assertj-core'

test {
	useJUnitPlatform()
	doFirst {
		// commandLineIncludePatterns: coomand line --tests
		// includePatterns: intellij
		if(filter.commandLineIncludePatterns.empty && filter.includePatterns.empty) {
			exclude "**/excludeDir/**"
		}
	}
	testLogging {
		events "passed", "skipped", "failed"
	}
}
```

#checkstyle
```groovy
id 'checkstyle'

checkstyle {
	// maxwarnings = 0
	configFile = file("")
	configProperties ["org.checkstyle.google.supressionfilter.config": ""]
	toolVersion = "10.17.0"
}
```

#freemarker
```groovy
// #!build.gradle
implementation 'org.springframework.boot:spring-boot-starter-freemarker'
```
``` properties
#!application.properties
## https://docs.spring.io/spring-boot/docs/1.1.0.M2/reference/html/common-application-properties.html
spring.freemarker.template-loader-path=file:src/main/resources/template
#spring.freemarker.template-loader-path=classpath:/template
spring.freemarker.prefix=/freemarker/
spring.freemarker.suffix=.ftl
spring.freemarker.contentType=text/html
spring.freemarker.charset=UTF-8
spring.freemarker.cache=false
```

```java
import org.springframework.web.servlet.view.freemarker.FreeMarkerConfigurer;
 
@Configuration
public class FreemarkerConfiguration {
    public FreemarkerConfiguration(freemarker.template.Configuration config) throws TemplateModelException {
        config.setSharedVariable("Hello", "Config");
    }
}
```

# Doc

특징
- IoC (Inversion of Control)
- AOP (Aspect-Oriented Programming)
- lightweight container
- Dependency Injection
- POJO (Plain Old Java Object)

구조
```
    | ORM | Web     |
AOP | ------------- | MVC
    | DAO | Context |
--------------------------
         core
```
