this is my personal project.

Im making: 
A pipeline to convert and clean the dataset from the vancouver open data specifically the open-vendors, food and restaurant. 
my goal is to convert the json into a more readable data, using SQL.

Therefore i have developed a series of steps that I should follow before I do any coding, since it is the best way I can orginize my project.

# Steps to follow: 

1. Pull the records with the vancouver api [Vancouver opend data](https://opendata.vancouver.ca/explore/dataset/food-vendors/api/):
    I will follow the portals API extract the data and clean the JSON

2. The next thing that I will do is to flatten the data with pandas.:
    I will use the pandas library so it can help me organize and keep all the data clean

3. Load the data cleaned with pandas into sqlite3

4. I will write my own SQL queries to be able to answer real questions about the data that im working on

5. Wrap everything into the CLI

6. OPTIONAL but must likely will use. sqlviewer to be able to visualize in a clear way the data

**Based on:**

This project is based on a brainstorm that I had when doing some requests to claude.

The request in matters was to look for most common requirements that companies were looking for different interns.

Among the different requirements that the AI retrieved were the creation of pipelines, therefore:

**Project:**
A Python ETL pipeline that ingests raw API data, cleans and flattens it, loads it into SQLite, and answers analytical questions via SQL queries.

**Objectives:**

- Learn python pipelines with different guidelines
- Learn pandas data extract and pass the data to SQL
- Wrtie clear SQL queries to be able to answer ral questions
- Use of the command line with SQL
- Representatoin of sql data

**Documents used**

