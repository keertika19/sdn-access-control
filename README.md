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

* Topology running
* Allowed ping
* Blocked ping
* Controller logs

---

## ✅ Conclusion

The SDN controller successfully enforces access control policies using match–action rules.

