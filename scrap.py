from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome()


base_url = "https://www.medrxiv.org/content/10.1101/2024.11.17.24317460v1"


output_file = "research_medrxiv.csv"


def scrape_page(url):
    try:
        
        driver.get(url)
        time.sleep(3)  
        
        
        try:
            title = driver.find_element(By.XPATH, '/html/body/div[3]/section/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div/div[1]/h1').text
        except Exception as e:
            title = "Title not found"
            print(f"Error finding title: {e}")
        
       
        try:
            abstract = driver.find_element(By.XPATH, '/html/body/div[3]/section/div/div/div/div/div/div/div/div/div[1]/div/div/div[5]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div[1]/div[1]/p').text
        except Exception as e:
            abstract = "Abstract not found"
            print(f"Error finding abstract: {e}")
        
        
        with open(output_file, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([title, abstract, url])
        
        print(f"Scraped: {title}")
        
        
        try:
            next_button = driver.find_element(By.XPATH, '/html/body/div[3]/section/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/span[2]/a')
            next_url = next_button.get_attribute("href")
            return next_url
        except Exception as e:
            print("No next page found or error navigating to the next page:", e)
            return None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None


with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Abstract", "URL"])


current_url = base_url

while current_url:
    current_url = scrape_page(current_url)


driver.quit()

print(f"Scraping completed. Data saved to {output_file}")
