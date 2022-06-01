# Project 1

## AmazonBot 
AmazonBot is a class that inherits from Object. It has 3 main methods, and other supporting methods. The main methods are:
- scrapeproduct(self,product,pages=1)
- scrapepage(self,link)
- exportxlsx(self,path="",name='test1.xlsx')

The supporting methods are:
- __click(self,button)
- __getproductlinks(self,pages=1)
- getproductdelivery(self,start)
- getsellerfrom(self,e)
- __buyingoptions(self)
- getproductname(self)
- getproductpriceanddelivery(self)
- getoptions(self)
- get_path_option(self,option,var)
- get_product_overview_and_features(self)
- extract_reviews(self,reviews)
- get_product_reviews_and_rating(self,link)
- exportxlsx(self,path='',name='test1.xlsx')

# Explanation:
## Supporting Methods:
### 1. __click(self,button): 
The following method takes as an input parameter a clickable webelement (button or input) and clicks it. It handles the exceptions _StaleElementReferenceException_ and _ElementNotInteractableException_ exceptions .

### 2. __getproductlinks(self,pages=1) : 
The following method takes as an input parameter number of pages (int) to be scraped from. It stops and print a message to the command line when the maximum number of pages is reached. (It can also throw an exception when the maximum number of pages is reached. Just uncomment the assert and comment the following if and else statements)
### 3. getproductdelivery(self,start):
The following method takes as an input parameter start (string) which handles 2 seperate cases of delivery then returns the delivery details if available [(deliveryprice, deliverytime)].Else it returns the ["Unavailable message"]. 

### 4. getsellerfrom(self,e) :
The following method takes as an input parameter e (int) which represent the e<sup>th</sup> delivery option of the product when there's the button "See All Buying Options" and returns (seller,country).

### 5. __buyingoptions(self):
The following method checks for the "See All Buying Options" button, and if present, returns a list of tuples. These tuples consists of (price,delivery) of each of the options. Else, it returns an empty list.

### 6. getproductname(self):
The following method returns the product name. It uses CSS Selector from the constants.py file (constants.productname). 

### 7. getproductpriceanddelivery(self):
The following method calls the __buyingoptions(self) method. If there are different buying options, it returns the list of tuples (price,delivery) for each of the options. Otherwise, it returns the tuple of (price,delivery).

### 8. getoptions(self):
The following method the list of different options(types) of the product if present. Otherwise, it returns an empty list. Products may differ by sizes or colors or etc. This method detects these variations of the product.

### 9. get_path_option(self,option,var):
The following method takes as an input parameter one option(string) and var (int) which represents the variation and returns the corresponding xpath of the option.

### 10. get_product_overview_and_features(self):
The following method returns the overview , features , and details of the product (overview , bultext , detail1+detail2) (tuple).

### 11. extract_reviews(self,reviews):
The following method takes as an input parameter reviews (webelement of type a) that contains the link for the reviews page. If applicable, it returns the postive and critical reviews (g_reviews, c_reviews) where both elements are of type string. Otherwise, it returns the top reviews.

### 12. get_product_reviews_and_rating(self):
The following method calls the extract_reviews method to get the positive and critical reviews, scrapes the rating of the product then returns (good,critical,rating). 

### 13.exportxlsx(self,path='',name='test1.xlsx'):
The following method takes as an input parameters path and name of the xlsx sheet, then exports the scraped data into excel sheet in the specificied path. By default it exports the data in the same directory of the .py files.
