#!/usr/bin/env python

import feedparser, requests

def main():
  response = requests.get("https://ao.gl/feed")
  feed = feedparser.parse(response.content)

  feed.entries = feed.entries[0:9]

  for entry in feed.entries:
    print(entry.title)
    print(entry.links[0].href)
    print()
