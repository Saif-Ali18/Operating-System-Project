# 📊 OS Project: SJF and Round Robin Comparative Analyzer

This project simulates and compares two CPU scheduling algorithms — **Shortest Job First (SJF)** and **Round Robin (RR)** — along with **Deadlock Detection** and **Memory Management** (First Fit and Best Fit). Visualizations are provided using `matplotlib`.

---

## 📁 Project Structure

```
OS-Project/

🗄 main.py                  # Entry point to run the project
🗄 sjf.py                   # SJF Scheduling implementation
🗄 round_robin.py           # Round Robin implementation
🗄 memory.py                # First Fit and Best Fit logic + visualization
🗄 deadlock.py              # Deadlock detection logic
🗄 plot.py                  # Plotting comparison metrics

```

---

## 🚀 How to Run (on Windows)

### 1. ✅ Prerequisites

- matplotlib library (for graphs)

```bash
pip install matplotlib
```

---

### 2. ▶️ Run the Project

```bash
python main.py
```


## 📈 Features

✅ **Scheduling Algorithms:**

- Shortest Job First (SJF)
- Round Robin (with quantum)

✅ **Performance Metrics:**

- CPU Utilization
- Average Waiting Time
- Average Turnaround Time
- Context Switches
- Throughput

✅ **Deadlock Detection:**

- Safe sequence detection
- Deadlocked processes display

✅ **Memory Management:**

- First Fit Allocation
- Best Fit Allocation
- Visualized as bar graphs

---

## 🧚‍♂️ Sample Input (during execution)

When prompted:

```
Enter memory block sizes: 100 500 200 300 600
Enter process sizes: 212 417 112 426
```

---

## 📊 Visualization Example

Bar graphs showing how memory is allocated to processes using First Fit and Best Fit.

---

## 👨‍💼 Developed By

- Saif , Fahad , Zeeshan
- IET Department
- 4th Semester — Operating Systems Lab

