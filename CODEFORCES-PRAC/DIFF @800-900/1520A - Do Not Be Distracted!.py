def task_monitor(x:str):
    global cmp_task
    cmp_task = set()
    prv_task = ""
    for task in x:
        if task != prv_task:
            if task in cmp_task:
                return("NO")
            cmp_task.add(task)
            prv_task = task
    return("YES")
t = int(input())
for _ in range(t):
    n = int(input())
    task_str = input()
    print(task_monitor(task_str))
