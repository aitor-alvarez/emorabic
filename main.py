#Use this file to call functions in utils.py and to execute them in sequence
import argparse
from utils import YoutubeAudio



if __name__ == "__main__":
	terms = ['الدحيح', 'مصر']
	path = 'data/video_urls.csv'

	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("--max-results", dest="max_results", type=int,
	                    default=10, help="the maximum number of audios per term")

	parser.set_defaults(verbose=False)
	args = parser.parse_args()

	max_results: int = args.max_results

	YoutubeAudio(terms=terms, path=path, max_results=max_results)
