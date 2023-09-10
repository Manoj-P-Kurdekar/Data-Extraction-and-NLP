# Data Extraction and NLP

This repository contains a Python program for extracting textual data from a given URL, performing text analysis, and computing various variables as specified in the task objective. The program is designed to handle a batch of articles, extracting their content, and conducting text analysis to generate meaningful insights.

## Table of Contents
1. [Objective](#1-objective)
2. [Data Extraction](#2-data-extraction)
3. [Data Analysis](#3-data-analysis)
4. [Variables](#4-variables)
5. [Output Data Structure](#5-output-data-structure)
6. [Usage](#6-usage)
7. [Dependencies](#7-dependencies)
8. [Contributing](#8-contributing)
9. [License](#9-license)

## 1. Objective
The main objective of this project is to extract textual data from provided URLs and perform text analysis to compute various text-related variables, as outlined in the task description.

## 2. Data Extraction
The program reads a list of articles from an Excel file (`Input.xlsx`), extracts the article title and text, and saves each article as a separate text file with a unique filename based on the `URL_ID`. It ensures that only the article content is extracted, excluding any website headers, footers, or other irrelevant information.

## 3. Data Analysis
For each extracted article, the program performs text analysis to compute the specified variables such as positive score, negative score, polarity score, subjectivity score, and more. The details of these variables are given below.

## 4. Variables
The program calculates the following variables as described:
1. POSITIVE SCORE
2. NEGATIVE SCORE
3. POLARITY SCORE
4. SUBJECTIVITY SCORE
5. AVG SENTENCE LENGTH
6. PERCENTAGE OF COMPLEX WORDS
7. FOG INDEX
8. AVG NUMBER OF WORDS PER SENTENCE
9. COMPLEX WORD COUNT
10. WORD COUNT
11. SYLLABLE PER WORD
12. PERSONAL PRONOUNS
13. AVG WORD LENGTH

## 5. Output Data Structure
The output data is structured according to the variables, which includes all input variables from `Input.xlsx` and the computed text analysis variables.

## 6. Usage
To use this program, follow these steps:
1. Ensure you have the required dependencies
2. Place the articles' URLs in the `Input.xlsx` file.
3. Run the Python program to extract data and perform text analysis.
4. The results will be saved in the `Output Data Structure.xlsx` file.

## 7. Dependencies
Make sure you have the following Python libraries installed:
- pandas
- numpy
- nltk
- textblob
- docx2txt

You can install them using pip:

```
pip install pandas numpy nltk textblob docx2txt
```

## 8. Contributing
Contributions to this project are welcome! Feel free to open issues or pull requests to suggest improvements or report bugs.

## 9. License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of this license.

Thank you for using this data extraction and text analysis tool!
