## webserver
### sinatra
#ruby #slim
```sh
gem install sinatra thin slim
# web server: thin puma univorn webrick
``` 

```ruby web.rb
require 'sinatra'
require 'slim'

get '/' do
    slim :index
end
```

``` DIRECTORY
- views
    - index.slim
- public
    - css
    - js
```

### fastapi
#python
https://fastapi.tiangolo.com/#installation 
- /docs 지원
```sh
pip install "fastapi[standard]"

fastapi <dev|run> main.py
```

```python
from typing import Union
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}

@app.get("/echo")
def echo(req: Request):
	return dict(req.query_params)
```
### flask
#python
```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
	# request
	# - path, method
	# - input: args, data, json
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8081)
```
### python http
#python 
```sh
python -m http.server [PORT]      #python3
python -m SimpleHTTPServer [PORT] #python2
```

