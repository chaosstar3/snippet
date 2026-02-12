# init
https://nextjs.org/docs/app/getting-started/installation

```
npx create-next-app@latest
```


# structure
## routing
- Component
	- page.ts
	- route.ts: API Endpoint
	- layout.ts
	- template.ts
- Private dir
- Routing group


- syntactic sugar

```ts
// tsconfig.json: compilerOptions.paths."@/components/*"
import { Button } from '@/components/button'
```

## PAge
```ts
export default function Page() {
  return <h1>Hello Next.js!</h1>
}
```