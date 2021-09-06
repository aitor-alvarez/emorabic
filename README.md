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
	type	id	term	duration	new_duration	link
0	video	SYuDWeJs8nc	['ضحك', 'ضحك', 'ضحك', 'ضحك']	3:46	346	https://www.youtube.com/watch?v=SYuDWeJs8nc
1	video	PTgyeMbcwqw	['ضحك']	1:30	130	https://www.youtube.com/watch?v=PTgyeMbcwqw

```

- More columns can be added if we want. One issue is the repetition we have when the code assigns the `term` which I working on solving it.
