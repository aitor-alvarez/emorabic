#Use this file to call functions in utils.py and to execute them in sequence
from utils import YoutubeAudio



if __name__ == "__main__":
	terms = ['الدحيح', 'مصر']
	path = 'data/video_urls.csv'
	YoutubeAudio(terms, path)

