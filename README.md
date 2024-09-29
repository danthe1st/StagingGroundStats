# Staging Ground statistics

I took the last 100 pages of Staging Ground approvals (state: 29.9.2024) from the review history, grouped these by user, filtered out inactive users and created bar charts out of it.

The ones with "big" in the name include all users who contributed more than 5 of these approvals, ones marked "small" only include users who contributed more than 20 of these approvals.

The horizontal lines represents the median.

- `mean` refers to the mean votes/views on questions approved by the reviewer.
- `interquantile mean` is the mean excluding outliers (anything smaller than the 10%th quantile or greater than the 90% quantile)
- `mean [positive - negative]` refers to the number of questions with a positive score minus the number of questions with a negative score normalized by the total number of approved questions
- `ratio of questions with answers` is the amount of approved questions divided by the amount of approved questions with at least one answer
- `sum` is the sum of votes/views of all questions the reviewer has approved.
- `total number of approved questions` is the total number of questions the reviewer has approved.
- ratio is the of approved questions with the attribute divided by the approval count i.e. the ratio of closed/deleted questions (or mean number of answers, I know the title doesn't fit here)
- count is the total number of closed/deleted questions or answers to questions the reviewer has approved

