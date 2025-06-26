def first_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= processes[i]:
                allocation[i] = j
                memory_blocks[j] -= processes[i]
                break
                visualize_memory_allocation(memory_blocks, allocation)
    return allocation


def best_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= processes[i]:
                if best_idx == -1 or memory_blocks[j] < memory_blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            memory_blocks[best_idx] -= processes[i]
            visualize_memory_allocation(memory_blocks, allocation)

    return allocation


def display_allocation(processes, allocation, algo_name):
    print(f"\n--- {algo_name} Allocation ---")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"Process {i + 1} of size {processes[i]} -> Block {allocation[i] + 1}")
        else:
            print(f"Process {i + 1} of size {processes[i]} -> Not Allocated")

import matplotlib.pyplot as plt

def visualize_memory_allocation(memory_blocks, allocations):
    fig, ax = plt.subplots(figsize=(10, 2))
    y = 0

    for i, size in enumerate(memory_blocks):
        color = 'lightgreen' if i in allocations else 'lightcoral'
        label = f'P{allocation[i]}' if allocation[i] != -1 else 'Free'

        ax.barh(y, size, left=sum(memory_blocks[:i]), height=0.5, color=color, edgecolor='black')
        ax.text(sum(memory_blocks[:i]) + size/2, y, label, ha='center', va='center', fontsize=10)

    ax.set_xlim(0, sum(memory_blocks))
    ax.set_ylim(-0.5, 1)
    ax.set_yticks([])
    ax.set_title('Memory Allocation Visualization')
    ax.set_xlabel('Memory Size')
    plt.tight_layout()
    plt.show()
