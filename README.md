
# tocgen
Generates a table of contents using a specified absolute directory as the root where child markdown files will be converted into a markdown list of links; To the files location appended by the name of the markdown file. 

# Why did I make this ? 

Well , I was messing around with a jekyll template while converting my "config" repo to a website. This repo is just a giant repo of organized markdown files. So I wanted to turn this into a website with a unique template to showcase what i've been upto for the past 3 years.


This is a simple python script that creates a markdown list with links to the markdown files in a directory. Think of this TOC as one that creates LINKS to other child files, rather than other sections on the page.


# Installation 

```
git clone https://github.com/buhfur/toc_gen $HOME
sudo ln -s $HOME/toc_gen/tocgen /usr/local/bin/

```


# Usage 

**Please note you must specify the absolute path for the markdown file and the directory.**


```
usage: tocgen [-h] [--show-changes] --dir DIR --file PATH-TO-FILE

optional arguments:
  -h, --help            show this help message and exit
  --show-changes, -s    Show table of contents before writing to file
  --dir DIR, -d DIR     Specify absolute directory as root for Table of
                        Contents
  --file FILE, -f FILE  File the TOC will be written to

```
