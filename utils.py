#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from youtubesearchpython import VideosSearch
import pandas as pd
import youtube_dl


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
        for values in self.terms.values():
            for term in values:
                results = VideosSearch(term, limit=self.MAX_RESULTS, region=self.REGION)
                output = results.result()
                for value in output.values():
                    for values in value:
                        list_of_dicts.append(values)

        #### (2) save the list of dicts to a dataframe
        df = pd.DataFrame(list_of_dicts)
        duration = df["duration"].tolist()
        duration2 = [int(item.replace(":", "")) for item in duration]
        df["new_duration"] = duration2

        ### (3) filter the dataframe rows by the new duration entered on the command line
        df = df.loc[df["new_duration"] <= self.DURATION]

        ### (4) add the term as a column in the dataframe
        for keys, values in self.terms.items():
            for term in values:
                d = df.title.str.findall(term)
                if d.any():
                    df["term"] = d
                    df["emotion"] = keys
                    df["region"] = self.REGION

        # ### (5) delete unneccesary columns and save to csv file
        df = df[
            [
                "type",
                "id",
                "term",
                "emotion",
                "region",
                "duration",
                "link",
            ]
        ]

        df = df[~df.term.str.len().eq(0)]
        datafile = "./data/gulf.csv"
        df.to_csv(datafile, sep="\t", encoding="utf-8")

        # # (6) download the audio/s
        urls = df["link"].tolist()

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "./audio/gulf/%(id)s.%(ext)s",
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
