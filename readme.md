# What is this?

This tool is a very simple web scraper that takes data related to Fallout 4 crafting components
and displays that data within a CLI. The FO4ComponentScraper class handles scraping and parsing the data,
and the main.py file contains the 'loop' that allows you to query the data via the command line.

### Why?

In the game you need the correct number/type of components in order to craft and upgrade things. Personally
I don't find scouring the wasteland for junk enjoyable, so I tend to use the game console and spawn in whatever
components I need. I found navigating the Wiki to be a pain, so I created this utility. I can run it in a terminal
on a second monitor, tab over to get the object ID I need, then tab back into the game.

This program is total overkill (I could just copy the IDs I need into a txt file,
or write a script that only prints all IDs) but I wanted to try out some web scraping with Python.

### How?

Clone the repository to any folder with `git clone https://github.com/pmdredd/fo4_component_scraper.git`.

Create a new virtual env using  `python3 -m venv venv` then activate that env with `venv\Scripts\activate` on Windows,
or `source venv/bin/activate` on Linux/MacOS.

Install the required libraries (requests and BeautifulSoup) using `python3 -m pip install -r requirements.txt`.

Now you can open the tool by typing `python3 main.py`.


### What next?

I'm not convinced I need a class for this tool. Really it's 4 functions, 2 of which are 'get the data' and 'processs the data'.
Maybe I can just turn it into a module and skip the ceremony of OOP.


