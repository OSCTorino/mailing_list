# Mailing list extractor
Code to obtain the mailing list from the INOSC portal

## How to install
For a linux system, have Python and Git installed. Then:
```bash
git clone git@github.com:OSCTorino/mailing_list.git
cd mailing_list
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## How to use
Go to [the OSCT members page](https://osc-international.com/osc-torino-members/?filter_osc_e60cd=OSC%20Torino) (or any other OSC members page you'd like to fetch emails from).
Wait until the list of members is fully loaded.

Save the webpage as HTML by clicking on your browser's menu, then "Save page as...".
Finally, point the script to the downloaded HTML:
```bash
python worm_mailing_list.py <path_to_downloaded_html> <path_to_output_txt_file>
```

An example:
```bash
python worm_mailing_list.py /home/user/Downloads/OSC_members.html /home/user/Desktop/emails.txt
```

You will get a nice list of emails in the output file.

> [!INFO]
> Why do you need to download the HTML for yourself? It's hard to parse Javascript in a Python script, and every solution is kind of hacky (e.g. opening a brower for you, navigating to the webpage, then copying it).
> Letting you download the page yourself is easy and fast, and it circumvents all of these problems.
