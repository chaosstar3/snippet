
#ruby #webserver #sinatra #slim #cheatsheet

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
