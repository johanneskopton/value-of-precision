import daft
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Helvetica"
})

# Colors.
p_color = {"ec": "#46a546"}
s_color = {"ec": "#f89406"}

pgm = daft.PGM()

# Nodes.
pgm.add_node("clusters", r"$x_i$", 2, 3, observed=True)
pgm.add_node("classes", r"$y_i ^j$", 3, 1, observed=True)
pgm.add_node("classes_prob", r"$p_i ^j$", 2, 1)
pgm.add_node("beta", r"$\beta^j_{a, b, c}$", 1, 1)
pgm.add_node("apples", r"$y^{\mathsf{total}}_i$", 3, 2)
pgm.add_node("apple_prob", r"$p^{x\rightarrow y}_i$", 3, 3)
# pgm.add_node("b", r"$b$", 4, 3.1, fixed=True)
pgm.add_node("m", r"$m$", 4, 3.0)
pgm.add_node("s", r"$s$", 4, 2.3)
pgm.add_node("b", r"$b$", 4, 1.6)

# Edges.
pgm.add_edge("apples", "classes")
pgm.add_edge("classes_prob", "classes")
pgm.add_edge("apple_prob", "apples")
pgm.add_edge("beta", "classes_prob")
# pgm.add_edge("b", "apple_prob")
pgm.add_edge("m", "apple_prob")
pgm.add_edge("s", "apple_prob")
pgm.add_edge("b", "apple_prob")
pgm.add_edge("clusters", "apple_prob")
pgm.add_edge("clusters", "apples")
pgm.add_edge("clusters", "classes_prob")
# And a plate.
pgm.add_plate([1.5, 0.1, 2, 3.3], label=r"tree $i$", shift=-0.1)
pgm.add_plate([0.1, 0.5, 3.3, 1], label=r"quality class $j$", shift=-0.1)

# Render and save.
pgm.render(dpi=300)
plt.savefig("pgm.png", dpi=500)


plt.show()
