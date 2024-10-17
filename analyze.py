import json
import numpy as np
from matplotlib import pyplot as plt
import urllib.parse

SMALL_PLOT = False

def op_plot(ax, user_arrays, op, name, format_spec="%.1f"):
    values = []
    lens = []
    xs = []
    for user_url, arr in user_arrays.items():
        value=op(arr)
        values.append(value)
        lens.append(len(arr))
        user_url_split = user_url.split("/")
        user_name = user_url_split[-1]
        user_id = user_url_split[-2]
        xs.append(urllib.parse.unquote(user_name[0:15]))
    colormap = plt.get_cmap("viridis")
    ax.bar(xs, values, color=colormap(lens))
    if SMALL_PLOT:
        ax.bar_label(ax.containers[0], fmt=format_spec)
    median = np.median(values)
    ax.set_title(f"{name}")
    ax.tick_params(axis='x', labelrotation=-90)
    ax.axhline(median)
    ax.text(ax.get_xlim()[1]+0.1, median, f"median: {median:.3}")


if SMALL_PLOT:
    FILE_SUFFIX="_small.png"
    MIN_QUESTIONS=20
else:
    FILE_SUFFIX="_big.png"
    MIN_QUESTIONS=5

def multiplot(user_arrays, name, include_mean_pos_neg=True, mean_pos_neg_name="mean [positive - negative]"):
    fig, ax = plt.subplots(4 + int(include_mean_pos_neg))
    fig.set_size_inches(25, 15)
    fig.suptitle(name, fontsize=14)
    plt.subplots_adjust(hspace=2.5)
    op_plot(ax[-1], user_arrays, len, "total number of approved questions", format_spec="%d")
    op_plot(ax[-2], user_arrays, np.sum, "sum", format_spec="%d")
    op_plot(ax[0], user_arrays, np.mean, "mean")
    op_plot(ax[1], user_arrays, inter_quantile_mean, "inter quantile mean")
    if include_mean_pos_neg:
        op_plot(ax[2], user_arrays, lambda x: ((np.array(x)>0).sum()-(np.array(x)<0).sum())/len(x), mean_pos_neg_name)
    plt.savefig(f"{name}{FILE_SUFFIX}")
    plt.show()

def boolplot(user_arrays, name):
    fig, ax = plt.subplots(3)
    fig.set_size_inches(25, 15)
    fig.suptitle(name, fontsize=14)
    plt.subplots_adjust(hspace=2.5)
    op_plot(ax[2], user_arrays, len, "total number of approved questions", format_spec="%d")
    op_plot(ax[1], user_arrays, sum, "count", format_spec="%d")
    op_plot(ax[0], user_arrays, lambda x: sum(x)/len(x), "ratio", format_spec="%0.2f")
    plt.savefig(f"{name}{FILE_SUFFIX}")
    plt.show()

def inter_quantile_mean(values):
    values = np.array(values)
    mask = ((values>=np.quantile(values, 0.1)) & (values <=np.quantile(values, 0.9)))
    relevant = values[mask]
    return np.mean(relevant)

if __name__ == "__main__":
    with open("sgStats.json", "r") as fh:
        raw_data = json.load(fh)
    stats = {}
    for user_url, user_data in raw_data.items():
        if len(user_data)>MIN_QUESTIONS:
            user_url_split = user_url.split("/")
            user_name = user_url_split[-1]
            user_id = user_url_split[-2]
            for data in user_data:
                if "closed" not in data:
                    data["closed"]=0
                if "deleted" not in data:
                    data["deleted"]=0
                if "duplicate" not in data:
                    data["duplicate"]=0
                for k,v in data.items():
                    if k not in stats:
                        stats[k] = {}
                    if user_url not in stats[k]:
                        stats[k][user_url]=[]
                    stats[k][user_url].append(v)
    multiplot(stats["votes"], "score")
    multiplot(stats["answers"], "answers", mean_pos_neg_name="ratio of questions with answers")
    multiplot(stats["views"], "views", include_mean_pos_neg=False)
    boolplot(stats["closed"], "closed")
    boolplot(stats["duplicate"], "duplicate")
    boolplot(stats["deleted"], "deleted")
