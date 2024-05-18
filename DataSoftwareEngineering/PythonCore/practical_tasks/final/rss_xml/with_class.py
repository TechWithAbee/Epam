import argparse
import requests
import xml.etree.ElementTree as ET
import json

class RSSReader:
    def __init__(self, source, limit=None, json_output=False):
        self.source = source
        self.limit = limit
        self.json_output = json_output

    def fetch_rss(self):
        response = requests.get(self.source)
        response.raise_for_status()
        return response.content

    def parse_rss(self, xml_content):
        root = ET.fromstring(xml_content)
        channel = root.find('channel')
        return {
            'title': channel.find('title').text,
            'link': channel.find('link').text,
            'description': channel.find('description').text,
            'language': channel.find('language').text if channel.find('language') is not None else '',
            'pubDate': channel.find('pubDate').text if channel.find('pubDate') is not None else '',
            'items': self.parse_items(channel.findall('item'))
        }

    def parse_items(self, items):
        parsed_items = []
        for item in items[:self.limit]:
            parsed_items.append({
                'title': item.find('title').text if item.find('title') is not None else '',
                'author': item.find('author').text if item.find('author') is not None else '',
                'pubDate': item.find('pubDate').text if item.find('pubDate') is not None else '',
                'link': item.find('link').text if item.find('link') is not None else '',
                'category': [category.text for category in item.findall('category')],
                'description': item.find('description').text if item.find('description') is not None else ''
            })
        return parsed_items

    def output_as_json(self, rss_data):
        print(json.dumps(rss_data, indent=2))

    def output_as_text(self, rss_data):
        print(f"Feed: {rss_data['title']}")
        print(f"Link: {rss_data['link']}")
        print(f"Description: {rss_data['description']}\n")
        for item in rss_data['items']:
            print(f"Title: {item['title']}")
            if item['author']:
                print(f"Author: {item['author']}")
            if item['pubDate']:
                print(f"Published: {item['pubDate']}")
            if item['link']:
                print(f"Link: {item['link']}")
            if item['category']:
                print(f"Categories: {', '.join(item['category'])}")
            if item['description']:
                print(f"\n{item['description']}\n")
            print()

    def run(self):
        xml_content = self.fetch_rss()
        rss_data = self.parse_rss(xml_content)
        if self.json_output:
            self.output_as_json(rss_data)
        else:
            self.output_as_text(rss_data)

def main():
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
    parser.add_argument('source', type=str, help='RSS URL')
    parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter is provided')
    args = parser.parse_args()

    reader = RSSReader(source=args.source, limit=args.limit, json_output=args.json)
    reader.run()

if __name__ == "__main__":
    main()
