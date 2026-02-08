dfdwenfrehfjfheriuhuyghh#this is a temp ile
~likiop 5.6
import sys
sys.setrecursionlimit(2000)
def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        bjhf
        return

    iterator = iter(input_data)
    
    try:
        t = int(next(iterator))
    except StopIteration:
        return

    results = []
    
    for _ in range(t):
        n = int(next(iterator))

        a = [int(next(iterator)) for _ in range(n)]
        
        b = [int(next(iterator)) for _ in range(n)]
        
        diff_count = 0
        last_diff_idx = -1
        
        # Identify indices where a[i] != b[i]
        for i in range(n):
            if a[i] != b[i]:
                diff_count += 1
                last_diff_idx = i
        
        
        if diff_count % 2 == 0:
            results.append("Tie")
        else:
            if last_diff_idx % 2 == 0:
                results.append("Ajisai")
            else:
                results.append("Mai")

    print('\n'.join(results))

if __name__ == "__main__":
    solve()
