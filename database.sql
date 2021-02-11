CREATE DATABASE IF NOT EXISTS gabrielh_abm;
use gabrielh_abm;

CREATE TABLE usuarios(
    id           int(25) auto_increment not null PRIMARY KEY,
    nombre       varchar(40),
    apellido     varchar(50),
    email        varchar(150) not null UNIQUE,
    password     varchar(255) not null,
    fecha        date not null
)