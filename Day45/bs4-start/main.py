import bs4
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = bs4.BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.get_text()
    article_texts.append(article_text)
    article_link = article_tag.find(name="a")
    article_link_href = article_link.get("href")
    article_links.append(article_link_href)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

#print(article_upvotes)
#print(article_links)
#print(article_texts)














#with open('website.html', encoding='utf8') as file:
#    contents = file.read()

#soup = bs4.BeautifulSoup(contents, 'html.parser')
##print(soup.prettify())
#all_anchor_tag = soup.find_all(name='a')
#print(all_anchor_tag)

#selection_heading = soup.find(name="h3", class_="heading")
#print(selection_heading)
