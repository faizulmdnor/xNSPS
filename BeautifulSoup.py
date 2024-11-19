import requests
from bs4 import BeautifulSoup

# Step 3: Fetch the webpage content
url = "https://en.wikipedia.org/wiki/List_of_laptop_brands_and_manufacturers"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 5: Find the table containing laptop brands
    # On this page, we can identify the right table based on its structure or specific class (if available)
    table = soup.find('table', {'class': 'wikitable'})

    # Step 6: Extract data from the table
    brands = []
    if table:
        rows = table.find_all('tr')

        for row in rows[1:]:  # Skip the header row
            cells = row.find_all('td')
            if cells:
                # Get the brand name, usually the first cell in each row
                brand_name = cells[0].get_text(strip=True)
                brands.append(brand_name)

    # Step 7: Output the results
    print("Laptop Brands:")
    for brand in brands:
        print(brand)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
