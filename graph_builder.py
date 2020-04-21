import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

count = [10000, 100000, 1000000, 10000000]

timewithout_indexes = [0.0126, 0.1054, 0.7582, 6.9992]
timewith_indexes = [0.0032, 0.0026, 0.0028, 0.01399]

fig, ax = plt.subplots()

plt.xlabel('count of items in DB, :10000000')
plt.ylabel('execution time, sec')
ax.plot(count, timewithout_indexes,  color = 'r', linewidth = 1,  marker='o')
ax.plot(count, timewith_indexes,  color = 'g', linewidth = 1, marker='o')


ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))


fig.set_figwidth(12)
fig.set_figheight(8)


plt.show()
