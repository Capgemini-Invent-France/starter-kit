# homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

###############################################
# terminal tools
###############################################
# iterm2 installation with custom fonts
brew tap homebrew/cask-fonts
brew cask install --force font-hack-nerd-font iterm2

# iterm2 configuration
mkdir -p $HOME/.iterm2
curl -fsSL https://raw.githubusercontent.com/Capgemini-Invent-France/starter-kit/main/environment_setup/macbook_setup/com.googlecode.iterm2.plist > $HOME/.iterm2/com.googlecode.iterm2.plist
defaults write com.googlecode.iterm2.plist PrefsCustomFolder -string "$HOME/.iterm2"
defaults write com.googlecode.iterm2.plist LoadPrefsFromCustomFolder -bool true

# zsh
brew install --force git zsh zsh-syntax-highlighting zsh-autosuggestions
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
curl -fsSL https://raw.githubusercontent.com/Capgemini-Invent-France/starter-kit/main/environment_setup/macbook_setup/.zshrc > $HOME/.zshrc

# fuzzy search in terminal
brew install --force fzf
$(brew --prefix)/opt/fzf/install

###############################################
# coding tools
###############################################
# frontend (javascript)
# brew install --force node

# backend (python)
brew cask install --force anaconda
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Capgemini-Invent-France/starter-kit/main/environment_setup/macbook_setup/configure_anaconda.sh)"
curl -fsSL https://raw.githubusercontent.com/Capgemini-Invent-France/starter-kit/main/environment_setup/macbook_setup/.pylintrc > $HOME/.pylintrc

# backend (spark)
brew tap homebrew/cask-versions
brew cask install --force java8
brew install --force scala apache-spark

# IDEs
brew cask install --force visual-studio-code
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Capgemini-Invent-France/starter-kit/main/environment_setup/macbook_setup/configure_vscode.sh)"
# brew cask install --force atom
# sh -c "$(curl -fsSL https://raw.githubusercontent.com/Capgemini-Invent-France/starter-kit/main/environment_setup/macbook_setup/configure_atom.sh)"

###############################################
# various tools
###############################################
brew cask install --force firefox
