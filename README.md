# Staging Ground statistics

I took all Staging Ground approvals (state: 17.10.2024) from the review history (16806 posts in total), grouped these by user, filtered out inactive users and created bar charts out of it.

General statistics collected from the script using these approvals:
```none
retrieval log from 17.10.2024

posts checked: 16806
average votes: 0.07533023920028561 (total: 1266)
average answers: 0.37980483160775913 (total: 6383)
average views: 66.40342734737594 (total: 1115976)
average duplicate: 0.047840057122456266 (total: 804)
average deleted: 0.17356896346542902 (total: 2917)
average closed: 0.08241104367487802 (total: 1385)

error: 36
error request failure (no information about answers in post): 36
```

The ones with "big" in the name include all users who contributed more than 20 of these approvals, ones marked "small" only include users who contributed more than 40 of these approvals.

The horizontal lines represents the median.

- `mean` refers to the mean votes/views on questions approved by the reviewer.
- `interquantile mean` is the mean excluding outliers (anything smaller than the 10%th quantile or greater than the 90% quantile)
- `mean [positive - negative]` refers to the number of questions with a positive score minus the number of questions with a negative score normalized by the total number of approved questions
- `ratio of questions with answers` is the amount of approved questions divided by the amount of approved questions with at least one answer
- `sum` is the sum of votes/views of all questions the reviewer has approved.
- `total number of approved questions` is the total number of questions the reviewer has approved.
- ratio is the of approved questions with the attribute divided by the approval count i.e. the ratio of closed/deleted questions (or mean number of answers, I know the title doesn't fit here)
- count is the total number of closed/deleted questions or answers to questions the reviewer has approved

The data was collected using [this userscript](https://github.com/danthe1st/SO-Userscripts/?tab=readme-ov-file#approved-staging-ground-review-statistics)
