# SDN-Based Access Control System (POX + Mininet)

## 📌 Problem Statement

This project implements an SDN-based access control system that allows only authorized hosts to communicate within a network while blocking unauthorized hosts.

## 🧠 Objective

* Implement controller–switch interaction
* Design flow rules using match–action
* Control network behavior dynamically

## 🏗️ Network Topology

* Controller: POX
* Switch: s1
* Hosts: h1, h2, h3

## ▶️ Execution Steps

### Terminal 1 (Controller)

```bash
cd ~/pox
./pox.py access_control
```

### Terminal 2 (Mininet)

```bash
sudo mn --topo single,3 --controller remote
```

---

## 🧪 Test Cases

### ✅ Allowed Traffic

```bash
h1 ping h2
```

✔ Successful communication

### ❌ Blocked Traffic

```bash
h3 ping h1
```

❌ Destination unreachable

---

## 📸 Proof of Execution

(Add screenshots here)

* Setup
* <img width="604" height="441" alt="Screenshot 2026-04-19 194928" src="https://github.com/user-attachments/assets/273ab22c-9348-41d1-985e-207c5cf111d2" />

* Allowed ping

* <img width="576" height="447" alt="Screenshot 2026-04-19 194955" src="https://github.com/user-attachments/assets/afba1b6d-edbd-442c-b243-821c64a5d1bc" />

* Blocked ping
* <img width="591" height="152" alt="Screenshot 2026-04-19 195022" src="https://github.com/user-attachments/assets/106a2b67-819a-49c6-afb9-f1560b5e713f" />

* Controller logs

* <img width="527" height="370" alt="Screenshot 2026-04-19 195059" src="https://github.com/user-attachments/assets/f3ed7fd9-30e0-474c-8f94-827f4072305e" />

<img width="425" height="273" alt="Screenshot 2026-04-19 195110" src="https://github.com/user-attachments/assets/ae1e2693-7740-4f62-86bc-9eee6db338cb" />



---

## ✅ Conclusion

The SDN controller successfully enforces access control policies using match–action rules.

