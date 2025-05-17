# python

## venv
```sh
python -m venv [env_name]
source [env_name]/bin/activate
```
## pyenv
### install pyenv
```sh
curl https://pyenv.run | bash
export PYENV_ROOT=$HOME/.pyenv
export PATH=PYENV_ROOT/bin:$PATH
``` 
### install pyenv-win
https://github.com/pyenv-win/pyenv-win
```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
``` 
### install python
```sh
pyenv install -l
pyenv install [python_version]
```
### use version
```sh
python local [python_version]
```

# node
## nvm
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

# manager
## sdkman
```
curl -s "https://get.sdkman.io" | bash
```
## asdf
https://asdf-vm.com/guide/getting-started.html
```sh
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.15.0
zshrc
. "$HOME/.asdf/asdf.sh"
```
