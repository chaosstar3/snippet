## init
- init svelte
> npx sv create
- tailwindcss (https://tailwindcss.com/docs/guides/sveltekit)
> npm i -D tailwindcss postcss autoprefixer
> npx tailwindcss init -p
- shadcn (https://www.shadcn-svelte.com/docs/installation/sveltekit)
> npx shadcn-svelte@latest init
> npx shadcn-svelte@latest add button
- sass
> npm i -D sass 
- lucide
> npm add lucide-svelte

## Develop
> npm run dev
## Build
> npm run build
> npm run preview

# add
## proxy
`vite.config.ts`
```ts
defindConfig{
	//...
	server: {
		proxy: {
			'/api': 'http://localhost:8080'
		}
	}
}
```
## static build
https://svelte.dev/docs/kit/adapter-static
> npm i -D @sveltejs/adapter-static

`svelte.config.js`
```ts
import adapter from '@sveltejs/adapter-static';

export default {
	kit: {
		adapter: adapter({
			// default options are shown. On some platforms
			// these options are set automatically — see below
			pages: 'build',
			assets: 'build',
			fallback: undefined,
			precompress: false,
			strict: true
		})
	}
};
```
`src/routes/+layout.js`
```ts
export const prerender = true
```

# Doc
script module -> run once
script
style
## Routing

+page.svelte
```ts
import type { PageData } from './$types';
let { data }: { data: PageData } = $props();
```
+page.ts / +page.server.ts
```ts
import type { PageLoad } from './$types';

export const load: PageLoad = ({ params }) => { return {} }
```
+error.svelte
+layout.svelte
```html
<script>
	let { children } = $props();
</script>

{@render children()}
```

## Rune
prefix: $, keyword
- state: state 변수 만들기. proxy 사용
- derived
- effect
- props: component arg
- bindable
- inspect
- host
