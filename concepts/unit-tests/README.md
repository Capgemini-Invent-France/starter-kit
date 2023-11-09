# Unittest

This module allows you to introduce the notion of unit tests in a theoretical and practical way
<br>
## Some examples of tests in development

- Unit tests: Ensure that an isolated function works properly
- Integration: Make sure that the different blocks of an application react well to each other
- Acceptance: Ensure that the application meets business expectations

<br>

## Why perform unit tests?

- To ensure the proper functioning of each part of the code (Divide and conquer)
- Reduce the number of bugs and the time to resolve them
    - Detect and identify errors earlier
    - Validate fixed bugs
- Structure and improve code quality (scalable, maintainable..)
    - Integrate case management / exception handling
    - Refactoring and reduction of regression risk
    - Industrialization of development (need to create atomic functions, etc..)

<br>

## How to structure a unit test?

- Methodology:
    - Arrange: Define the test input variables and the expected result
    - Act: Call the function to test on the defined inputs
    - Assert: Compare the result with the expected resul
- Python libraries:
    - Unittest (integrated)
    - Pytest

## Useful documentation 

- Pytest official documentation : https://docs.pytest.org/en/7.2.x/
- Clear explanation on the fixture decorator : https://openclassrooms.com/fr/courses/7155841-testez-votre-projet-python/7414196-utilisez-les-fixtures