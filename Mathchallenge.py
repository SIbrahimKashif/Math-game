import random, time

funcs = ["-", "+", "*"]
maxvalue = 15
minvalue = 3
qs = 10

print("\nTest your mental-math skills with this challenge!")


def challenge():
    func = random.choice(funcs)
    lvalue = random.randint(minvalue, maxvalue)
    rvalue = random.randint(minvalue, maxvalue)

    exp = str(lvalue) + func + str(rvalue)
    ans = eval(exp)

    return exp, ans


input("\nPress enter to start\n")

stime = time.time()

wrong = 0

for i in range(qs):
    exp, ans = challenge()
    while True:
        resp = input(f"Problem #{i+1}: {exp}= ")
        if resp == str(ans):
            break
        else:
            wrong += 1

etime = time.time()
ttime = etime - stime

if ttime < 25 and wrong == 0:
    fb = "Unreal Work!"
elif ttime < 45 and wrong < 3:
    fb = "Awesome Job!"
elif ttime < 75 and wrong < 5:
    fb = "Nice Job!"
else:
    fb = "Good try! Better luck next time,"

duration = str(ttime).split(".")[0]

print(
    f"\n{fb} You answered {qs} questions in *{duration}s* with *{wrong}* questions wrong\n"
)
