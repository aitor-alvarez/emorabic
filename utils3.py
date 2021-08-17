#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from youtubesearchpython import ChannelsSearch
from typing import List, Dict
import youtube_dl
import json


class GetYoutubeVideosByRegion():
	def __init__(self, path: str, terms: list, max_results: int = 20,  region: str = 'US'):
		self.terms: list = terms
		self.path: str = path
		self.MAX_RESULTS: int = max_results
		self.REGION: str = region
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
			results = ChannelsSearch(term, limit=self.MAX_RESULTS, region=self.REGION)
			output = results.result()
			for value in output.values():
				for values in value:
					list_of_dicts.append(values)
		return list_of_dicts

	def write_to_file(self):
		data = self.search_videos()
		with open('./data/data.txt', 'w') as outfile:
			json.dump(data, outfile)
		
	def download_urls(self):
		links = []
		for i in self.search_videos():
			for k, v in i.items():
				if k == 'link':
					links.append(v)

		ydl_opts = {
				'format': 'bestaudio/best',
				'outtmpl': './audio/%(id)s.%(ext)s',
				'postprocessors': [{
					'key': 'FFmpegExtractAudio',
					'preferredcodec': 'flac',
					'preferredquality': '192'}]
					}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			for i in links:
				ydl.download([i])

		print()
		print('########################################')
		print(f'# FOUND {len(links)} AUDIO/S #')
		print('########################################')
		print()

	