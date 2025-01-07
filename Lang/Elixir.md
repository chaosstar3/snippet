# tip
> IO.inspect(var)

# init
## install
https://elixir-lang.org/install.html#toc
### version manager

> asdf plugin add erlang https://github.com/asdf-vm/asdf-erlang.git
> asdf plugin-add elixir https://github.com/asdf-vm/asdf-elixir.git

[compatibility](https://hexdocs.pm/elixir/compatibility-and-deprecations.html#compatibility-between-elixir-and-erlang-otp)

> asdf install erlang 27.2
> asdf install elixir 1.18.1-otp-27

## project
> mix new PATH(.)

> mix deps.get

# doc
## type
int, float, boolean, atoms(symbol), string, list, tuple / nil

> :true == true => true

string
- concat `<>`
- interpolation "#{var}"
- String.split("")
list
- hd(): head, tl(): tail

IO: File.read("path/to/file") => {:ok, "... contents ..."}

## syntax
operator
- `=`: match
- `^`: pin
case, cond, if / do / end

### module
alias: module alias
require: module macro
import: import functions without prefix
use: invoke custom code


# framework
## web

pheonix
- Plug lib: web server adapter, official
	- cowboy: erlang http server
	- bandit: elixir http server
- router module
- .ex module: elixir modules
- ecto lib: DB
- EEx: html template

