from scraper import scrape_website

text = scrape_website(
    "https://codecolonies.com/"
)

print(text[:1000])