#webserver

#ruby #sinatra #slim

> gem install sinatra thin slim

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

#python #flask
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