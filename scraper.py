import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

# Step 1: Get the URL and tag from the user
url = input("Enter the URL you want to scrape: ").strip()
tag = input("Enter the HTML tag you want to scrape (e.g., h1, p, div): ").strip()

# Step 2: Send a request to the website
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP errors
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Step 3: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 4: Extract and display the specified tag's content
elements = soup.find_all(tag)

if elements:
    print(f"\nExtracted '{tag}' elements from {url}:\n")
    for i, element in enumerate(elements, start=1):
        print(f"{i}. {element.get_text(strip=True)}")
else:
    print(f"No '{tag}' elements found on the page.")
