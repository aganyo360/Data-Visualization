import matplotlib.pyplot as plt

squares =[1,4,9,16,25, 36]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=5)
plt.savefig('output.png')
plt.show()
