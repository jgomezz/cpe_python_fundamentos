-- Crear la base de datos HR
-- CREATE DATABASE HR;

-- Borrar base de datos HR
-- DROP DATABASE HR;

-- Seleccionar la base de datos HR
USE HR;

-- Crea la tabla EMPLEADOS
CREATE TABLE EMPLEADOS (
	NRO_EMP int(11) NOT NULL AUTO_INCREMENT,
	NOMBRE varchar(50) NOT NULL,
	APELLIDO varchar(50) NOT NULL,
	SEXO enum('H','M') NOT NULL,
	FECHA_NACIMIENTO date ,
	FECHA_CONTRATO date ,
	PRIMARY KEY (NRO_EMP)
);

