## init
- init svelte
```sh
# init svelte
npx sv create

# add-on
npx sv add tailwindcss prettier eslint vitest
```
### add-on
- [tailwindcss](https://tailwindcss.com/docs/guides/sveltekit)
- prettier: formatter
- eslint: lint
- vitest: unit test
- playwright: browser testing
- tailwindcss
- sveltekit-adapter: deployment
- drizzle: db orm
- lucia: auth guide
- mdsvex: +markdown
- paraglide: i18n
- storybook: fe workshop
### component
- [shadcn](https://www.shadcn-svelte.com/docs/installation/sveltekit)
- [lucide](https://lucide.dev/icons/)
- sass
```sh
npx shadcn-svelte@latest init
#npx shadcn-svelte@latest add button

npm add lucide-svelte

npm i -D sass 
```
## Develop
```sh
# dev
npm run dev

# build
npm run build
npm run preview
```
### Design
- class variable은 non_reactive -> type으로 정의 or toObject(
## Ref
### env 
https://svelte.dev/docs/kit/$env-static-private
```ts
import { MY_ENV_VAR } from '$env/static/private' // .env
```

```env
MY_ENV_VAR=VAR
```
### proxy
`vite.config.ts`
```ts
define Config{
	//...
	server: {
		proxy: {
			'/api': 'http://localhost:8080'
		}
	}
}
```
### static build
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

### DB
#### better-sqlite3
```sh
npm i better-sqlite3 @types/better-sqlite3
```
```ts
// lib/db.ts
import Database from 'better-sqlite3'
import { DB_PATH } from '$env/static/private' // .env

const db = new Database(DB_PATH, { verbose: console.log });
export default db;
```
```ts
//+page.server.ts
import type { PageServerLoad } from './$types';
import db from "$lib/db"

export const load = (async ({ params }) => {
	const stmt = db.prepare("SELECT 1");
	const rows = stmt.all();

	return {
		rows: rows
	}
}) satisfies PageServerLoad;
```
```ts
//+page.svelte
export let data: PageData;
console.log(data.rows);
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
+server.ts
```ts
import { json, fail, error } from "@sveltejs/kit";
import type { RequestHandler } from "./$types";

export const POST: RequestHandler = async ({ request }) => {
	const data = await request.json();
	//const data = await request.formData();
	if (data.ok) {
		return json({ success: true }, { status: 201 });
	} else {
		return fail(400, ""/*or {error: ""}*/);
		//return error(500, "");
	}
};
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
