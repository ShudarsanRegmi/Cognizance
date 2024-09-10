# Installation Guide

### Create a virtual environment and activate it
```bash
python -m venv .venv
.\Scripts\activate #for windows
source ./.venv/bin/activate # for linux
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### dump the database
```bash
mysql -u [username] -p [database_name] < database.sql
```

### Change the database configuration in main.py
```py
self.db = Database(host='localhost', user='', password='', database='flight_management')
```

### Run main.py

```bash
python main.py
```

---

## Images
![image](https://github.com/user-attachments/assets/92837e55-6a32-48f5-bbd7-b5a7ac0f8dbb)

![image](https://github.com/user-attachments/assets/07aea73e-597d-4155-a0d1-210466520bdd)

![image](https://github.com/user-attachments/assets/e3d3d1fe-4c65-40bb-9dba-8a67057c9148)

![image](https://github.com/user-attachments/assets/009777d4-36df-42d3-9058-f5b193c429a6)

![image](https://github.com/user-attachments/assets/945e3f7b-5868-4d48-87eb-31007225ef2c)

![image](https://github.com/user-attachments/assets/4c5d142f-1273-402d-8cb4-f49f136977e6)


