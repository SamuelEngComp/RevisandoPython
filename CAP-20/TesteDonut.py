# library
import matplotlib.pyplot as plt

# create data
names = 'groupA', 'groupB', 'groupC', 'groupD',
size = [12, 11, 3, 30]

# Create a circle for the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# Label distance: gives the space between labels and the center of the pie
plt.pie(size, labels=names, labeldistance=0.45)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.show()

# Label color
plt.rcParams['text.color'] = 'red'
plt.pie(size, labels=names)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.show()

# Custom wedges
plt.pie(size, labels=names, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()