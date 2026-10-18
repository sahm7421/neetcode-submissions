from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Count the frequency of each task
        counts = Counter(tasks)
        max_freq = max(counts.values())
        
        # Count how many tasks share the maximum frequency
        max_freq_count = sum(1 for count in counts.values() if count == max_freq)
        
        # Calculate time based on chunk structure:
        # (max_freq - 1) groups of length (n + 1), plus the trailing tasks
        min_time = (max_freq - 1) * (n + 1) + max_freq_count
        
        # Total time is bounded below by the number of tasks
        return max(len(tasks), min_time)