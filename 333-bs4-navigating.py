'''
Navigating with Beautiful Soup

Via Tags

parent / parents
contents
next_sibling / next_siblings

Via Searching

find_parent / find_parents
find_next_sibling / find_next_siblings
find_previous_sibling / find_previous_siblings
'''

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# data = soup.body.contents[1].next_sibling.next_sibling
# soup.find(class_="super-special").parent.parent
# data = soup.find(id="first").find_next_sibling().find_next_sibling()
# data = soup.select("[data-example")
data = soup.find("h3").find_parent("html")

print(data)