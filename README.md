# ms-project
A template for students doing M.S. or undergraduate independent studies/theses.

See instructions here: [Instructions.md](Instructions.md)

This README.md file should summarize your project. Think of it as the short version of your project report.

## Problem

Here is the problem your are going to solve.

## Research questions

Here are the core questions / subproblems you will address:

1. ...
2. ...
3. ...

## Related work

Here's how other people have tried to solve this problem, with a few links/citations. 

## Data

#### Data Description
The datas are collected from [TripAdvisor](http://www.tripadvisor.com).

* Crawl datas of hotels in several cities(Current from Chicago, New York, San Francisco, Las Vegas, Orlando)
* Extracted several fields but focus to only full review
* ~850000 reviews have been collected.
* Dataset is not set yet. More cities will be added and will have more datas.
 

#### Data Format
There will be only one file `reviews.txt` which contains all collected raw datas. Within this file, you will see the following structure:

	{"key1":val1 , "key2":val2 , ... , "text": <comments 1>}	
	{"key1":val1 , "key2":val2 , ... , "text": <comments 2>}
	...

Each line is in JSON format and represents an independent review. The `value` comes after `text` key is a review of a hotel.

(The raw data format could be changed in the future.)



## Methods

Here is an outline of your approach.

## Results

Here is a summary of the main results.

## Conclusions / Future Work

Here's the main conclusions and a list of directions for improvement.

