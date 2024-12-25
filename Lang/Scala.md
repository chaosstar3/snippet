main

val: immutable
var: mutable

### Type
- Any: 최상위
	- AnyVal
		- num, String, Unit(void)
	- AnyRef
		- Class, Tuple, Seq, Array, List, Set, Map, 
- Null: 최하위
- Option
	- None
- function: type => type = () => {}

sum type {A} = {B, C}
product type: match case

### Syntax

assign
```scala
var a: type = 1
a = {1}
a = {
	1
}
```

generic `[T]`
array `arr(0)`

string interpolation: `s"hello ${name}"`


```scala
class MyClass {}
object MyObject {} // singleton

val obj = new MyClass()
obj.func()
MyObject.func()
MyObject() // MyObject.apply()
```

### function
func func() func{}
type inference: argument type 지정 안해도 알아서, 이름도 underscore`_`로 사용가능

companion object: 선언하면 변환가능 후보
> implicit aTob(a: A[Int]) =  new B

Currying argument 괄호 나눠서 받음
- {}는 argument 하나일때만 사용가능
