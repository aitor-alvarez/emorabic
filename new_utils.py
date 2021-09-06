#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from youtubesearchpython import VideosSearch
import pandas as pd
import youtube_dl
import re


class GetYoutubeVideos:
    def __init__(
        self,
        terms: list,
        max_results: int = 20,
        duration: int = 60,
        region: str = "US",
    ):
        self.terms: list = terms
        self.MAX_RESULTS: int = max_results
        self.DURATION: int = duration
        self.REGION: str = region

        #### (1) get a list of dicts by term
        list_of_dicts = []
        for term in self.terms:
            results = VideosSearch(term, limit=self.MAX_RESULTS, region=self.REGION)
            output = results.result()
            for value in output.values():
                for values in value:
                    list_of_dicts.append(values)

        #### (2) save the list of dicts to a dataframe
        df = pd.DataFrame(list_of_dicts)
        mydict = pd.Series(df.link.values, index=df.duration).to_dict()
        mydict = {int(k.replace(":", "")): v for k, v in mydict.items()}
        dictionary = mydict.keys()

        ### (3) convert duration to an integer and append to the dataframe
        df = pd.DataFrame(df)
        df["new_duration"] = dictionary

        ### (4) filter the dataframe rows by the new duration entered on the command line
        df = df.loc[df["new_duration"] <= self.DURATION]

        ### (5) add the term (emotion) as a column in the dataframe
        for term in self.terms:
            d = df.title.str.findall(term)
            if d.any():
                df["term"] = d

        ### (7) delete unneccesary columns and save to csv file
        df = df[["type", "id", "term", "duration", "new_duration", "link"]]
        df = df[~df.term.str.len().eq(0)]
        datafile = "./data/data.csv"
        df.to_csv(datafile, sep="\t", encoding="utf-8")

        # (8) download the audio/s
        urls = df["link"].tolist()

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "./audio/%(id)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "flac",
                    "preferredquality": "192",
                }
            ],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for i in urls:
                ydl.download([i])

        print()
        print("########################################")
        print(f"# FOUND {len(urls)} AUDIO/S LESS THAN {self.DURATION} SECONDS #")
        print("########################################")
        print()
