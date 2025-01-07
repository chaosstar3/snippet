### template
```javascript
const template = document.querySelector("template");
const fragment = document.importNode(template.content, true);
const target = document.querySelector("target");
target.appendChild(fragment);
//
let newChild = target.lastElementChild;
```
