### template
```javascript
const template = document.querySelector("template");
const fragment = document.importNode(template.content, true);
const target = document.querySelector("target");
target.appendChild(fragment);
//
let newChild = target.lastElementChild;
```
### fetch
```ts
const response = await fetch(url);
if (!response.ok) {
	throw new Error(`${response.status}`);
}

const json = await response.json();
console.log(json)
```