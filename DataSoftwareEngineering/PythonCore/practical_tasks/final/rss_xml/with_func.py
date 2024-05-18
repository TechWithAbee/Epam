from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET
from json import dumps as json_dumps

class UnhandledException(Exception):
    pass

def parse_rss_item(item, limit):
    parsed_items = []
    count = 0

    for elem in item:
        if limit is not None and count >= limit:
            break

        title = elem.find('title').text if elem.find('title') is not None else ''
        author = elem.find('author').text if elem.find('author') is not None else ''
        pub_date = elem.find('pubDate').text if elem.find('pubDate') is not None else ''
        link = elem.find('link').text if elem.find('link') is not None else ''
        category = [category.text for category in elem.findall('category')]
        description = elem.find('description').text if elem.find('description') is not None else ''

        parsed_items.append({
            'title': title,
            'author': author,
            'pubDate': pub_date,
            'link': link,
            'category': category,
            'description': description
        })
        count += 1

    return parsed_items

def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.
    """
    root = ET.fromstring(xml)
    channel = root.find('channel')

    title = channel.find('title').text if channel.find('title') is not None else ''
    link = channel.find('link').text if channel.find('link') is not None else ''
    description = channel.find('description').text if channel.find('description') is not None else ''
    language = channel.find('language').text if channel.find('language') is not None else ''
    pub_date = channel.find('pubDate').text if channel.find('pubDate') is not None else ''
    last_build_date = channel.find('lastBuildDate').text if channel.find('lastBuildDate') is not None else ''
    managing_editor = channel.find('managingEditor').text if channel.find('managingEditor') is not None else ''
    categories = [category.text for category in channel.findall('category')]

    items = parse_rss_item(channel.findall('item'), limit)

    if json:
        result = {
            'title': title,
            'link': link,
            'description': description,
            'language': language,
            'pubDate': pub_date,
            'lastBuildDate': last_build_date,
            'managingEditor': managing_editor,
            'categories': categories,
            'items': items
        }
        return [json_dumps(result, indent=2)]
    else:
        result = [
            f"Feed: {title}",
            f"Link: {link}",
            f"Description: {description}",
            f"Language: {language}",
            f"Publish Date: {pub_date}",
            f"Last Build Date: {last_build_date}",
            f"Editor: {managing_editor}",
            f"Categories: {', '.join(categories)}",
        ]

        for item in items:
            result.append(f"\nTitle: {item['title']}")
            if item['author']:
                result.append(f"Author: {item['author']}")
            if item['pubDate']:
                result.append(f"Published: {item['pubDate']}")
            if item['link']:
                result.append(f"Link: {item['link']}")
            if item['category']:
                result.append(f"Categories: {', '.join(item['category'])}")
            if item['description']:
                result.append(f"\n{item['description']}\n")

        return result

def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)

if __name__ == "__main__":
    main()
