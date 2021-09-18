### The number of audios per term can be specified.

## two packages are used to download youtube videos.

## In utils, we use `youtube_search`:

- we can get up to 20 videos/audios per term and we can specify the duration as follows:

`python3 main.py --max-results 10 --duration 60`

## In utils2, we use `youtubesearchpython`:

- It does the same thing as `utils`. We tried to change in the source code so that it returns more than 20 videos/audios, but it seems it did not work.

`python3 main.py --max-results 10 --duration 60`

## In utils3, we use `youtubesearchpython`:

- We used `ChannelsSearch` object so that we can search for videos in certain regions. Unfortualtely, the results do not include the duration of the video which means all videos with different lengths pertaining to the area with the term specified will be downloaded.

`python main.py --max-results 1 --region 'Egypt'`

## Note:

- If we need to use any of these, we need to comment/uncomment the necessary lines in `main.py` file.

- The default duration of the audio is 60 seconds as the argument above shows.
- I noticed that we need to increase the number of `--max-results` to get the desired duration. In other words, it is not easy to get durations less than 30 seconds.

## In new_utils:

- we can use the following commad to download audios and save a csv file.

`python main.py --max-results 10 --duration 2020 --region 'Egypt'`

The audios will be downloaded in `audio` directory and the `csv file` will be in data directory. The `csv`file should look as follows:

```
	type	id	term	emotion	duration	new_duration	link
46	video	NtZfG2qE15M	['معصب']	angry	0:27	27	https://www.youtube.com/watch?v=NtZfG2qE15M
48	video	aFCA5_KZ77o	['معصب']	angry	0:16	16	https://www.youtube.com/watch?v=aFCA5_KZ77o
56	video	QsZBHN8MtCA	['معصب']	angry	0:31	31	https://www.youtube.com/watch?v=QsZBHN8MtCA
58	video	2nioS4a6xhA	['معصب']	angry	0:14	14	https://www.youtube.com/watch?v=2nioS4a6xhA

```

- More columns can be added if we want. One issue is the repetition we have when the code assigns the `term` which I working on solving it.
