import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 5.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
plt.axis("equal")

ax.set(xlim=(-10, 10), ylim=(-10, 10))

for i in range(0, 7):
   rainbow = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
   c = plt.Circle((0, 0), 7-i, fill=True, color=rainbow[i])
   ax.add_artist(c)

plt.show()