from sjf import sjf_scheduling 
from round_robin import round_robin_scheduling 

def take_input():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        print(f"\nEnter details for Process {i+1}:")
        pid = input("PID: ")
        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))
        processes.append({'pid': pid, 'arrival': arrival, 'burst': burst})
    quantum = int(input("\nEnter Time Quantum (for Round Robin): "))
    return processes, quantum

def display_result(result):
    print(f"\n📊 {result['algorithm']} Results:")
    print(f"🔹 Average Waiting Time     : {result['avg_waiting_time']:.2f}")
    print(f"🔹 Average Turnaround Time  : {result['avg_turnaround_time']:.2f}")
    print(f"🔹 Context Switches         : {result['context_switches']}")
    print(f"🔹 CPU Utilization          : {result['cpu_utilization']:.2f}%")
    print(f"🔹 Throughput               : {result['throughput']:.2f} processes/unit time\n")


if __name__ == "__main__":
    processes, quantum = take_input()
    rr_result = round_robin_scheduling(processes.copy(), quantum)
    sjf_result = sjf_scheduling(processes.copy())
    display_result(sjf_result)
    display_result(rr_result)

from plot import plot_comparison
plot_comparison(sjf_result, rr_result)

from deadlock import detect_deadlock, get_deadlock_input

def handle_deadlock():
    print("\n--- Deadlock Detection ---")
    processes, allocation, max_demand, available = get_deadlock_input()
    result = detect_deadlock(processes, allocation, max_demand, available)

    if result['deadlock']:
        print("Deadlock detected in processes:", result['deadlocked_processes'])
    else:
        print("No Deadlock detected.")
        print("Safe Sequence:", ' → '.join(result['safe_sequence']))
        
handle_deadlock()

from memory import first_fit, best_fit, display_allocation

def handle_memory_allocation():
    print("\n--- Memory Management ---")
    blocks = list(map(int, input("Enter memory block sizes: ").split()))
    processes = list(map(int, input("Enter process sizes: ").split()))

    # First Fit
    ff_alloc = first_fit(blocks.copy(), processes)
    display_allocation(processes, ff_alloc, "First Fit")

    # Best Fit
    bf_alloc = best_fit(blocks.copy(), processes)
    display_allocation(processes, bf_alloc, "Best Fit")
    
handle_memory_allocation()
