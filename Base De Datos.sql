--borrar datos
   
DELETE FROM Cita_Medica;
DELETE FROM Disponibilidad;
DELETE FROM estado_cita ;
DELETE FROM Bloque_horario;
DELETE FROM Medico;
DELETE FROM Paciente;
DELETE FROM Sucursal;
DELETE FROM Especialidad;


CREATE TABLE Especialidad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Sucursal (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    telefono INT NOT NULL
);

CREATE TABLE Paciente (
    rut INT PRIMARY KEY,
    nombre VARCHAR(300) NOT NULL,
    apellido VARCHAR(300) NOT NULL,
    usuario VARCHAR(300) NOT NULL,
    email VARCHAR(300) NOT NULL,
    contraseña VARCHAR(300) NOT NULL,
    direccion VARCHAR(300) NOT NULL,
    telefono INT NOT NULL
);

CREATE TABLE Medico (
    rut INT PRIMARY KEY,
    sucursal_id INT,
    especialidad_id INT,
    nombre VARCHAR(300) NOT NULL,
    apellido VARCHAR(300) NOT NULL,
    usuario VARCHAR(300) NOT NULL,
    email VARCHAR(300) NOT NULL,
    contraseña VARCHAR(300) NOT NULL,
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal (id) ON DELETE CASCADE,
    FOREIGN KEY (especialidad_id) REFERENCES Especialidad (id) ON DELETE CASCADE
);

CREATE TABLE Bloque_horario (
    id SERIAL PRIMARY KEY,
    hora_ini TIME NOT NULL,
    hora_fin TIME NOT NULL
);

CREATE TABLE Disponibilidad (
    id SERIAL PRIMARY KEY,
    id_bloque INT NOT NULL,
    rut_medico INT NOT NULL,
    fecha DATE NOT NULL,
    estado BOOLEAN NOT NULL,
    FOREIGN KEY (id_bloque) REFERENCES Bloque_horario (id) ON DELETE CASCADE,
    FOREIGN KEY (rut_medico) REFERENCES Medico (rut) ON DELETE CASCADE
);


CREATE TABLE Estado_Cita (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL
);

CREATE TABLE Cita_Medica (
    id SERIAL PRIMARY KEY,
    rut_medico INT NOT NULL,
    rut_paciente INT NOT NULL,
    cita INT NOT NULL,
    id_estado INT NOT NULL,
    FOREIGN KEY (rut_medico) REFERENCES Medico (rut) ON DELETE CASCADE,
    FOREIGN KEY (rut_paciente) REFERENCES Paciente (rut) ON DELETE CASCADE,
    FOREIGN KEY (cita) REFERENCES Disponibilidad (id) ON DELETE CASCADE,
    FOREIGN KEY (id_estado) REFERENCES Estado_Cita (id) ON DELETE CASCADE
);


--insertar datos base

INSERT INTO Especialidad (nombre)
VALUES
    ('Odontologia'),
    ('Cardiología'),
    ('Anestesiología');

INSERT INTO Sucursal (nombre, direccion, telefono)
VALUES
    ('San Maria', 'San Pedro', 123456789),
    ('Salvacion', 'Antofagasta', 987654321),
    ('Ultimo Respiro', 'Santiago', 555555555);



INSERT INTO Bloque_horario (hora_ini, hora_fin)
VALUES
    ('08:00:00', '09:00:00'),
	('09:00:00', '10:00:00'),
	('10:00:00', '11:00:00'),
	('11:00:00', '12:00:00'),
	('12:00:00', '13:00:00'),
	('13:00:00', '14:00:00'),
	('14:00:00', '15:00:00'),
	('15:00:00', '16:00:00'),
	('16:00:00', '17:00:00'),
	('17:00:00', '18:00:00');

INSERT INTO Estado_Cita (nombre)
VALUES 
('Programada'),
('Confirmada'),
('Anulada'),
('Completada');



   


