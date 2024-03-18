import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to scrape IMDb homepage
# def scrape_imdb_homepage(https://www.imdb.com/)
#     response = requests.get(https://www.imdb.com/)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # Extract relevant data (example: top movies)
#     top_movies = soup.find_all('td', class_='titleColumn')
#     movies_list = []
#     for movie in top_movies:
#         title = movie.a.text
#         year = movie.span.text.strip('()')
#         movies_list.append((title, year))
#     return movies_list

def create_database(db_name):
    conn = sqlite3.connect(db_name+'.db')
    c = conn.cursor()
    # Create table if not exists
    c.execute(f'''CREATE TABLE IF NOT EXISTS {db_name}
                     (job_title TEXT, company_name TEXT, location TEXT)''')
    conn.close()

# Function to save data to SQLite database
def save_to_database(job_title, company_name, location):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    # Create table if not exists
    # Insert data into the table
    sql_command = f"INSERT INTO jobs VALUES ('{job_title}', '{company_name}','{location}');"
    print(sql_command)
    c.execute(sql_command)
    conn.commit()
    conn.close()

create_database("jobs")

