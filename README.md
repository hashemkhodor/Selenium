# Scraping Amazon

## Objective: 
Very simple objective : scrape products from Amazon.

## Requirements:
The following project is implemented with Python 3.8.12 and using the following libraries: 
- Selenium 3.141.0
- Openpyxl 3.0.5
**_Note: You have to download the chrome.exe file to match your google chrome's one (version wise) _**

## AmazonBot 
AmazonBot is a class that inherits from Object. It has 3 main methods, and other supporting methods. It also has several data attributes.
The attributes are :
- self.path  (Holds the path of the chrome.exe application) 
- self.driver 
- self.currentproduct
- self.handles 
- self.products
- self.wait 

The constructor:
- __init__(self,path) 

The main methods are:
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


## Product 
Product is a class that inherits from Object. It is used to store the products scraped by the AmazonBot. It has one main method. 

The attributes are:
- self.name
- self.price
- self.deliveryprice
- self.deliverytime
- self.link
- self.keyword
- self.deliveryoptions
- self.overview
- self.features
- self.goodreviews
- self.criticalreviews
- self.overallrating
- self.details
- self.generalreviews

The constructor:
- __init__(self,name,link=None,keyword=None,price=[],deliveryoptions=None,deliveryprice=['Unavailable'],deliverytime=['Unavailable'],overview='',features='',criticalreviews='',goodreviews='',generalreviews='',rating='',details=''):

The main methods are:
- deliverybreakdown(self)

# Explanation:

## AmazonBot:
### Constructor:
#### 0. __init__(self,path) :
The following constructor takes as an input parameter the path(directory) of the chrome.exe file. It assigns self.driver to be an instance of webdriver.Chrome(path), and it opens 2 windows and stores their namehandles in self.namehandles list . The first window is for scraping the product, while the second is for scraping the reviews.

### Main Methods:
#### 1. scrapeproduct(self,product,pages=1) :
The following method takes as an input parameters product(string) and pages (int) and scrapes all the products from Amazon from the number of pages specified. It calls first the __getproductlinks(self,pages) method then calls the scrapepage(self,link) method.
#### 2. scrapepage(self,link) :
The following method takes as an input parameter link of the page to scrape it. It calls the methods : getoptions() , get_product_reviews_and_rating(link), getproductname() , and getproductpriceanddelivery(). It creates an instance product then append it to the self.products.

#### 3.exportxlsx(self,path='',name='test1.xlsx'):
The following method takes as an input parameters path and name of the xlsx sheet, then exports the scraped data into excel sheet in the specificied path. By default it exports the data in the same directory of the .py files. 

### Supporting Methods:
#### 1. __click(self,button): 
The following method takes as an input parameter a clickable webelement (button or input) and clicks it. It handles the exceptions _StaleElementReferenceException_ and _ElementNotInteractableException_ exceptions .

#### 2. __getproductlinks(self,pages=1) : 
The following method takes as an input parameter number of pages (int) to be scraped from. It stops and print a message to the command line when the maximum number of pages is reached. (It can also throw an exception when the maximum number of pages is reached. Just uncomment the assert and comment the following if and else statements)
#### 3. getproductdelivery(self,start):
The following method takes as an input parameter start (string) which handles 2 seperate cases of delivery then returns the delivery details if available [(deliveryprice, deliverytime)].Else it returns the ["Unavailable message"]. 

#### 4. getsellerfrom(self,e) :
The following method takes as an input parameter e (int) which represent the e<sup>th</sup> delivery option of the product when there's the button "See All Buying Options" and returns (seller,country).

#### 5. __buyingoptions(self):
The following method checks for the "See All Buying Options" button, and if present, returns a list of tuples. These tuples consists of (price,delivery) of each of the options. Else, it returns an empty list.

#### 6. getproductname(self):
The following method returns the product name. It uses CSS Selector from the constants.py file (constants.productname). 

#### 7. getproductpriceanddelivery(self):
The following method calls the __buyingoptions(self) method. If there are different buying options, it returns the list of tuples (price,delivery) for each of the options. Otherwise, it returns the tuple of (price,delivery).

#### 8. getoptions(self):
The following method the list of different options(types) of the product if present. Otherwise, it returns an empty list. Products may differ by sizes or colors or etc. This method detects these variations of the product.

#### 9. get_path_option(self,option,var):
The following method takes as an input parameter one option(string) and var (int) which represents the variation and returns the corresponding xpath of the option.

#### 10. get_product_overview_and_features(self):
The following method returns the overview , features , and details of the product (overview , bultext , detail1+detail2) (tuple).

#### 11. extract_reviews(self,reviews):
The following method takes as an input parameter reviews (webelement of type a) that contains the link for the reviews page. If applicable, it returns the postive and critical reviews (g_reviews, c_reviews) where both elements are of type string. Otherwise, it returns the top reviews.

#### 12. get_product_reviews_and_rating(self):
The following method calls the extract_reviews method to get the positive and critical reviews, scrapes the rating of the product then returns (good,critical,rating). 

## Product:
### Constructor :
#### 0. __init__(self,name,link=None,keyword=None,price=[],deliveryoptions=None,deliveryprice=['Unavailable'],deliverytime=['Unavailable'],overview='',features='',criticalreviews='',goodreviews='',generalreviews='',rating='',details='')
The construct takes as input arguments the different attributes of the product and then assigns them to self. When constructing products in the scrapeproduct(link) method in AmazonBot, we only assign the name, link, keyword, deliveryoptions, overview, features, goodreviews, criticalreviews, rating, and details.

#### 1. deliverybreakdown(self):
The following method breaks down the deliveryoptions attribute into price, deliveryprice, and deliverytime. 

