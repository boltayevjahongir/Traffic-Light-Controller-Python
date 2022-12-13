import random
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Tkagg")
tsikl = 10

def cars_count_random(min, max):
    cars_count = []
    for item in range(1, tsikl+1):
        cars_count.append(random.randint(min, max))
    return cars_count

def passed_count_random(min, max):
    passed_count = []
    for item in range(1, tsikl+1):
        passed_count.append(random.randint(min, max))
    return passed_count

def unpassed_count(cars_count, passed_count):
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

A=cars_count_random(9, 16)
A_passed=passed_count_random(5, 11)
delta = unpassed_count(A, A_passed)

print(A)
print(A_passed)
print(delta)

# ax=plt.axes()
# ax.set_facecolor('grey')
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
plt.step(list(range(1, len(A)+1)), A, where='post', label="Mashinalar soni")
plt.step(list(range(1, len(A_passed)+1)), A_passed, where='post', label="O'tkazish qobiliyati")
plt.step(list(range(1, len(delta)+1)), delta, where='post', label="Qolib ketganlar")
plt.legend()
plt.title("Trafic Light Control", fontdict=font1)
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
