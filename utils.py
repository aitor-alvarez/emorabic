from youtube_search import YoutubeSearch
from pydub import AudioSegment


#Search for videos based on a list of terms and save dict objects to list
def search_videos(terms):
	i =0
	for term in terms:
		i+= 1
		results = YoutubeSearch(term, max_results=10).to_dict()
		if i==1:
			output = results
		else:
			output +=results

	return output


#This function takes a list of json-like dict objects and writes the to a txt file, just to keep the complete data
def write_to_file(data, datafile='data/video_urls.txt'):
	df = open(datafile, 'w')
	for d in data:
		df.write(d)
	df.close()


#this function should be used to download all videos from the list of json objects
def download_urls(list_urls):
	base_url = 'https://youtube.com'

	# to do, use youtube-dl to download the full url
	for l in list_urls:
		url = base_url+l['url_suffix']
		#use here the function or class to download the yt videos to data/videos



def extract_audio_from_video(video_path):
	if video_path.endswith('.mp4'):
		audiofile = AudioSegment.from_file(video_path)
		output_file = video_path.replace('mp4', 'flac')
		try:
			AudioSegment.from_file(video_path).export(output_file, format='flac')
			return output_file
		except:
			return "There has been an error with your audio file. The file might be corrupted or damaged."
	else:
		return "This video file is not in mp4 format"




