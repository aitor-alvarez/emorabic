#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from new_utils import GetYoutubeVideos

# list of terms used to download the audios

terms = {
    "disgust": ["اشمئزاز", "مشمئزة", "مشمئز", "قرف"],
    "angry": ["معصب", "معصبه", "غضبان"],
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--max-results",
        dest="max_results",
        type=int,
        default=10,
        help="the maximum number of audios per term",
    )
    parser.add_argument(
        "--duration",
        dest="duration",
        default=60,
        type=int,
        help="the desired duration of the audio",
    )
    parser.add_argument(
        "--region",
        dest="region",
        default=60,
        type=str,
        help="the desired region of the audio",
    )

    parser.set_defaults(verbose=False)
    args = parser.parse_args()

    max_results: int = args.max_results
    duration: int = args.duration
    region: str = args.region

    GetYoutubeVideos(
        terms=terms, max_results=max_results, duration=duration, region=region
    )
