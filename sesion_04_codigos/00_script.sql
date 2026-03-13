-- Crear la base de datos HR
-- CREATE DATABASE HR;

-- Borrar base de datos HR
-- DROP DATABASE HR;

-- Seleccionar la base de datos HR
-- USE HR;

-- Crea la tabla EMPLEADOS
/*
CREATE TABLE EMPLEADOS (
	NRO_EMP int(11) NOT NULL AUTO_INCREMENT,
	NOMBRE varchar(50) NOT NULL,
	APELLIDO varchar(50) NOT NULL,
	SEXO enum('H','M') NOT NULL,
	FECHA_NACIMIENTO date ,
	FECHA_CONTRATO date ,
	PRIMARY KEY (NRO_EMP)
);
*/

-- Eliminar tabla
/*
USE HR;
DROP TABLE EMPLEADOS;
*/

-- Insertar registros en la tabla EMPLEADOS
/*
INSERT INTO EMPLEADOS (NOMBRE, APELLIDO, SEXO, FECHA_NACIMIENTO, FECHA_CONTRATO) VALUES
('Carlos', 'Ramirez', 'H', '1990-05-12', '2020-03-15'),
('Ana', 'Torres', 'M', '1992-08-21', '2021-06-10'),
('Luis', 'Gomez', 'H', '1988-11-03', '2019-09-01'),
('Maria', 'Lopez', 'M', '1995-02-14', '2022-01-20'),
('Jorge', 'Castro', 'H', '1987-07-30', '2018-05-12'),
('Elena', 'Vargas', 'M', '1993-09-18', '2021-11-08'),
('Pedro', 'Sanchez', 'H', '1991-04-09', '2020-07-22'),
('Lucia', 'Fernandez', 'M', '1996-12-01', '2023-02-15'),
('Miguel', 'Rojas', 'H', '1989-03-27', '2019-10-10'),
('Sofia', 'Herrera', 'M', '1994-06-05', '2022-08-30');
*/

-- Realizar consultas a las tablas

-- SELECT * FROM EMPLEADOS;

/*
SELECT * FROM EMPLEADOS
WHERE NOMBRE = 'Ana';
*/

/*
SELECT * FROM EMPLEADOS
WHERE UPPER(NOMBRE) = 'ANA';
*/

/*
-- Listado de empleados que tenga la letra u en su nombre
SELECT * FROM EMPLEADOS
WHERE UPPER(NOMBRE) LIKE '%u%';
*/

/*
-- Deseo los empleados que son mujeres y tienen en su apellido la letra o
SELECT * FROM EMPLEADOS
WHERE UPPER(APELLIDO) LIKE '%o%' AND SEXO = 'M';
*/

/*
-- Cuantos empledos son mujeres?
SELECT COUNT(*) FROM EMPLEADOS
WHERE SEXO = 'M';
*/

/*
SELECT NRO_EMP, APELLIDO, FECHA_CONTRATO 
FROM EMPLEADOS
WHERE SEXO = 'M';
*/


-- Ejercicio : Obtener los nombres de los varones que tengan la vocal a en su nombre
/*
SELECT * FROM empleados
WHERE UPPER(NOMBRE) LIKE '%a%' AND SEXO = 'H';
*/

-- Actualizar : UPDATE
/*
UPDATE EMPLEADOS 
SET APELLIDO = 'Ramirez', NOMBRE='Carlos'
WHERE NRO_EMP = 1;


SELECT *
FROM EMPLEADOS;
*/


-- Ejercicio : CAmbiar a mayuscula el apellido del empleado Elena
-- Ejericio :  Cambiar a minuscula el nombre de Sofia

/*
INSERT INTO EMPLEADOS (NOMBRE, APELLIDO, SEXO, FECHA_NACIMIENTO, FECHA_CONTRATO) VALUES
('Juan', 'Medrano', 'H', '1993-07-18', '2019-12-20'),
('Silvia', 'Gutierres', 'M', '1990-08-21', '2022-07-10');
*/

-- Borrar registros
DELETE FROM EMPLEADOS  
WHERE NRO_EMP = 12;

SELECT *
FROM EMPLEADOS;


-- INsertar un registro y eliminarlo de la base de datos
INSERT INTO empleados (NOMBRE,APELLIDO,SEXO,FECHA_NACIMIENTO,FECHA_CONTRATO) VALUES
('Milagros','Chunga','M','2006-06-26','2023-02-05');

SELECT *
FROM empleados;

-- Borrar registro--
DELETE FROM empleados
WHERE NRO_EMP=11;
SELECT *
FROM empleados;


INSERT INTO EMPLEADOS (NOMBRE, APELLIDO, SEXO, FECHA_NACIMIENTO, FECHA_CONTRATO) 
VALUES ('Carlos', 'Perez', 'M', '1985-05-12', '2023-01-15');

DELETE FROM EMPLEADOS 
WHERE NOMBRE = 'Carlos' AND APELLIDO = 'Perez';


INSERT INTO EMPLEADOS (NOMBRE, APELLIDO, SEXO, FECHA_NACIMIENTO, FECHA_CONTRATO) VALUES
('JOSE', 'CHAVEZ', 'H', '1993-07-18', '2019-12-20');
SELECT *
FROM EMPLEADOS;

DELETE FROM EMPLEADOS  
WHERE NRO_EMP = 25;


