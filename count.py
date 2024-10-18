# calculates how many reviewers reviewed which portion of questions

import json
import numpy as np

if __name__ == "__main__":
    with open("sgStats.json", "r") as fh:
        raw_data = json.load(fh)
    reviewer_count_per_question = []
    num_reviewed_per_reviewer = []
    for user_url, user_data in raw_data.items():
        for _ in user_data:
            reviewer_count_per_question.append(len(user_data))
        num_reviewed_per_reviewer.append(len(user_data))
    ps = [0.25, 0.5, 0.75, 0.8]
    thresholds = np.quantile(reviewer_count_per_question, 1-np.array(ps))
    for p, threshold in zip(ps, thresholds):
        # Note: neither >threshold nor >=threshold is completely correct here
        # The true amount of reviewers reviewing the given threshold is between the value calculated with > and >=.
        # This is because there can be multiple reviewers reviewing the same number of questions and the quantile can be in between reviewers.
        amount=np.sum(np.array(num_reviewed_per_reviewer)>=threshold)
        print(f"{amount:3} ({100*amount/len(num_reviewed_per_reviewer):2.3}%) reviewers reviewed {p} of questions. These each reviewed at least {threshold} questions.")


