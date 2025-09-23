def brute_force(arr, k):
    grabs = [i for i, c in enumerate(arr) if c == 'G']
    passengers = [i for i, c in enumerate(arr) if c == 'P']
    
    max_count = 0
    solutions = 0

    def backtrack(i, used, count):
        nonlocal max_count, solutions

        # ถึง grab คันสุดท้ายแล้ว → อัพเดทคำตอบ
        if i == len(grabs):
            if count > max_count:
                max_count = count
                solutions = 1
            elif count == max_count:
                solutions += 1
            return

        # กรณีไม่ใช้ Grab คันนี้
        backtrack(i+1, used, count)

        # กรณีใช้ Grab คันนี้จับกับผู้โดยสาร
        for p in passengers:
            if p not in used and abs(grabs[i] - p) <= k:
                used.add(p)
                backtrack(i+1, used, count+1)
                used.remove(p)

    backtrack(0, set(), 0)
    return solutions, max_count


def greedy(arr, k):
    arr = list(arr)
    n = len(arr)
    count = 0
    
    for i in range(n):
        if arr[i] == 'P':
            for j in range(max(0, i-k), min(n, i+k+1)):
                if arr[j] == 'G':
                    count += 1
                    arr[j] = 'X'   # Grab นี้ถูกใช้แล้ว
                    break
    return count




with open("lab4/testcase/normal/4.1.1.txt", 'r') as file:
    lines = file.readlines()

arr = str(lines[0].strip())
k = int(lines[1].strip())

# ---------------- Main ----------------
if __name__ == "__main__":

    # Brute force
    #solutions, max_count = brute_force(arr, k)
    #print("Brute force → วิธีทั้งหมด =", solutions, ", ผู้โดยสารสูงสุด =", max_count)

    # Greedy
    greedy_count = greedy(arr, k)
    print("Greedy → ผู้โดยสารสูงสุด =", greedy_count)