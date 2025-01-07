# python

## venv
> python -m venv [env_name]
> source [env_name]/bin/activate
## pyenv
### install pyenv
> curl https://pyenv.run | bash
> export PYENV_ROOT=$HOME/.pyenv
> export PATH=PYENV_ROOT/bin:$PATH
### install python
> pyenv install -l
> pyenv install [python_version]
### use version
> python local [python_version]

# node
## nvm
> curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# manager
## sdkman
> curl -s "https://get.sdkman.io" | bash

## asdf
https://asdf-vm.com/guide/getting-started.html
> git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.15.0
zshrc
> . "$HOME/.asdf/asdf.sh"