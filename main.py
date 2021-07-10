#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from utils import YoutubeAudio

# list of terms used to download the audios
terms = ['الأهلي']

# path to the csv file that contains all the information about the youtube links
path = 'data/video_urls.csv'

if __name__ == "__main__":
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("--max-results", dest="max_results", type=int, default=10, help="the maximum number of audios per term")
	parser.add_argument("--duration", dest="duration", default=60, type=int, help="the desired duration of the audio")

	parser.set_defaults(verbose=False)
	args = parser.parse_args()

	max_results: int = args.max_results
	duration: int = args.duration

	YoutubeAudio(terms=terms, path=path, max_results=max_results, duration=duration)
