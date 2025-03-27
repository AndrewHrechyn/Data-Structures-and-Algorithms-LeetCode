# # import matplotlib.pyplot as plt
# # import pandas as pd
# # import seaborn as sns
# #
# # # Вхідні дані у вигляді списку словників
# # data = [
# #     {"Threads": 1, "Chunk Size": 1, "Type": "static", "Time": 0.011, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 2, "Type": "static", "Time": 0.011, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 4, "Type": "static", "Time": 0.011, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 6, "Type": "static", "Time": 0.011, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 8, "Type": "static", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 16, "Type": "static", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 32, "Type": "static", "Time": 0.011, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 64, "Type": "static", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 100, "Type": "static", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 1, "Type": "dynamic", "Time": 0.009, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 2, "Type": "dynamic", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 4, "Type": "dynamic", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 6, "Type": "dynamic", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 8, "Type": "dynamic", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 16, "Type": "dynamic", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 32, "Type": "dynamic", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 64, "Type": "dynamic", "Time": 0.011, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 100, "Type": "dynamic", "Time": 0.010, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 1, "Type": "guided", "Time": 0.006, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 2, "Type": "guided", "Time": 0.006, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 4, "Type": "guided", "Time": 0.006, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# #     {"Threads": 1, "Chunk Size": 6, "Type": "guided", "Time": 0.006, "Max Imbalance": 0, "Percentage Imbalance": 0.00},
# # ]
# #
# # # Конвертація у DataFrame
# # df = pd.DataFrame(data)
# #
# # # Побудова графіків
# # plt.figure(figsize=(12, 6))
# # sns.lineplot(data=df, x="Chunk Size", y="Time", hue="Type", marker="o")
# # plt.title("Час виконання залежно від розміру чанка та типу розподілу")
# # plt.xlabel("Chunk Size")
# # plt.ylabel("Time (Seconds)")
# # plt.legend(title="Тип розподілу")
# # plt.grid(True)
# # plt.show()
#
#
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # Дані у вигляді словника
# data = {
#     "Threads": [1] * 27 + [2] * 27 + [4] * 27 + [8] * 27 + [16] * 27,
#     "Chunk Size": [1, 2, 4, 6, 8, 16, 32, 64, 100] * 5 * 3,
#     "Type": (["static"] * 9 + ["dynamic"] * 9 + ["guided"] * 9) * 5,
#     "Time (ms)": [
#         0.011, 0.011, 0.011, 0.011, 0.010, 0.010, 0.011, 0.010, 0.010,  # static, 1 thread
#         0.009, 0.010, 0.010, 0.010, 0.010, 0.010, 0.010, 0.011, 0.010,  # dynamic, 1 thread
#         0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.005, 0.007, 0.007,  # guided, 1 thread
#
#         0.022, 0.026, 0.017, 0.016, 0.016, 0.015, 0.015, 0.020, 0.015,  # static, 2 threads
#         0.021, 0.020, 0.022, 0.020, 0.021, 0.020, 0.021, 0.022, 0.018,  # dynamic, 2 threads
#         0.013, 0.012, 0.011, 0.010, 0.010, 0.011, 0.011, 0.011, 0.011,  # guided, 2 threads
#
#         0.015, 0.016, 0.016, 0.016, 0.015, 0.016, 0.016, 0.016, 0.015,  # static, 4 threads
#         0.016, 0.016, 0.016, 0.015, 0.016, 0.017, 0.016, 0.016, 0.016,  # dynamic, 4 threads
#         0.010, 0.010, 0.010, 0.009, 0.010, 0.009, 0.011, 0.009, 0.009,  # guided, 4 threads
#
#         0.016, 0.016, 0.015, 0.016, 0.016, 0.017, 0.017, 0.016, 0.016,  # static, 8 threads
#         0.017, 0.019, 0.016, 0.016, 0.016, 0.016, 0.016, 0.016, 0.015,  # dynamic, 8 threads
#         0.011, 0.011, 0.010, 0.011, 0.009, 0.010, 0.009, 0.010, 0.010,  # guided, 8 threads
#
#         0.017, 0.016, 0.016, 0.019, 0.023, 0.015, 0.016, 0.014, 0.014,  # static, 16 threads
#         0.017, 0.015, 0.015, 0.016, 0.015, 0.014, 0.015, 0.014, 0.013,  # dynamic, 16 threads
#         0.010, 0.010, 0.010, 0.009, 0.010, 0.010, 0.008, 0.009, 0.009  # guided, 16 threads
#     ]
# }
#
# # Створення датафрейму
# df = pd.DataFrame(data)
#
# # Побудова графіків
# plt.figure(figsize=(12, 6))
#
# # Візуалізація для кожного типу розподілу
# types = ["static", "dynamic", "guided"]
# colors = ["red", "blue", "green"]
#
# for t, c in zip(types, colors):
#     subset = df[df["Type"] == t]
#     for threads in sorted(df["Threads"].unique()):
#         sub_subset = subset[subset["Threads"] == threads]
#         plt.plot(sub_subset["Chunk Size"], sub_subset["Time (ms)"], marker='o', linestyle='-',
#                  label=f"{t} - {threads} threads", color=c, alpha=0.7)
#
# plt.xlabel("Chunk Size")
# plt.ylabel("Execution Time (ms)")
# plt.title("Execution Time vs Chunk Size for Different Scheduling Types and Thread Counts")
# plt.legend()
# plt.grid(True)
# plt.show()
#


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Вхідні дані
threads = np.array([1, 2, 4, 8, 16])
execution_time_static = np.array([0.0105, 0.0185, 0.0155, 0.0160, 0.0160])
execution_time_dynamic = np.array([0.0095, 0.0190, 0.0160, 0.0165, 0.0145])
execution_time_guided = np.array([0.0060, 0.0110, 0.0100, 0.0095, 0.0090])

imbalance_static = np.array([0.00, 20.00, 20.00, 20.00, 20.00])
imbalance_dynamic = np.array([0.00, 20.00, 20.00, 20.00, 20.00])
imbalance_guided = np.array([0.00, 0.24, 3.74, 4.63, 12.91])

# Створення графіків
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Графік 1: Час виконання vs. Кількість потоків
axes[0, 0].plot(threads, execution_time_static, label="Static", marker="o")
axes[0, 0].plot(threads, execution_time_dynamic, label="Dynamic", marker="s")
axes[0, 0].plot(threads, execution_time_guided, label="Guided", marker="^")
axes[0, 0].set_title("Час виконання vs. Кількість потоків")
axes[0, 0].set_xlabel("Кількість потоків")
axes[0, 0].set_ylabel("Час виконання (с)")
axes[0, 0].legend()
axes[0, 0].grid()

# Графік 2: Максимальний дисбаланс vs. Кількість потоків
axes[0, 1].plot(threads, imbalance_static, label="Static", marker="o")
axes[0, 1].plot(threads, imbalance_dynamic, label="Dynamic", marker="s")
axes[0, 1].plot(threads, imbalance_guided, label="Guided", marker="^")
axes[0, 1].set_title("Відсотковий дисбаланс vs. Кількість потоків")
axes[0, 1].set_xlabel("Кількість потоків")
axes[0, 1].set_ylabel("Відсотковий дисбаланс (%)")
axes[0, 1].legend()
axes[0, 1].grid()

# Графік 3: Порівняння різних типів балансування
x_labels = ["Static", "Dynamic", "Guided"]
avg_time = [np.mean(execution_time_static), np.mean(execution_time_dynamic), np.mean(execution_time_guided)]
axes[1, 0].bar(x_labels, avg_time, color=["blue", "green", "red"])
axes[1, 0].set_title("Середній час виконання для різних балансувань")
axes[1, 0].set_ylabel("Час виконання (с)")

# Відключення четвертого графіка (залишимо порожнім)
axes[1, 1].axis("off")

plt.tight_layout()
plt.show()

