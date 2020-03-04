import cgi
from database_connect import get_restaurants



def bulleted_restaurants():
  restuarants_list = ""
  for restuarant in get_restaurants("Kreuzberg"):
    restuarants_list += "<li>" + restuarant[1] + "</li>"
  
  return restuarants_list

html = f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Restaurants!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
    
    <!-- import the webpage's javascript file -->
    <script src="/script.js" defer></script>
  </head>  
  <body>
    <h1>Restaurants in Kreuzberg:</h1>
    
    <p>
      <ul style="list-style-type:circle;">
        {bulleted_restaurants()}
      </ul>
    </p>

  </body>
</html>
'''

with open("./index.html", "w+") as index_html:
  index_html.write(html)
