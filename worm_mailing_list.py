"""Read the OSC Members page and extract all email addresses

This needs to read the HTML saved from the (fully loaded) webpage of the OSC
website as it uses Javascript to load the list of members.

To use it, go to your OSC members page, and wait for the list of people to load.
Then, save page as "anything.html". Point the script to it, and it will find
and extract all email addresses in a neat little list in an output file.
"""
import bs4
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger("OSC_worm")

def main(args):

    log.info("Reading members page...")
    with Path(args.downloaded_html).open("r") as stream:
        data = stream.read()

    log.info(f"Read in a {len(data)} char HTML page")
    
    log.info("Looking for emails...")
    soup = bs4.BeautifulSoup(data, features="lxml")
    email_divs = soup.html.find_all(class_ = "um-member-metaline um-member-metaline-user_email")
    emails = [x.find("a").get_text() for x in email_divs]

    log.info(f"Found {len(emails)} emails. Writing to output...")
    with Path(args.output).open("w+") as stream:
        stream.writelines([f"{x}\n" for x in emails])
    log.info("Done!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("downloaded_html", help="The saved HTML from the OSC members page")
    parser.add_argument("output", help="Output file to save emails to")

    args = parser.parse_args()

    main(args)
