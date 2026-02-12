> java -cp "test-dependencies" org.junit.platform.launcher.cmd.Launcher --scan-classpath --include-classname=TestClass --include-methodname=TestMethod
# extensions
- tab-indent space-align
# vsce
https://code.visualstudio.com/api/get-started/your-first-extension

```sh
# pre-requisite
npx --package yo --package generator-code -- yo code
npm i -g yo generator-code
npm i -g @vscode/vsce

# init
yo code

# builder
npm i -g @vscode/vsce

# build
vsce package
```

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

## shortcut
when clause
https://dev.to/whitphx/find-vscodes-undocumented-when-clause-contexts-1p2g
```sh
grep -rni -E "RawContextKey(<.*>)?\('.*\)" src/* | sed -E "s/^.*RawContextKey(<.*>)?\(([^)]*)\).*/\2/" | sed -E "s/^.*RawContextKey(<.*>)?\(([^)]*)\).*/\2/" | sed -E "s/'([^']*)'.*/\1/" | uniq | sort
grep -rni -E "RawContextKey(<.*>)?\([^'].*\)" src/*
```
