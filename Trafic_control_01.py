import random
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Tkagg")
tsikl = 10


A = [5, 12]


def cars_count_random(min, max):
    cars_count = []
    for item in range(1, tsikl+1):
        cars_count.append(random.randint(min, max))
    return cars_count

def passed_count_random(min, max, type):
    passed_count = []
    for item in range(type, tsikl+type):
        if item%2==0:
            passed_count.append(0)
        else:
            passed_count.append(random.randint(min, max))
    return passed_count

def unpassed_count_AB(cars_count, passed_count):
    unpassed = []
    traffic_light = 1  # 1-Green(yashil), 0-Red(qizil)
    delta=0
    for cars_count_item, passed_count_item in zip(cars_count, passed_count):
        print(traffic_light, end=",  ")
        if traffic_light == 1:
            delta = cars_count_item - passed_count_item + delta
            if delta < 0:
                delta = 0
            traffic_light = 0
        else:
            delta = cars_count_item + delta
            traffic_light = 1
        unpassed.append(delta)
    print("\n")
    return unpassed
def unpassed_count(cars_count, passed_count, type):
    unpassed = []
    traffic_light = type  # 1-Green(yashil), 0-Red(qizil)
    delta=0
    for cars_count_item, passed_count_item in zip(cars_count, passed_count):
        print(traffic_light, end=",  ")
        if traffic_light == 1:
            delta = cars_count_item - passed_count_item + delta
            if delta < 0:
                delta = 0
            traffic_light = 0
        else:
            delta = cars_count_item + delta
            traffic_light = 1
        unpassed.append(delta)
    print("\n")
    return unpassed



A=cars_count_random(5, 15)
A_passed=passed_count_random(10, 18, 1)
B=cars_count_random(5, 15)
B_passed=passed_count_random(10, 18, 1)
delta = unpassed_count(A, A_passed, 1)
deltaB = unpassed_count(B, B_passed, 1)

# CD tomon
C=cars_count_random(5, 15)
C_passed=passed_count_random(10, 18, 0)
D=cars_count_random(5, 15)
D_passed=passed_count_random(10, 18, 0)
deltaC = unpassed_count(C, C_passed, 0)
deltaD = unpassed_count(D, D_passed, 0)

print(A)
print(A_passed)
print(delta)
print("")
print(C_passed)


# ax=plt.axes()
# ax.set_facecolor('grey')
plt.figure(1)
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
plt.step(list(range(1, len(A)+1)), A, where='post', label="Mashinalar soni")
plt.step(list(range(1, len(A_passed)+1)), A_passed, where='post', label="O'tkazish qobiliyati")
plt.step(list(range(1, len(delta)+1)), delta, where='post', label="Qolib ketganlar")
plt.legend()
plt.title("Trafic Light Control (A-B)", fontdict=font1)
plt.ylim(ymin=0)
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.figure(2)
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
plt.step(list(range(1, len(C)+1)), C, where='post', label="Mashinalar soni")
plt.step(list(range(1, len(C_passed)+1)), C_passed, where='post', label="O'tkazish qobiliyati")
plt.step(list(range(1, len(deltaC)+1)), deltaC, where='post', label="Qolib ketganlar")
plt.legend()
plt.title("Trafic Light Control(C-D)", fontdict=font1)
plt.ylim(ymin=0)
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()
exit()


    #
    # A = random.randint(9, 16)  # Adan B ga kelayotgan mashinalar soni
    # B = random.randint(5, 11)  # B dan A ga kelayotgan mashinalar soni
    # C = random.randint(5, 10)  # C dan D ga kelayotgan mashinalar soni
    # D = random.randint(4, 9)  # D dan C ga kelayotgan mashinalar soni
    #
    # AB = random.randint(7, 18)  # Adan B ga yashil chiroqda o'tish imkoniyati
    # BA = random.randint(3, 12)  # B dan A ga yashil chiroqda o'tish imkoniyati
    # CD = random.randint(3, 12)  # C dan D ga yashil chiroqda o'tish imkoniyati
    # DC = random.randint(2, 11)  # D dan C ga yashil chiroqda o'tish imkoniyati
