## init
### Spring Initializr
- group: com.example.group
- artifact -> rootProject.name, com.example.group.artifact
- name -> {Name}Application
#### curl
> options: curl https://start.spring.io
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
#### spring boot cli
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
#### spring cli
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
### build env
- vscode Spring Boot Extension Pack
	- Language support for Java
	- Test Runner for Java
	- Debugger for Java
	- (Project Manager for Java)
- devtools auto restart command line
> 	gradle build --continuous
> 	gradle bootrun

## configs 
#### lombok
```groovy
// #!build.gradle
compileOnly 'org.projectlombok:lombok'
annotationProcessor 'org.projectlombok:lombok'

testCompileOnly 'org.projectlombok:lombok'
testAnnotationProcessor 'org.projectlombok:lombok'
```
### batch 
#cheatsheet 
```groovy
// #!build.gradle
implementation 'org.springframework.boot:spring-boot-starter-batch'
runtimeOnly 'com.h2database:h2'
```
```properties
# application.properties
#spring.batch.job.name=job
#datasource.batch.driverClass=org.h2.Driver
#datasource.batch.jdbc-url=jdbc:h2:mem:sb;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
```
```java
// JobConfig.java
import org.springframework.batch.core.ExitStatus;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.StepExecution;
import org.springframework.batch.core.StepExecutionListener;
import org.springframework.batch.core.configuration.annotation.JobScope;
import org.springframework.batch.core.job.builder.JobBuilder;
import org.springframework.batch.core.repository.JobRepository;
import org.springframework.batch.core.step.builder.StepBuilder;
import org.springframework.batch.item.ItemReader;
import org.springframework.batch.item.file.builder.FlatFileItemReaderBuilder;
import org.springframework.batch.item.file.mapping.DefaultLineMapper;
import org.springframework.batch.repeat.RepeatStatus;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.FileSystemResource;
import org.springframework.lang.NonNull;
import org.springframework.transaction.PlatformTransactionManager;
 
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Configuration
@RequiredArgsConstructor
public class JobConfig {
	final JobRepository jobRepository;
	final PlatformTransactionManager transactionManager;

	@Bean
	public Job job(
		@Qualifier("taskletStep") Step taskletStep,
		@Qualifier("rpwStep") Step rpwStep
	) {
		return new JobBuilder("job", jobRepository)
			.start(taskletStep)
			.next(rpwStep)
			.build();
	}
	
	@Bean
	@JobScope
	public Step taskletStep(
		@Value("#{jobParameters['param']}") String param
	) {
		return new StepBuilder("step", jobRepository)
			.tasklet((contribution, chunkContext) -> {
				log.info("Param: {}", param);
				return RepeatStatus.FINISHED;
			}, transactionManager)
			.build();
	}

	@Bean
	public Step rpwStep() {
		return new StepBuilder("step", jobRepository)
			.chunk(1000, transactionManager)
			.reader(fileReader())
			.processor(item -> item)
			.writer(chunk -> {})
			.listener(listener())
			.build();
	}

	private ItemReader<String> fileReader() {
		return new FlatFileItemReaderBuilder<String>()
			.name("fileReader")
			.resource(new FileSystemResource("a"))
			.lineMapper(new DefaultLineMapper<>())
			.build();
	}
	
	private StepExecutionListener listener() {
		return new StepExecutionListener() {
			@Override
			public void beforeStep(@NonNull StepExecution stepExecution) {
			stepExecution.getClass();
			
			}
			@Override
			public ExitStatus afterStep(@NonNull StepExecution stepExecution) {
				return ExitStatus.COMPLETED;
			}
		};
	}
}
```
```java
// Test.java
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.batch.core.BatchStatus;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.JobExecution;
import org.springframework.batch.core.JobParameters;
import org.springframework.batch.core.JobParametersBuilder;
import org.springframework.batch.test.JobLauncherTestUtils;
import org.springframework.batch.test.context.SpringBatchTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
@SpringBatchTest // JobLauncherTestUtils
class InitApplicationTests {
	@Autowired
	JobLauncherTestUtils jobLauncherTestUtils;

	@Test
	public void execute(@Qualifier("job") Job job) throws Exception {
		JobParameters jobParameters = new JobParametersBuilder()
			.addString("param", "param")
			.toJobParameters();

		jobLauncherTestUtils.setJob(job);
		JobExecution jobExecution = jobLauncherTestUtils.launchJob(jobParameters);

		Assertions.assertEquals(BatchStatus.COMPLETED, jobExecution.getStatus());
	}
}
```

### DB
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
### #checkstyle
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
#### #freemarker
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
