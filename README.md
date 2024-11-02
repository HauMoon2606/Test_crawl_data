# Test crawl data with selenium and scrapy library

This is a demo project of python's selemium library and python's scrapy library to crawl data from simple websites.  

## Table of contents
  - [Table of contents](#table-of-contents)
  - [Project overview](#project-overview)
  - [Selenium](#selenium)
    - [Installation](#installation)
    - [Website](#website)
    - [Usage](#usage)

  - [Scrapy](#scrapy)
    - [Installation](#installation-1)
    - [Website](#website-1)
    - [Usage](#usage-1)


## Project overview
This project includes 2 files, each file represent to a library used to crawl data.  

## Selenium
### Installation
To run this project, ensure you have the following:
1. **Python** (3.8+)
2. **Chrome broswer**
3. **Selenium webdriver** for the selected browser
4. **Selenium** (3.141.0)
5. **Pandas**
### Website
1. [Result of EPL](https://www.adamchoi.co.uk/overs/detailed)
2. [Book product int audible](https://www.audible.com/search)
### Usage
1. Run the crawler
   ```bash
   # Run the crawler script of result EPL 
   python EPL_crawl_data.py
   # Run the crawler script of book in audible 
   python crawl.py
2. Storage and Result
   After crawling data from the website , the results will be saved in a .csv as follow:  
   ![EPL result!](/Image/Selenium/EPL/EPL.png)
   ![Book audible!](/Image/Selenium/Audible/Book.png)

## Scrapy
### Installation
1. **Python**
2. **Scrapy 2.4.0**
### Website
1. [Population of countries](https://www.worldometers.info/world-population/population-by-country/)
2. [Book product int audible](https://www.audible.com/search)
3. [Transcript of movies](https://subslikescript.com/movies)

### Usage
1. Run the crawler
   ```bash
   # Run the crawler script of website 1
   scrapy crawl worldometers 
   # Run the crawler script of website 2
   scrapy crawl audible
   #Run the crawler script of website 3
   scrapy crawl transcript
2. Storage and result
   After crawling data from the website , the results will be saved in a .csv or .json as follow:  
   ![population result!](/Image/Scrapy/population.png)
   ![Book audible!](/Image/Scrapy/audible.png)
   ![Transcripts of movies!](/Image/Scrapy/transcript.png)