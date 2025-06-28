-- Crea la base de datos
CREATE DATABASE IF NOT EXISTS mariscos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Crea el usuario (ajusta la contraseña a algo seguro)
CREATE USER IF NOT EXISTS 'mariscos_user'@'%' IDENTIFIED BY 'TuPasswordSegura123';

-- Da permisos al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON mariscos_db.* TO 'mariscos_user'@'%';

-- Aplica los cambios
FLUSH PRIVILEGES;