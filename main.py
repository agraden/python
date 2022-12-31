import requests

def website_status(url):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      return True
    else:
      return False
  except:
    return False

website = input("Enter a full website URL to check if it's online or offline: ")

if website_status(website):
  print("The website is reachable.")
else:
  print("The website is not reachable.")
