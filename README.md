# Techolution-Assignment
This repository acts as an assignment for first round of techolution hiring

## Approach
* As the given webpage is a rendered with Javascript, if we use requests library in python we can't extract the entire source code from the webpage. So, I used selenium and headless browser to render the page and then extract its source code. I used phantomjs as a browser in selenium and scraped the webpage.
* Once I got the source code, I selected the required data fields using xpath and class names, and then extracted the data into python lists.
* I used these list data structures to create a dictionary, then used this dictionary to create pandas dataframe.
* Then I sorted data in this df using number of days since posted as a key.
* Then I stored this dataframe into csv file.
