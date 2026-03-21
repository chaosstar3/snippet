## Init
- group: com.example.group
- artifact
	- settings.gradle: rootProject.name
	- package: {group}.{artifact}
- name
	- {Name}Application
	- application.properties: spring.application.name={name}
### spring initializr 
> by curl
> https://start.spring.io 
```sh
curl https://start.spring.io/starter.zip \
	-d "groupId=com.example.group" \
	-d "artifactId=artifact" \
	-d "name=name" \
	-d "javaVersion=21" \
	-d "dependencies=batch,jdbc" \
	-d "baseDir=dir" \
	--output spring.zip
```
### spring boot cli
> install: sdkman 
> https://docs.spring.io/spring-boot/cli/using-the-cli.html
```sh
spring init \
	-g com.example.group \
	-a project \
	-n name \
	-j 21 \
	-d batch,jdbc \
	dir
```
### spring cli
> https://docs.spring.io/spring-cli/reference/index.html
```sh
java -jar spring-cli-0.10.0-SNAPSHOT.jar boot start \
	--group com.example.group \
	--artifact artifact \
	--name name \
	--package-name pkgname \
	--dependencies batch,jdbc \
	--java-version 21 \
	--path dir
```
### gradle init
```sh
gradle init \
  --type java-application \
  --dsl groovy \
  --test-framework junit-jupiter \
  --package com.example \
  --project-name project \
  --no-split-project \
  --java-version 21
```
## dev
- vscode Spring Boot Extension Pack
	- Language support for Java
	- Test Runner for Java
	- Debugger for Java
	- (Project Manager for Java)
- devtools auto build & restart
```
// build.gradle
developmentOnly 'org.springframework.boot:spring-boot-devtools'
// application.properties
spring.devtools.restart.enabled=true

// CLI
gradle build --continuous
gradle bootrun
```


## configs 
#### lombok
```groovy
// #!build.gradle
compileOnly 'org.projectlombok:lombok'
annotationProcessor 'org.projectlombok:lombok'

testCompileOnly 'org.projectlombok:lombok'
testAnnotationProcessor 'org.projectlombok:lombok'
```
#### dotenv  
```groovy  
bootRun {  
	doFirst {
		if (!file('.env').exists()) {
			throw new GradleException("need .env")
		}
	}
    systemProperty 'spring.config.import', 'optional:file:.env[.properties]'  
}  
```
### DB
JDBC(Low) - MyBatis - JPA(High)
#### mysql
```groovy

implementation 'org.springframework.boot:spring-bost-starter-jdbc'
implementation 'org.mybatis.spring.boot:mybatis-spring-boot-starter:$version'

runtimeOnly 'com.mysql:mysql-connector-j'
```
```properties
spring.datasource.url=jdbc:mysql://
spring.datasource.username=
spring.datasource.password=
```
### test
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
#### checkstyle
```groovy
id 'checkstyle'

checkstyle {
	// maxwarnings = 0
	configFile = file("")
	configProperties ["org.checkstyle.google.supressionfilter.config": ""]
	toolVersion = "10.17.0"
}
```
### lib
#### freemarker
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

# spring
## convention
### 디렉토리 구조
- 도메인형: 도메인 기준 디렉토리
- 계층형: controller, service, dao, dto 디렉토리
## Doc

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

## changes
#### 6.1
- Parameter Name Retention: `LocalVariableTableParameterNameDiscoverer` removed [#](https://github.com/spring-projects/spring-framework/issues/29559)
	- 기존 `-g` option (debug info)이 local variable를 못담음
	- use `-parameters` -> `StandardReflectionParameterNameDiscoverer`
	- gradle은 java plugin에서 -parameters를 추가
	- IDE는 -g 만 사용하여 java compile API를 호출
