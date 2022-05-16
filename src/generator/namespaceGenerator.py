
from argparse import Namespace
from collections import defaultdict
from posixpath import dirname
import typing
import os
import json

from os.path import join as pj
from os.path import normpath as np

from regex import R

CATPIC_EXTENSIONS = (
    ".png", ".jpg", ".jpeg", ".gif"
)

def get_namespace(projRoot: str, parsedArgs: Namespace) -> dict:
    retVal = {
        "includes": _get_html_includes(projRoot),
        "mods": _get_mods_info(projRoot),
        "news": _get_news_info(projRoot),
        "catPictures": _get_cat_pictures(projRoot)
    }

    if parsedArgs.article:
        articleId = parsedArgs.article
        for group in retVal["news"]:
            for article in group["entries"]:
                if article["id"] == articleId:
                    retVal["article"] = article
                    break
        retVal["includes"]["content"] = pj(projRoot, _get_news_folder()) + f"/{articleId}/content.html"

    return retVal


def _get_template_path() -> str:
    return np("src")

def _get_html_includes(projRoot: str) -> dict:
    incRoot = pj(projRoot, _get_template_path())
    incExt = ".html.inc"
    return {
        "TitleArea": pj(incRoot, "TitleArea") + incExt,
        "CommonHead": pj(incRoot, "CommonHead") + incExt
    }

def _get_mods_folder() -> str:
    return np("src/mods")

def _get_mods_info_from_dir(modsRoot: str, gameDir: str) -> dict:
    retVal = dict({
        "title": gameDir,
        "mods": list()
    })
    dirpath, dirnames, filenames = next(os.walk(pj(modsRoot, gameDir)))
    for modDir in dirnames:
        with open(pj(modsRoot, gameDir, np(f"{modDir}/{modDir}.json")), 'r', encoding="utf-8") as jsonInfoFile:
            currMod = json.load(jsonInfoFile)
            retVal["mods"].append(currMod)
    return retVal

def _get_mods_info(projRoot: str) -> list:
    retVal = list()

    modsFolder = _get_mods_folder()
    dirpath, dirnames, filenames = next(os.walk(pj(projRoot, modsFolder)))
    for dirName in dirnames:
        retVal.append(_get_mods_info_from_dir(dirpath, dirName))

    return retVal

def _get_news_folder():
    return np("src/news")

def _get_news_info_from_dir(newsRoot, newsDir) -> dict:
    retVal = dict()
    with open(pj(newsRoot, np(f"{newsDir}/{newsDir}.json")), 'r', encoding="utf-8") as jsonInfoFile:
        retVal = json.load(jsonInfoFile)
    return retVal

def _news_to_blocks(news: list[dict]) -> list:
    retVal = list()

    dateRanges = defaultdict(list)
    for newsEntry in sorted(news, key=lambda newsEntry: newsEntry["date"], reverse=True):
        date_split = newsEntry["date"].split("-")
        y, m, d = (date_split[0], date_split[1], date_split[2])
        date_key = f"{y}_{m}"
        dateRanges[date_key].append(newsEntry)

    for dateRange, news in dateRanges.items():
        retVal.append({
            "date": dateRange.replace('_','-'),
            "entries": news
        })

    return retVal

def _get_news_info(projRoot: str) -> list:
    retVal = list()

    newsFolder = _get_news_folder()
    dirpath, dirnames, filenames = next(os.walk(pj(projRoot, newsFolder)))
    news = [_get_news_info_from_dir(dirpath, dirName) for dirName in dirnames]
    retVal = _news_to_blocks(news)
    return retVal

def _get_cat_pictures(projRoot: str) -> list:
    retVal = list()

    picRoot = np("static/img/catshrine")
    for file in os.listdir(pj(projRoot, picRoot)):
        fileName = os.fsdecode(file)
        fileSplit = os.path.splitext(fileName)
        if len(fileSplit) < 2:
            continue
        
        fileExt = fileSplit[1]
        if fileExt.lower() in CATPIC_EXTENSIONS:
            retVal.append({
                "imagePath": "/img/catshrine/" + f"{fileName}"
            })

    return retVal
