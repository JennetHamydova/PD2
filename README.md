## Szybki start 

```bash
# 1) klon repo
git clone https://github.com/JennetHamydova/PD2.git
cd PD2

# 2) środowisko
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

# 3) instalacja zależności
pip install -r requirements.txt

# 4) uruchomienie serwera
python app.py
