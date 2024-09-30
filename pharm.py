import requests
from bs4 import BeautifulSoup

# Step 1: Send HTTP request to pharmacy site
url = 'https://supertails.com/collections/pet-pharmacy'
response = requests.get(url)

# Step 2: Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Scrape product details
products = soup.find_all('div', class_='product')  # Assuming products are listed in 'product' divs

medications = []

for product in products:
    name = product.find('h2', class_='product-name').text
    price = product.find('span', class_='product-price').text
    availability = product.find('span', class_='availability-status').text
    
    # Append to the medications list
    medications.append({
        'name': name,
        'price': price,
        'availability': availability
    })

# Step 4: Output the scraped data
for medication in medications:
    print(f"Medication: {medication['name']}, Price: {medication['price']}, Availability: {medication['availability']}")
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Set up Selenium WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Step 2: Visit the pharmacy site
driver.get('https://example-pharmacy.com/pet-medications')

# Step 3: Find products and extract details
products = driver.find_elements(By.CLASS_NAME, 'product')

for product in products:
    name = product.find_element(By.CLASS_NAME, 'product-name').text
    price = product.find_element(By.CLASS_NAME, 'product-price').text
    availability = product.find_element(By.CLASS_NAME, 'availability-status').text
    print(f"Medication: {name}, Price: {price}, Availability: {availability}")

# Close the browser
driver.quit()
import smtplib
from email.mime.text import MIMEText

def send_order_email(medication, customer_details):
    # Step 1: Create the email content
    message = f"Order for {medication} from {customer_details['name']}, Pet: {customer_details['pet_name']}"
    msg = MIMEText(message)
    msg['Subject'] = f"New Order: {medication}"
    msg['From'] = "yourapp@example.com"
    msg['To'] = "pharmacy@example.com"

    # Step 2: Send email using SMTP
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('yourapp@example.com', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

# Usage
send_order_email('Flea Treatment', {'name': 'John Doe', 'pet_name': 'Buddy'})
