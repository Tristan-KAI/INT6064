# Logistic Map — one equation, from stable to chaos
# Real STEM question: how many fish can we harvest sustainably?
import matplotlib.pyplot as plt

r = 2.8        # growth rate: try 2.8 / 3.2 / 3.5 / 3.9
P = [0.1]      # initial population fraction (0~1)
for _ in range(60):
    P.append(r * P[-1] * (1 - P[-1]))

plt.plot(P, '.-', color='#2563eb')
plt.xlabel('Generation')
plt.ylabel('P (population fraction)')
plt.title(f'Logistic Map  r = {r}')
plt.ylim(0, 1)
plt.show()

# Bifurcation diagram: stable -> period-doubling -> chaos
rs, Ps = [], []
for r in [i / 1000 for i in range(2500, 4001)]:
    p = 0.5
    for _ in range(300):
        p = r * p * (1 - p)
    for _ in range(100):
        p = r * p * (1 - p)
        rs.append(r)
        Ps.append(p)

plt.figure(figsize=(9, 6))
plt.scatter(rs, Ps, s=0.15, c='#2563eb')
plt.xlabel('r (growth rate)')
plt.ylabel('P (long-term)')
plt.title('Bifurcation: stable -> period-doubling -> chaos')
plt.show()

print('Try changing r to 3.2 / 3.5 / 3.9 and re-run.')
