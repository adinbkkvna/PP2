def solve(heads,legs):
    rabbits=(legs-2*heads)//2
    chickens=heads-rabbits

    if rabbits <0 or chickens<0:
        print("No solution")
    else:
        print(rabbits)
        print(chickens)
solve(35,94)