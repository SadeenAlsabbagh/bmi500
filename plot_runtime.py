import matplotlib.pyplot as plt

datasets = [3, 6, 10]

normalization = [0.0445, 0.0700, 0.4468]
highly_variable = [0.0692, 0.0788, 0.4595]
scaling = [0.0413, 0.0743, 0.1706]
pca = [0.3378, 0.5599, 2.0478]
neighbors = [4.1083, 4.0346, 30.5457]
louvain = [0.1267, 0.3582, 0.8066]
umap = [8.4489, 15.8173, 14.1890]
write_output = [0.1661, 0.2568, 0.6890]
rank_genes = [1.9042, 3.5704, 13.5918]

plt.figure(figsize=(10, 6))

plt.plot(datasets, normalization, marker='o', label='Normalization')
plt.plot(datasets, highly_variable, marker='o', label='Highly variable genes')
plt.plot(datasets, scaling, marker='o', label='Scaling')
plt.plot(datasets, pca, marker='o', label='PCA')
plt.plot(datasets, neighbors, marker='o', label='Neighbors')
plt.plot(datasets, louvain, marker='o', label='Louvain')
plt.plot(datasets, umap, marker='o', label='UMAP')
plt.plot(datasets, write_output, marker='o', label='Write output')
plt.plot(datasets, rank_genes, marker='o', label='Rank genes')

plt.xlabel('Dataset size (thousands of cells)')
plt.ylabel('Runtime (seconds)')
plt.title('Scanpy Runtime by Dataset Size')
plt.xticks(datasets, ['PBMC3K', 'PBMC6K', 'PBMC10K'])
plt.legend()
plt.tight_layout()

plt.savefig('scanpy_runtime.png', dpi=300)
