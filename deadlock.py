def detect_deadlock(processes, allocation, max_demand, available):
    n = len(processes)
    m = len(available)
    finish = [False] * n
    work = available[:]
    safe_seq = []

    while True:
        found = False
        for i in range(n):
            if not finish[i]:
                need = [max_demand[i][j] - allocation[i][j] for j in range(m)]
                if all(need[j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allocation[i][j]
                    safe_seq.append(processes[i])
                    finish[i] = True
                    found = True
        if not found:
            break

    deadlock_processes = [processes[i] for i in range(n) if not finish[i]]

    return {
        'deadlock': len(deadlock_processes) > 0,
        'deadlocked_processes': deadlock_processes,
        'safe_sequence': safe_seq if len(deadlock_processes) == 0 else None
    }

def get_deadlock_input():
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resource types: "))

    processes = [f'P{i}' for i in range(n)]

    print("\nEnter Allocation Matrix:")
    allocation = [[int(x) for x in input(f"Allocation for P{i}: ").split()] for i in range(n)]

    print("\nEnter Max Demand Matrix:")
    max_demand = [[int(x) for x in input(f"Max demand for P{i}: ").split()] for i in range(n)]

    print("\nEnter Available Resources:")
    available = [int(x) for x in input("Available: ").split()]

    return processes, allocation, max_demand, available
