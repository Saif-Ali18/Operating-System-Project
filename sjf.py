def sjf_scheduling(processes):
    time = 0
    completed = 0
    n = len(processes)
    context_switches = 0
    waiting_time = {}
    turnaround_time = {}
    is_completed = [False] * n
    total_burst_time = sum(p['burst'] for p in processes)

    while completed < n:
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if processes[i]['arrival'] <= time and not is_completed[i]:
                if processes[i]['burst'] < min_burst:
                    min_burst = processes[i]['burst']
                    idx = i
        if idx != -1:
            p = processes[idx]
            start = time
            time += p['burst']
            waiting_time[p['pid']] = start - p['arrival']
            turnaround_time[p['pid']] = time - p['arrival']
            is_completed[idx] = True
            completed += 1
            context_switches += 1
        else:
            time += 1

    avg_wait = sum(waiting_time.values()) / n
    avg_turn = sum(turnaround_time.values()) / n
    cpu_utilization = (total_burst_time / time) * 100
    throughput = n / time

    return {
        'algorithm': 'SJF',
        'avg_waiting_time': avg_wait,
        'avg_turnaround_time': avg_turn,
        'context_switches': context_switches,
        'cpu_utilization': round(cpu_utilization, 2),
        'throughput': round(throughput, 2)
    }
