import matplotlib.pyplot as plt

datasets = ["PBMC3K", "PBMC6K", "PBMC10K"]

rank_genes_groups = [1.727, 3.397, 13.573]
compute_statistics = [1.673, 3.307, 13.161]
wilcoxon = [1.624, 3.251, 13.040]
ranks = [1.332, 2.609, 8.653]
basic_stats = [0.126, 0.245, 2.767]

plt.figure(figsize=(10, 6))

plt.plot(datasets, rank_genes_groups, marker="o", label="rank_genes_groups")
plt.plot(datasets, compute_statistics, marker="o", label="compute_statistics")
plt.plot(datasets, wilcoxon, marker="o", label="wilcoxon")
plt.plot(datasets, ranks, marker="o", label="_ranks")
plt.plot(datasets, basic_stats, marker="o", label="_basic_stats")

plt.xlabel("Dataset")
plt.ylabel("Cumulative runtime (seconds)")
plt.title("cProfile Results for rank_genes_groups")
plt.legend()
plt.tight_layout()

plt.savefig("cprofile_rank_genes.png", dpi=300)
