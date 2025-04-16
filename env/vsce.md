https://code.visualstudio.com/api/get-started/your-first-extension

init
> npx --package yo --package generator-code -- yo code
> 
> npm i -g yo generator-code
> yo code

builder
> npm i -g @vscode/vsce

build
> vsce package

## test
#test #typescript
### mocha
```ts
import * as assert from 'assert';

describe('Tests', () => {
	it('test', () => {
		assert.equal(1, 1);
	})
})
```

```js
//.mocharc.js
"use strict"

module.exports = {
	require: ["ts-node/register'],
	extensiohns: ['ts'],
	spec: '/src/test/**/*.test.ts',
	timeout: 3000,
}
```