import matplotlib.pyplot as plt

datasets = ["PBMC3K", "PBMC6K", "PBMC10K"]

wall_time = [26.33, 35.98, 74.30]
cpu_percent = [103, 103, 109]
memory_kb = [892652, 924912, 1359452]

# Wall-clock time
plt.figure(figsize=(7, 5))
plt.bar(datasets, wall_time)
plt.xlabel("Dataset")
plt.ylabel("Wall-clock time (seconds)")
plt.title("Coarse-Grain Profiling: Wall-Clock Time")
plt.tight_layout()
plt.savefig("coarse_walltime.png", dpi=300)
plt.close()

# CPU utilization
plt.figure(figsize=(7, 5))
plt.bar(datasets, cpu_percent)
plt.xlabel("Dataset")
plt.ylabel("CPU utilization (%)")
plt.title("Coarse-Grain Profiling: CPU Utilization")
plt.tight_layout()
plt.savefig("coarse_cpu.png", dpi=300)
plt.close()

# Peak memory
memory_mb = [x / 1024 for x in memory_kb]

plt.figure(figsize=(7, 5))
plt.bar(datasets, memory_mb)
plt.xlabel("Dataset")
plt.ylabel("Peak memory (MB)")
plt.title("Coarse-Grain Profiling: Peak Memory")
plt.tight_layout()
plt.savefig("coarse_memory.png", dpi=300)
plt.close()

