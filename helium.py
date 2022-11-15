import hartree_fock as hf
import matplotlib.pyplot as plt

orbitals = [(1, 0, 0)]

Z = 2
name = 'He'
hf.create_atom(Z, 0)
hf.add_orbitals(orbitals)
hf.set_grid(r0=2.7e-4, h=0.022)
etot, r, res = hf.hartree_fock(damp=0.6)

print (f'Finished calculation for Z = {Z} ({name})')
print (f'Hartree-Fock energy: {etot}')

orbital = '1s'
res_1s = res[name]
energy_1s = res_1s['energy']
P_1s = res_1s['p']

fig, ax = plt.subplots()
label = f'{name}, E = {energy_1s:.4f}'
# ax.plot(r[1:], P_1s[1:] / r[1:])
ax.plot(r, P_1s, label=label)
ax.set_xlim(0, 6)
plt.legend()
plt.show()