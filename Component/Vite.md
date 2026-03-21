## init
```sh
pnpm create vite@latest
```
## config
### proxy
`vite.config.ts`
```ts
export default defineConfig({
	//...
	server: {
		proxy: {
			'/api': 'http://localhost:8080',
		}
	}
})
