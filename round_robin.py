from collections import deque

def round_robin_scheduling(processes, quantum=2):
    queue = deque()
    time = 0
    context_switches = 0
    waiting_time = {}
    turnaround_time = {}
    remaining = {p['pid']: p['burst'] for p in processes}
    total_burst_time = sum(p['burst'] for p in processes)
    original_processes = list(processes)  # Keep original for arrival info
    arrived = []
    processes.sort(key=lambda x: x['arrival'])

    while processes or queue:
        while processes and processes[0]['arrival'] <= time:
            p = processes.pop(0)
            queue.append(p)
            arrived.append(p['pid'])

        if queue:
            p = queue.popleft()
            pid = p['pid']
            start_time = time
            execute = min(quantum, remaining[pid])
            time += execute
            remaining[pid] -= execute
            if remaining[pid] > 0:
                queue.append(p)
            else:
                turnaround_time[pid] = time - p['arrival']
                waiting_time[pid] = turnaround_time[pid] - p['burst']
            context_switches += 1
        else:
            time += 1

    avg_wait = sum(waiting_time.values()) / len(waiting_time)
    avg_turn = sum(turnaround_time.values()) / len(turnaround_time)
    
    cpu_utilization = (total_burst_time / time) * 100
    throughput = len(original_processes) / time

    return {
        'algorithm': 'Round Robin',
        'avg_waiting_time': avg_wait,
        'avg_turnaround_time': avg_turn,
        'context_switches': context_switches,
        'cpu_utilization': round(cpu_utilization, 2),
        'throughput': round(throughput, 2)
    }
    
