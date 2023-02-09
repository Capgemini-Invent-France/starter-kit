# Predicting-readmission

Pipeline to predict if a patient will be readmitted in the following day or not or not. Huge focus put on the interpretability and on statistic dependance between features. 


## How to generate automatic documentation
The pydoc module automatically generates documentation from Python modules. The documentation can be presented as pages of text on the console, served to a web browser, or saved to HTML files.
It will use all the marckdown you completed to generate the documentation for each script and each function. 
You can use the following code to generate the docuemtation once you installed it with pop (""pip install pdoc3") and you created the a dedicated folder at the root : 
```
pdoc src -o docs --html
```