# 🔍 Systemövervakningsapplikation i Python

En konsolbaserad applikation för systemövervakning byggd i **Python**.
Programmet gör det enkelt att övervaka **CPU-användning**, **minnesanvändning** och **diskanvändning**, samt att konfigurera och hantera larm baserat på valda gränsvärden.

---

## ✨ Funktioner

- **Övervaka systemresurser** i realtid:

  - CPU-användning i %
  - Minnesanvändning i % och GB
  - Diskanvändning i % och GB

- **Skapa larm** för CPU, minne och disk med valfria tröskelvärden (1–100 %).
- **Visa alla aktiva larm**, sorterade per typ.
- **Ta bort larm** via menyval.
- **Spara larm till disk** i JSON – laddas automatiskt vid nästa programstart.
- **Loggning av händelser** till fil med tidsstämplar.
- **Robust input-hantering** – applikationen kraschar inte vid felaktiga inmatningar.

Exempel på larmutskrift i övervakningsläge:

```
*** VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER 80% ***
```

---

## 🛠 Installation

1. Klona repot:

   ```bash
   git clone https://github.com/<ditt-användarnamn>/<repo-namn>.git
   cd <repo-namn>
   ```

2. Skapa virtuell miljö och installera beroenden:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows

   pip install -r requirements.txt
   ```

---

## ▶️ Användning

Starta programmet med:

```bash
python main.py
```

Du får upp en meny med fem alternativ:

1. **Starta övervakning**
2. **Lista aktiv övervakning**
3. **Skapa larm**
4. **Visa larm**
5. **Starta övervakningsläge**

Navigera genom menyn med siffror. Felaktiga inmatningar hanteras med tydliga felmeddelanden.

---

## 📂 Struktur

Projektet är uppdelat i flera moduler för bättre läsbarhet och underhåll:

```
├── main.py           # Startpunkt för applikationen
├── monitoring.py     # Funktioner för att samla systemdata
├── alarms.py         # Hantering av larm (skapa, ta bort, visa)
├── logger.py         # Loggning av händelser
├── storage.py        # Lagra och läsa larm från JSON
├── utils.py          # Hjälpfunktioner (t.ex. inputvalidering)
└── requirements.txt  # Beroenden
```

---

## 📦 Beroenden

- [psutil](https://pypi.org/project/psutil/) – systeminformation (CPU, minne, disk)
- [json](https://docs.python.org/3/library/json.html) – lagring av larm
- [logging](https://docs.python.org/3/library/logging.html) – loggning av händelser

Installera alla beroenden:

```bash
pip install -r requirements.txt
```

---

## 📑 Exempel

Visa aktiv övervakning:

```
CPU Användning: 35%
Minnesanvändning: 65% (4.2 GB out of 8 GB used)
Diskanvändning: 80% (400 GB out of 500 GB used)
```

Visa larm:

```
CPU larm 70%
Disklarm 95%
Minneslarm 80%
```

---

## 🚀 Framtida förbättringar

- Skicka e-post vid aktiverade larm (SendGrid).
- Grafiskt gränssnitt (GUI) för att visa resurser och larm i realtid.
- Webbaserad dashboard.

---

## 📜 Licens

MIT License – se [LICENSE](LICENSE) för mer information.
