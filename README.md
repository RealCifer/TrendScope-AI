# TrendScope-AI
AI-Powered Kindle Bestseller Intelligence Pipeline

## Overview
TrendScope-AI is an AI-assisted data extraction pipeline designed to collect, structure, and analyze book metadata from Amazon Kindle bestseller pages.

The project demonstrates how semi-structured web data can be converted into a clean and analyzable dataset using Python automation and AI-assisted workflow design.

The generated dataset includes metadata such as book rankings, authors, ratings, pricing, and publishing information.

---

## Project Objective
The primary goal of this project is to:

- Extract structured information from Amazon Kindle bestseller category pages
- Visit individual product pages to enrich the dataset with additional metadata
- Clean and standardize the extracted data
- Store the final results in a structured dataset for analysis

This project demonstrates the use of AI tools and automation to solve high-volume data extraction tasks efficiently.

---

## Dataset Fields

The dataset contains the following fields:

Rank  
Title  
Author  
Rating  
Reviews  
Price  
URL  
Description  
Publisher  
Publication_Date  

The dataset is stored in CSV format for easy analysis.

---

## Technology Stack

Python  
BeautifulSoup (HTML Parsing)  
Requests (HTTP Requests)  
Pandas (Data Processing)  
AI-assisted workflow design

---

## Workflow

### 1. Bestseller Page Extraction
The pipeline begins by accessing the Amazon Kindle Bestseller page for the Paranormal Romance category.

From this page the following information is extracted:

- Rank
- Book Title
- Author
- Rating
- Number of Reviews
- Price
- Book URL

---

### 2. Product Page Extraction
Each book URL is visited individually to collect additional metadata from the product page.

The following fields are extracted:

- Book Description
- Publisher
- Publication Date

This step enriches the dataset with deeper book information.

---

### 3. Data Cleaning
After extraction, the dataset is cleaned and standardized.

Processing steps include:

- Converting ratings to numeric values
- Removing commas from review counts
- Standardizing price values
- Formatting publication dates consistently
- Handling missing values safely

---

## Project Structure

TrendScope-AI
│
├── trendscope_scraper.py
├── dataset.csv
├── workflow_document.docx
└── README.md

---

## Example Use Cases

- Book market analysis
- Publishing trend analysis
- Pricing strategy research
- Dataset generation for recommendation systems

---

## Future Improvements

Potential improvements for this project include:

- scraping multiple Kindle categories automatically
- building scheduled data pipelines
- storing data in a database
- creating dashboards for insights
- using AI models for trend detection

---

## Author

Aditya Khamait

This project demonstrates practical skills in:

- Web scraping
- Data extraction
- Dataset structuring
- AI-assisted workflow design