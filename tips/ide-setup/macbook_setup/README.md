## Macbook setup installation scripts
<!-- Setup inspired by https://github.com/qchenevier/macbook_setup -->

### What does it do

to be completed

Installs and configures the following tools :
* terminal tools : iterm2, zsh, fzf
* coding tools: anaconda, python, spark, VSCode
* other : firefox

### Installation

to be completed

Launch this command in a terminal:
```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Capgemini-Invent-France/starter-kit/main/environment_setup/macbook_setup/install.sh)"
```

Manual actions needed:
- Press enter when asked to start installation by brew
- Type your password when asked to do so to change you default shell to zsh
- Type `exit` in zsh shell and enter to quit zsh, when it is launched
- Press 3 times enter when asked by fzf for automatic config
- Type your password when asked by brew to install anaconda (beware: pretty long installation (5 min) !)
- Click `Open` when asked by OSX to open atom
- Click on `Restore` when atom opens, Click `Yes` when asked to install dependencies for various installation, wait 2-3 minutes for completion of automatic configuration (when you see green popup with "Sync-settings finished installing XX packages."), then close atom window
- Type your password when asked by brew to install java8

### Tests & manual config

##### Manual config of `iterm`:
- open spotlight with `cmd-space`
- type `iterm`
- click `yes` to confirm opening of application
- click `open system preferences` when asked to give full disk access
  - go to `confidentiality` tab
  - select `full disk access` on the left
  - click on the padlock to enable modifications
  - click on the `+` sign and add iterm to list of applications with full disk access
  - quit iterm then relaunch it

##### Test terminal fuzzy search by fzf:
- test path fuzzy search by typing `cd ` in the shell then `ctrl-t` to enable fuzzy search of folders
- test reverse-history fuzzy search by typing `ctrl-r`

##### Test anaconda installation:

In your shell, type:
- `which python`: you should see something like `/usr/bin/python` (the default python installation on mac)
- `conda activate`: you should see in yellow the activation of your conda environment
- `which python`: you should see something like `/usr/local/anaconda3/bin/python` (the python installation by conda in default environment)
- `conda env list`: you should see only 1 environment

##### Test spark-shell:

In your shell, type:
- `spark-shell`
- quit it with `:q`

##### Test atom & hydrogen:
- activate your base conda environment: `conda activate`
- go to a folder where there is a python file: `cd ...`
- open atom: `atom .`
- select some python code and try to run it with: `shift+enter`

##### Test vscode & configure it:
- go to a folder where there is a git repository
- open vscode: `code .`
- go on "extensions" tab on the left (icon with square) and install:
  - `Python` to enable interactivity with python code & jupyter notebook close to atom+Hydrogen
  - `Gitlens`

### Tips & tricks:

##### git shortcuts:
- explore git shortcuts given by oh-my-zsh: https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git#aliases
- most useful ones:
  - `gss`
  - `gaa`
  - `gcam`

##### zsh shortcut:
`cs` shortcut: short for `cd` then `ls`

### Cleaning

to be completed
