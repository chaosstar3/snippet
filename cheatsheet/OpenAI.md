https://platform.openai.com/docs/api-reference/introduction

```python
import os
import openai

client = openai.OpenAI(
	api_key=os.environ.get("API_KEY")
	base_url="https://ENDPOINT"
)
```

```python
response = client.chat.completions.create(
	model = "llm/model"
	messages = [
		{
			"role": "system",
			"content": "Hello"
		},
		{
			"role": "user",
			"content": "Hello"
		},
	],
	#stream=True,
)

print(response.choices[0].message.content)
# for chunk in response: #strea m
```