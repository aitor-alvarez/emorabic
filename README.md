### How to use this code:

- we can use the following commad to download audios and save them to csv file.

`python main.py --max-results 10 --duration 2020 --region 'Egypt'`

The audios will be downloaded in `audio` directory and the `csv file` will be in data directory.

In the `audio` directory, there are `egyptian`, `gulf`, `levantine`, `moroccan` and `tunisian` directories where the downloaded audio/s will be saved in these directories depending on the region. The same applies to the `csv files` that will be saved in the `data` directory.

When switching between the `region` on the commadline, we need to fix the code to reflect the result in both `audio` and `data` directories. This can be done by fixing line `65` in utils:

```
datafile = "./data/gulf.csv"
```

and line `73` in utils as well:

```
"outtmpl": "./audio/gulf/%(id)s.%(ext)s"
```

The `csv`file should look as follows:

```
	type	id	term	emotion	region	duration	link
1683	video	CpSCDjftbxY	['يفضح']	surprise	Kuwait	2:34	https://www.youtube.com/watch?v=CpSCDjftbxY
1700	video	LMAQIuo2oWA	['يفضح']	surprise	Kuwait	2:25	https://www.youtube.com/watch?v=LMAQIuo2oWA
1701	video	RCM7T2Qm9p8	['يفضح']	surprise	Kuwait	9:58	https://www.youtube.com/watch?v=RCM7T2Qm9p8
1702	video	VuogUDHetA8	['يفضح']	surprise	Kuwait	2:20	https://www.youtube.com/watch?v=VuogUDHetA8
1703	video	14GG7orZYXk	['يفضح']	surprise	Kuwait	10:26	https://www.youtube.com/watch?v=14GG7orZYXk
1705	video	h1PyFdH3T4Y	['يفضح']	surprise	Kuwait	2:23	https://www.youtube.com/watch?v=h1PyFdH3T4Y
1706	video	3OmfFcWnqU0	['يفضح']	surprise	Kuwait	10:08	https://www.youtube.com/watch?v=3OmfFcWnqU0
1707	video	BqcQJG-POfE	['يفضح']	surprise	Kuwait	3:49	https://www.youtube.com/watch?v=BqcQJG-POfE
1708	video	bz_Vp-W5_-4	['يفضح']	surprise	Kuwait	1:35	https://www.youtube.com/watch?v=bz_Vp-W5_-4

```

- NOTES: I just noticed that `terms` overlap between different dialects so I suggest separating our downloaded audios by region.
