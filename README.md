# Sistema POS para Restaurante de Mariscos

Este sistema fue desarrollado con **FastAPI**, **MariaDB** y un frontend HTML para gestionar pedidos en un restaurante de mariscos.

---

## Requisitos

- Python 3.10 o superior
- MariaDB (o MySQL compatible)
- FastAPI
- Uvicorn
- SQLAlchemy
- PyMySQL
- Passlib
- python-jose

---

## Instalación de dependencias

### 1. Clona el repositorio

```bash
git clone https://github.com/YolotlTellez29/pos-mariscos.git
cd pos-mariscos
```

---

### 2. Crea y activa un entorno virtual

#### **En Linux/MacOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### **En Windowserge branch 'api'
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
**

```cmderge branch 'api'
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.

python -m venv venv
venv\Scripts\activate
```

---

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```
erge branch 'api'
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.

El archivo `requirements.txt` ya contiene todas las dependencias necesarias:

```
fastapi
uvicorn
sqlalchemy
pymysql
python-jose
passlib[bcrypt]
```
erge branch 'api'
# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.

---

### 4. Configura la base de datos MariaDB/MySQL

Debes tener un servidor MariaDB/MySQL corriendo y crear una base de datos para el proyecto.

#### **En Linux/MacOS**

```bash
sudo mysql -u root -p
```

#### **En Windows**

Abre el cliente de MySQL/MariaDB y ejecuta:

```sql
CREATE DATABASE mariscos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'mariscos_user'@'localhost' IDENTIFIED BY 'tu_password_segura';
GRANT ALL PRIVILEGES ON mariscos_db.* TO 'mariscos_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Luego, configura las variables de entorno en tu sistema o edita el archivo `backend/database.py` para que coincidan con tu usuario y contraseña de la base de datos:

```python
MARIADB_USER = os.getenv("MARIADB_USER", "mariscos_user")
MARIADB_PASSWORD = os.getenv("MARIADB_PASSWORD", "tu_password_segura")
MARIADB_HOST = os.getenv("MARIADB_HOST", "localhost")
MARIADB_DB = os.getenv("MARIADB_DB", "mariscos_db")
```

Puedes exportar las variables de entorno antes de correr el backend:

#### **En Linux/MacOS**

```bash
export MARIADB_USER=mariscos_user
export MARIADB_PASSWORD=tu_password_segura
export MARIADB_HOST=localhost
export MARIADB_DB=mariscos_db
```

#### **En Windows (CMD)**

```cmd
set MARIADB_USER=mariscos_user
set MARIADB_PASSWORD=tu_password_segura
set MARIADB_HOST=localhost
set MARIADB_DB=mariscos_db
```

---

### 5. Inicializa la base de datos (crea las tablas)

Desde la raíz del proyecto, ejecuta:

```bash
python -c "from backend.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

---

### 6. Ejecuta el backend

```bash
uvicorn backend.main:app --reload
```

El backend estará disponible en [http://localhost:8000](http://localhost:8000).

---

### 7. Ejecuta el frontend

Abre los archivos HTML del directorio `frontend/` directamente en tu navegador, o usa una extensión de servidor estático en VS Code, o un servidor simple como:

```bash
cd frontend
python3 -m http.server 8080
```

Luego abre [http://localhost:8080/login.html](http://localhost:8080/login.html) en tu navegador.

---

## Notas adicionales

- Si usas Windows y tienes problemas con dependencias, asegúrate de tener instalado [Build Tools for Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/) para compilar paquetes de Python.
- Si tienes problemas con la conexión a la base de datos, revisa que el usuario, contraseña y nombre de la base de datos sean correctos y que el servidor MariaDB/MySQL esté corriendo.
- Si necesitas migrar la base de datos, puedes usar [Alembic](https://alembic.sqlalchemy.org/) para gestionar migraciones.

---

## Estructura del proyecto

```
backend/
  ├── main.py
  ├── database.py
  ├── deps.py
  ├── models/
  ├── schemas/
  ├── crud/
  ├── routes/
  └── utils/
frontend/
  ├── login.html
  ├── mesa.html
  ├── orden.html
  └── ... (archivos CSS)
requirements.txt
README.md
```

---

## Contacto

Para dudas o soporte, contacta a Yolotl Téllez en [su perfil de GitHub](https://github.com/YolotlTellez29).
