with open("13.txt") as f:
    start_time = int(f.readline())
    busses = [int(i) for i in f.readline().split(",") if i != "x"]

time, bus_id = min((i-(start_time%i),  i) for i in busses)
print(time * busses)