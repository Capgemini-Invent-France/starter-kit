# Configs used for VSCode

Find here a list of recommended VSCode extensions and some settings we like.


### Black formater 
Black is a Python code formatter. It can be configured to automatically format your code whenever you save a file in VSCode.
First you need to install python in vs code threw the extensions panel on the left. 

Launch this command in a terminal:
```
pip install black
```

Open your VSCode settings, by going 'Code -> Preferences -> Settings'.
Search for "python formatting provider" and select "black" from the dropdown menu.
In the settings, search for "format on save" and enable the "Editor: Format on Save" option. 

Now each time you save .py file it will be automaticaly formatted. 
Alternatively you can try to run in your terminal :
'''
black folder_name/
'''
You can also use this command in your terminal to check the file that can be formatted : 
'''
black --check
'''