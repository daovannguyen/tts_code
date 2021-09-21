import wget
from download import download
import os
import json

def get_content(text, str_start, str_end):
    a = text.split(str_start)
    b = []
    for i in range(1, len(a)):
        b.append(a[i].split(str_end)[0])
    return b

def download_from_url(url, path):
    try:
        wget.download(url, path)
    except:
        download(url, path)

def replace_all(text, str_start, str_end):
  x = get_content(text, str_start, str_end)
  x = set(x)
  for i in x:
    str = str_start + i + str_end
    text = text.replace(str, '')
  return text

def get_content_from_html(url):

    #download
    path = '3123123123124.txt'
    download_from_url(url, path)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    os.remove(path)

    #lay content
    text = replace_all(text, "<script", '</script>')
    text = replace_all(text, "<style", '</style>')
    text = replace_all(text, "<", '>')
    return text

def get_link_from_html(url):

    #download
    path = '3123123123124.txt'
    download_from_url(url, path)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    os.remove(path)

    #lay link
    a = get_content(text, "http", '"')
    for i in range(len(a)):
        a[i] = 'http' + a[i]
    return a