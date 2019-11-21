import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(constrained_layout=True)

gs = GridSpec(3, 3, figure=fig)

x = ["um","dois","tres"]
y = [1,2,3]

ax1 = fig.add_subplot(gs[0, :])
ax1.set_title("teste 1")
ax1.bar(x,y,width=0.32)
ax1.set_ylabel("qtd")
ax1.set_xlabel("dias")

# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = fig.add_subplot(gs[1, :-1])
ax2.set_title("teste 2")
ax2.bar(x,y,width=0.32)
ax2.set_ylabel("qtd")
ax2.set_xlabel("dias")

ax3 = fig.add_subplot(gs[1:, -1])
ax3.set_title("teste 3")
# ax3.bar(x,y,width=0.32)
ax3.pie(y,labels = x)
# ax3.set_ylabel("qtd")
# ax3.set_xlabel("dias")

ax4 = fig.add_subplot(gs[-1, 0])
ax4.set_title("teste 4")
ax4.bar(x,y,width=0.32)
ax4.set_ylabel("qtd")
ax4.set_xlabel("dias")

ax5 = fig.add_subplot(gs[-1, -2])
ax5.set_title("teste 5")
ax5.bar(x,y,width=0.32)
ax5.set_ylabel("qtd")
ax5.set_xlabel("dias")



fig.suptitle("Atividades NUTS 2018")
plt.show()
