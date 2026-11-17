def TOH(n,s,d,a):
    if n == 1:
        print(f"Move disk 1 from {s} to {d}")
        return
    TOH(n-1,s,a,d)
    print(f"Move disk {n} from {s} to {d}")
    TOH(n-1,a,d,s)
n = 3
TOH(n,'A','B','C')
