brew remove --force $(brew list) --ignore-dependencies
brew cask remove --force $(brew cask list)
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)" -- --force

rm -fr $HOME/.oh-my-zsh
rm $HOME/.zshrc