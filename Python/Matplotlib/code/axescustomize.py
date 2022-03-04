import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_title('Title!', fontsize=20)
ax.set_xlabel('X label', fontsize=15)
ax.set_ylabel('Y label', fontsize=15)

plt.show()

title_list = ['Ax' + str(i) for i in range(4)]
xlabel_list = ['X label ' + str(i) for i in range(4) ]
ylabel_list = ['Y label ' + str(i) for i in range(4) ]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
for ax_idx, ax in enumerate(axes.flat):
    ax.set_title(title_list[ax_idx], fontsize=30)
    ax.set_xlabel(xlabel_list[ax_idx], fontsize=20)
    ax.set_ylabel(ylabel_list[ax_idx], fontsize=20)


#fig.tight_layout()

#fig.subplot_adjust()

plt.show()