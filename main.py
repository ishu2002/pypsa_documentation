import pypsa
import numpy as np

n = pypsa.Network()

for i in range(32):
    n.add("Bus", f"Bus {i+1}", v_nom=110)

n.add("Generator", "Slack Generator", bus="Bus 1", p_set=0, control="Slack", slack=True, vm_pu=1.0)

pv_indices = [i+2 for i in range(8)]
for i in pv_indices:
    n.add("Generator", f"PV Generator {i}", bus=f"Bus {i}", p_set=50, control="PV", vm_pu=1.0)

for i in range(32):
    n.add("Load", f"Load {i+1}", bus=f"Bus {i+1}", p_set=np.random.uniform(10, 30), q_set=np.random.uniform(5, 15))

for i in range(31):
    n.add("Line", f"Line {i+1}", bus0=f"Bus {i+1}", bus1=f"Bus {i+2}", x=0.05, r=0.01, s_nom=100)

n.pf()
print(n.buses_t.v_mag_pu)
