# MangaWebDownloader

A script to download manga from websites or local files.

## Requirements

Install dependencies with:

```
pip install -r requirements.txt
```

## How to run the script

Run the main script by passing the URL or local path of the manga as the first argument:

```
python main_script.py <url_or_local_path>
```

Replace `main_script.py` with the actual name of your main Python file.

## Features

- Downloads all manga images from a remote web page or a locally saved page.
- Works well if the web page contains all the images to be downloaded.

## Technical Notes

The project has a **modular structure** that allows you to create a custom downloader for each different website. 
Currently, only the basic downloader is implemented, which scans all `<img src="..."/>` tags present in the web page.

It is possible to implement **custom logic for each website**, enabling advanced workflows such as querying multiple URLs to generate a single PDF, or handling specific site layouts.

This flexibility makes it easy to extend the project for more complex and site-specific downloading workflows.

Tested on **Python 3.13**.
