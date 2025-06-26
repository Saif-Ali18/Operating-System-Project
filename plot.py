import matplotlib.pyplot as plt

def plot_comparison(sjf_result, rr_result):
    algorithms = [sjf_result['algorithm'], rr_result['algorithm']]
    waiting_times = [sjf_result['avg_waiting_time'], rr_result['avg_waiting_time']]
    turnaround_times = [sjf_result['avg_turnaround_time'], rr_result['avg_turnaround_time']]
    context_switches = [sjf_result['context_switches'], rr_result['context_switches']]
    cpu_utilizations = [sjf_result['cpu_utilization'], rr_result['cpu_utilization']]
    throughputs = [sjf_result['throughput'], rr_result['throughput']]

    x = range(len(algorithms))

    plt.figure(figsize=(15, 10))

    # Average Waiting Time
    plt.subplot(2, 3, 1)
    plt.bar(x, waiting_times, color=['skyblue', 'orange'])
    plt.xticks(x, algorithms)
    plt.title("Average Waiting Time")
    plt.ylabel("Time")

    # Average Turnaround Time
    plt.subplot(2, 3, 2)
    plt.bar(x, turnaround_times, color=['lightgreen', 'salmon'])
    plt.xticks(x, algorithms)
    plt.title("Average Turnaround Time")
    plt.ylabel("Time")

    # Context Switches
    plt.subplot(2, 3, 3)
    plt.bar(x, context_switches, color=['plum', 'lightcoral'])
    plt.xticks(x, algorithms)
    plt.title("Context Switches")
    plt.ylabel("Count")

    # CPU Utilization
    plt.subplot(2, 3, 4)
    plt.bar(x, cpu_utilizations, color=['gold', 'lightblue'])
    plt.xticks(x, algorithms)
    plt.title("CPU Utilization (%)")
    plt.ylabel("Percentage")

    # Throughput
    plt.subplot(2, 3, 5)
    plt.bar(x, throughputs, color=['lightseagreen', 'coral'])
    plt.xticks(x, algorithms)
    plt.title("Throughput")
    plt.ylabel("Processes/Unit Time")

    plt.tight_layout()
    plt.show()
