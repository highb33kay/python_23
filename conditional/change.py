debt = int(input("Where is my change: "))

if debt == 3000:
    print("Oshey Badest")
elif debt > 3000:
    print(f"This is too much, Comot {debt - 3000}")
else:
    print(f"This money no reach, give me {3000 - debt}")
