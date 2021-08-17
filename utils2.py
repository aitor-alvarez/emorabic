#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from youtubesearchpython import VideosSearch, ChannelsSearch
from typing import List, Dict
import pandas as pd
import youtube_dl
import csv


class GetYoutubeVideos():
	def __init__(self, path: str, terms: list, max_results: int = 20, duration: int = 60):
		self.terms: list = terms
		self.path: str = path
		self.MAX_RESULTS: int = max_results
		self.DURATION: int = duration
		self.search_videos()
		self.write_to_file()
		self.download_urls()

	def search_videos(self) -> List[Dict]:
		'''
		Search for videos based on a list of terms and save dict objects to list
		Output: List of dictionaries
		'''
		list_of_dicts = []
		for term in self.terms:
			results = VideosSearch(term, limit=self.MAX_RESULTS)
			output = results.result()
			for value in output.values():
				for values in value:
					list_of_dicts.append(values)
		return list_of_dicts

	def write_to_file(self):
		list_of_keys = ['viewCount', 'thumbnails','richThumbnail', 'descriptionSnippet', 'channel', 'accessibility', 'shelfTitle']
		
		ll = []
		for i in self.search_videos():
			res = dict([(key, val) for key, val in i.items() if key not in list_of_keys])
			ll.append(res)
		
		datafile = './data/video_urls.csv'
		csv_columns = ['type', 'id', 'title', 'publishedTime',
                 'duration', 'link']
		try:
			with open(datafile, 'w') as csvfile:
				writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
				writer.writeheader()
				for d in ll:
					writer.writerow(d)
		except IOError:
			print("I/O error")

	def download_urls(self):
		main_urls = pd.read_csv(self.path, sep=',')

		mydict = pd.Series(main_urls.link.values,
		                   index=main_urls.duration).to_dict()
		mydict = {int(k.replace(":", "")): v for k, v in mydict.items()}

		urls = [v for k, v in mydict.items() if k <= self.DURATION]

		ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': './audio/%(id)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'flac',
                        'preferredquality': '192'}]
                }

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			for i in urls:
				ydl.download([i])

		print()
		print('########################################')
		print(f'# FOUND {len(urls)} AUDIO/S LESS THAN {self.DURATION} SECONDS #')
		print('########################################')
		print()
