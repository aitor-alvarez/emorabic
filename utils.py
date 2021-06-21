#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import csv
import youtube_dl
import pandas as pd
from pydub import AudioSegment
from youtube_search import YoutubeSearch

class YoutubeAudio:
	def __init__(self, terms, path):
		self.terms = terms
		self.path = path
		self.search_videos()
		self.write_to_file()
		self.download_urls()

	def search_videos(self):
		'''
		Search for videos based on a list of terms and save dict objects to list
		'''
		i = 0
		for term in self.terms:
			i += 1
			results = YoutubeSearch(term, max_results=10).to_dict()
			if i == 1:
				output = results
			else:
				output += results
		return output

	def write_to_file(self):
		'''
		This function takes the dictinary result from (search_videos) 
		and saves it to csv file here the header is the key values
		'''
		datafile = 'data/video_urls.csv'
		csv_columns = ['id', 'thumbnails', 'title', 'long_desc','channel', 'duration', 'views', 'publish_time', 'url_suffix']
		try:
			with open(datafile, 'w') as csvfile:
				writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
				writer.writeheader()
				for d in self.search_videos():
					writer.writerow(d)
		except IOError:
			print("I/O error")

	def download_urls(self):
		list_urls = pd.read_csv(self.path, sep=',')
		list_urls = list_urls['url_suffix'].tolist()
		base_url = 'https://youtube.com'

		url = [base_url+l for l in list_urls]
		ydl_opts = {
            	'format': 'bestaudio/best',
                'outtmpl': './audio/%(id)s.%(ext)s',
            	'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'flac',
                'preferredquality': '192'}]
        		}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			for i in url:
				ydl.download([i])



	


#This function takes a list of json-like dict objects and writes the to a txt file, just to keep the complete data
# def write_to_file(data, datafile='data/video_urls.txt'):
# 	df = open(datafile, 'w')
# 	with open(df, 'w') as f:
# 		for key, value in data.items():
# 			f.write(key, value)
# 	# for d in data:
# 	# 	df.write(d)
# 	df.close()



# def extract_audio_from_video(video_path):
# 	if video_path.endswith('.mp4'):
# 		audiofile = AudioSegment.from_file(video_path)
# 		output_file = video_path.replace('mp4', 'flac')
# 		try:
# 			AudioSegment.from_file(video_path).export(output_file, format='flac')
# 			return output_file
# 		except:
# 			return "There has been an error with your audio file. The file might be corrupted or damaged."
# 	else:
# 		return "This video file is not in mp4 format"

