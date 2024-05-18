import requests

def save_xml():
    # URL of the XML document
    url = "https://news.yahoo.com/rss"

    # Fetch the content from the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the content to an XML file
        with open("rss_feed.xml", "wb") as file:
            file.write(response.content)
        print("XML file has been saved successfully.")
    else:
        print("Failed to retrieve the XML document. Status code:", response.status_code)

# Call the function to save the XML file
if __name__ == "__main__":
    save_xml()