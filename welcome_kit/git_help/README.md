# How to work collaboratively with Git

Each time you want to work on the repository: follow those steps : 


* Clone the repositery to your computer. Once you are in the wanted place and you have retrieve the http key, you can use the following line of code in your terminal : 
```
git clone https://github.com/Capgemini-Invent-France/starter-kit.git
```

* Retrieve the latest version :
```
git pull
```

* List all the branch, create a branch your developement and begin working on it : 
```
git branch -a 
git branch my_personal_branch
git checkout my_personal_branch
```

* Do you magic : coding, machone learning, alchimy... and then add the modification of the wanted file with :
```
git add new_file.py src/ml_pipeline.py test/*
```

* Then commit all your modification to your branch :
```
git commit -m "This is an explixit message that details the modification I am commiting" 
```

* You can also commit all the modified files at one time without adding them with :
```
git commit -a -m "I've coded something magic, check this out."
```

* You can check at any time the added and commited files with this command : 
```
git status
```

* Push your modifications to the remor repositery :
``` 
git push origin my_personal_branch
```
Github prompts you with a direct link for creating a merge request. Copy the link in you browser and create a merge request with github.com.