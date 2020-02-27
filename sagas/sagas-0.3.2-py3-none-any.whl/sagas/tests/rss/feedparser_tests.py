import feedparser
import time
from subprocess import check_output
import sys

# feed_name = 'TRIBUNE'
# url = 'http://chicagotribune.feedsportal.com/c/34253/f/622872/index.rss'

feed_name = sys.argv[1]
url = sys.argv[2]

# db = '/var/www/radio/data/feeds.db'
db = './out/feeds.db'
limit = 12 * 3600 * 1000

#
# function to get the current time
#
current_time_millis = lambda: int(round(time.time() * 1000))
current_timestamp = current_time_millis()

def post_is_in_db(title):
    with open(db, 'r') as database:
        for line in database:
            if title in line:
                return True
    return False


# return true if the title is in the database with a timestamp > limit
def post_is_in_db_with_old_timestamp(title):
    with open(db, 'r') as database:
        for line in database:
            if title in line:
                ts_as_string = line.split('|', 1)[1]
                # ts = long(ts_as_string)
                ts = int(ts_as_string)
                if current_timestamp - ts > limit:
                    return True
    return False


#
# get the feed data from the url
#
feed = feedparser.parse(url)

#
# figure out which posts to print
#
posts_to_print = []
posts_to_skip = []

for post in feed.entries:
    # if post is already in the database, skip it
    # TODO check the time
    title = post.title
    if post_is_in_db_with_old_timestamp(title):
        posts_to_skip.append(title)
    else:
        posts_to_print.append(title)

#
# add all the posts we're going to print to the database with the current timestamp
# (but only if they're not already in there)
#
# f = open(db, 'a')
with open(db, 'a') as f:
    for title in posts_to_print:
        if not post_is_in_db(title):
            f.write(title + "|" + str(current_timestamp) + "\n")
# f.close

#
# output all of the new posts
#
count = 1
blockcount = 1
for title in posts_to_print:
    if count % 5 == 1:
        print("\n" + time.strftime("%a, %b %d %I:%M %p") + '  ((( ' + feed_name + ' - ' + str(blockcount) + ' )))')
        print("-----------------------------------------\n")
        blockcount += 1
    print(title + "\n")
    count += 1

"""
When run with the Chicago Tribune RSS feed URL shown, the script writes data like 
the following to its “database” (which is a text file with the fields 
separated by a | character):

Tiger Woods won't play in U.S. Open|1401322649189
Photos: Giants 5, Cubs 0|1401322649189
Baker foils Giants' no-hit bid, but Cubs lose 5-0|1401322649189
Sox Game Day: Noesi still searching for 1st Sox victory|1401322649189
Bears claim tackle Ola off waivers|1401322649189
Stanley Cup Final to start Wednesday|1401322649189
Renteria pushing Samardzija for All-Star game|1401322649189
Chicago teen Townsend stuns French star in French Open|1401322649189
Emanuel: No Wrigley Field hearing next month|1401322649189
"""

