# Lending Tree web Scraper built with Scrapy, Selenium,  and hosted on scrapyrt
## About the Project
This spider was designed to accept requests from lendingtree.com URLs (https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183). It returns JSON data of the title of review, author, star rating, and date of review. To run queries on other lenders, it requires parameters cat= "/type_of_loan/name_of_lender/id" (ie: mortgage/silver-fin-capital-group/37405089). 

## Getting Started 
This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.
'''python
git remote add clone https://github.com/williamle92/lendingtree.git
'''
## Installation
1. Optional: Create a virtual environment using "python -m venv venv
2. "pip install -r requirements.txt" to the venv
3. To run commands on scrapyrt API [Scrapyrt](https://scrapyrt.readthedocs.io/en/stable/)
``` 
scrapyrt 
```
4. Enter the following code into your browser: 
```
http://127.0.0.1:9080/crawl.json?spider_name=lending_spider&start_requests=true&max_requests=5&crawl_args={"cat":"personal/marcus-by-goldman-sachs/65656551"}
```
5. To set a limit on a request add &max_request={int} 
```
http://127.0.0.1:9080/crawl.json?spider_name=lending_spider&start_requests=true&max_requests=5
```
6. To end session ctrl + c

## Contact
William Le williamkle92@gmail.com
