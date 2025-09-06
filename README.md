# 🐟🐻 Predator-Prey Model: Fish vs Bears  

This project simulates the **Predator-Prey relationship** between **fish (prey)** and **bears (predator)** using the **Lotka–Volterra equations**.  

The goal is to demonstrate how predator and prey populations naturally oscillate over time, and to visualize these dynamics using **Python-based modeling and data visualization**.  

---

## 📂 Repository Contents  

- `new_predator_prey.csv` → Refined dataset (Fish & Bear population data)  
- `Predator prey model.csv` → Initial predator-prey dataset  
- `realdata_experimental.py` → Script to process experimental population data  
- `realdata_model_exp.py` → Lotka–Volterra simulation with real data  
- `realdata_phaseplot.py` → Generates **phase plots** (Fish vs Bear population cycles)  
- `test1.py` & `test1_phaseplot.py` → Basic test scripts for validation  

---

## 🚀 Features  

- Models **Fish vs Bear** population dynamics  
- Implements **Lotka–Volterra Predator-Prey equations**  
- Reads real or synthetic data from CSV files  
- Creates **time-series plots** (population vs time)  
- Creates **phase plots** (Fish population vs Bear population)  
- Easy to extend with different datasets  

---

## Background

The Lotka–Volterra equations describe how predator and prey populations change over time.

- 🐟 Fish (Prey): Their population grows when bears are absent, but declines as bears hunt them.

- 🐻 Bears (Predators): Their population depends on the availability of fish. Too few fish leads to a decline in bear numbers.

This creates a natural oscillation cycle where both populations rise and fall periodically.

