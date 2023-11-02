DROP DATABASE IF EXISTS dbDecidete2023;
CREATE DATABASE dbDecidete2023;
USE dbDecidete2023;

-- carrusel de aplicaciones
CREATE TABLE aplicaciones(
id_app int primary key auto_increment,
nombre varchar (15),
autor varchar (25),
tipo varchar (10),
ruta text,
imagen text,
comando_ejecucion text
);



DELIMITER //
CREATE TRIGGER aplicaciones_insert_trigger AFTER INSERT ON aplicaciones
FOR EACH ROW
BEGIN
  INSERT INTO ChangeInserts (fecha_insert, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), NEW.autor, 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'aplicaciones');
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER aplicaciones_update_trigger AFTER UPDATE ON aplicaciones
FOR EACH ROW
BEGIN
  INSERT INTO ChangeUpdate (fecha_update, old_data, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), CONCAT_WS(', ', OLD.nombre, OLD.autor, OLD.tipo, OLD.ruta, OLD.imagen, OLD.comando_ejecucion), 'USUARIO_ACTUALIZADOR', 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'aplicaciones');
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER aplicaciones_delete_trigger BEFORE DELETE ON aplicaciones
FOR EACH ROW
BEGIN
  INSERT INTO ChangeDeletes (fecha_delete, data_Deleted, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), CONCAT_WS(', ', OLD.nombre, OLD.autor, OLD.tipo, OLD.ruta, OLD.imagen, OLD.comando_ejecucion), 'USUARIO_ELIMINADOR', 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'aplicaciones');
END;
//
DELIMITER ;

-- registro biometricos
CREATE TABLE jugadores(
id_Datos_Cara int PRIMARY KEY AUTO_INCREMENT,
jugador CHAR(3),
embedding BLOB,
fechaRegistro datetime,
user_registro TEXT,
tipo_juego int
);

DELIMITER //
CREATE TRIGGER biometCara_insert_trigger AFTER INSERT ON biometCara
FOR EACH ROW
BEGIN
  INSERT INTO ChangeInserts (fecha_insert, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), NEW.user_registro, 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'biometCara');
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER biometCara_update_trigger AFTER UPDATE ON biometCara
FOR EACH ROW
BEGIN
  INSERT INTO ChangeUpdate (fecha_update, old_data, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), CONCAT_WS(', ', OLD.jugador, OLD.fechaRegistro, OLD.user_registro), 'USUARIO_ACTUALIZADOR', 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'biometCara');
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER biometCara_delete_trigger BEFORE DELETE ON biometCara
FOR EACH ROW
BEGIN
  INSERT INTO ChangeDeletes (fecha_delete, data_Deleted, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), CONCAT_WS(', ', OLD.jugador, OLD.fechaRegistro, OLD.user_registro), 'USUARIO_ELIMINADOR', 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'biometCara');
END;
//
DELIMITER ;

-- procedimiento almacenado para registrar (ulises)



CREATE TABLE biometMano(
id_Datos_Mano int PRIMARY KEY AUTO_INCREMENT,
jugador CHAR(3),
embedding BLOB,
fecharegistro datetime,
user_registro TEXT
);

DELIMITER //
CREATE TRIGGER biometMano_insert_trigger AFTER INSERT ON biometMano
FOR EACH ROW
BEGIN
  INSERT INTO ChangeInserts (fecha_insert, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), NEW.user_registro, 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'biometMano');
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER biometMano_update_trigger AFTER UPDATE ON biometMano
FOR EACH ROW
BEGIN
  INSERT INTO ChangeUpdate (fecha_update, old_data, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), CONCAT_WS(', ', OLD.jugador, OLD.fecharegistro, OLD.user_registro), 'USUARIO_ACTUALIZADOR', 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'biometMano');
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER biometMano_delete_trigger BEFORE DELETE ON biometMano
FOR EACH ROW
BEGIN
  INSERT INTO ChangeDeletes (fecha_delete, data_Deleted, user_responsible, ip_Log, host_Log, tabla_afectada)
  VALUES (NOW(), CONCAT_WS(', ', OLD.jugador, OLD.fecharegistro, OLD.user_registro), 'USUARIO_ELIMINADOR', 'IP_DEL_USUARIO', 'HOST_DEL_USUARIO', 'biometMano');
END;
//
DELIMITER ;

CREATE TABLE ChangeLogs (
ID_Log int PRIMARY KEY AUTO_INCREMENT,
fecha_Log datetime,
user_Log TEXT,
ip_Log VARCHAR(45),
host_Log VARCHAR(255),
tipo_cambio VARCHAR(10),
tabla_afectada VARCHAR(255)
);



CREATE TABLE ChangeDeletes(
ID_Delete int PRIMARY KEY AUTO_INCREMENT,
fecha_delete datetime,
data_Deleted TEXT,
user_responsible TEXT,
ip_Log varchar(45),
host_Log VARCHAR(255),
tabla_afectada VARCHAR(255)
);



CREATE TABLE ChangeInserts(
ID_Insert int PRIMARY KEY AUTO_INCREMENT,
fecha_insert datetime,
user_responsible TEXT,
ip_Log varchar(45),
host_Log VARCHAR(255),
tabla_afectada VARCHAR(255)
);



CREATE TABLE ChangeUpdate(
ID_update int PRIMARY KEY AUTO_INCREMENT,
fecha_update datetime,
old_data TEXT,
user_responsible TEXT,
ip_Log varchar(45),
host_Log VARCHAR(255),
tabla_afectada VARCHAR(255)
);


