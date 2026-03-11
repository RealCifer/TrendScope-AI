import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.com/Best-Sellers-Kindle-Store-Paranormal-Romance/zgbs/digital-text/6190491011"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

books = []

items = soup.select(".zg-grid-general-faceout")

rank = 1

for item in items:

    title = item.select_one(".p13n-sc-truncate")
    title = title.text.strip() if title else ""

    author = item.select_one(".a-size-small.a-link-child")
    author = author.text.strip() if author else ""

    rating = item.select_one(".a-icon-alt")
    rating = rating.text.split(" ")[0] if rating else ""

    reviews = item.select_one(".a-size-small")
    reviews = reviews.text.replace(",", "") if reviews else ""

    price = item.select_one(".p13n-sc-price")
    price = price.text.replace("$", "") if price else ""

    link = item.select_one("a")
    link = "https://amazon.com" + link["href"] if link else ""

    books.append({
        "Rank": rank,
        "Title": title,
        "Author": author,
        "Rating": rating,
        "Reviews": reviews,
        "Price": price,
        "URL": link
    })

    rank += 1

df = pd.DataFrame(books)

df.to_csv("dataset.csv", index=False)

print("Dataset created successfully!")