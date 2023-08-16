-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-08-2023 a las 08:57:19
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sayaconsulting3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `client`
--

CREATE TABLE `client` (
  `id_cliente` int(10) NOT NULL,
  `Nombre_cliente` varchar(200) NOT NULL,
  `Descripcion` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `client`
--

INSERT INTO `client` (`id_cliente`, `Nombre_cliente`, `Descripcion`) VALUES
(1, 'IDS Solutions', 'IDS Comercial'),
(2, 'GNP Seguros', 'Aseguradora Mexicanas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contact`
--

CREATE TABLE `contact` (
  `Nombre` varchar(100) NOT NULL,
  `Correo` varchar(55) NOT NULL,
  `Asunto` varchar(200) NOT NULL,
  `Mensaje` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `contact`
--

INSERT INTO `contact` (`Nombre`, `Correo`, `Asunto`, `Mensaje`) VALUES
('asd', 'asd', 'asd', 'asd'),
('ASD', 'ASDA', 'SDASD', 'ASD'),
('asda', 'javi@gmail.com', 'asdas', 'dasd'),
('asdas', 'asd@asd.com', 'asd', 'asd'),
('asdas', 'asd@asd.com', 'asd', 'asdasdad'),
('sdf', 'sdf@asd.com', 'asd', 'asd'),
('asd', 'asd@gmai.com', 'asdas', 'dasd'),
('asd', 'asd@gmail.lcom', 'asd', 'asd'),
('asd', 'asd@gmail.lcom', 'asd', 'asd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asd@asd.com', 'asf', 'asdasd'),
('asd', 'asdas@gmial.com', 'asda', 'sda'),
('asd', 'asdas@gmial.com', 'asda', 'sda'),
('asdasd', 'asd@asdas.com', 'asdasd', 'asda'),
('SFSDF', 'JBKJ@gmail.com', 'dsfsa', 'asfsffasfs');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyect`
--

CREATE TABLE `proyect` (
  `id_proyecto` int(20) NOT NULL,
  `Nombre_proyecto` varchar(100) NOT NULL,
  `Descripcion_proyecto` varchar(100) NOT NULL,
  `Fecha_inicio` date NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `id_team` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyect`
--

INSERT INTO `proyect` (`id_proyecto`, `Nombre_proyecto`, `Descripcion_proyecto`, `Fecha_inicio`, `id_cliente`, `id_team`) VALUES
(5, 'APP BANCOPPEL', 'Aplicacion banca movil', '2023-07-06', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `team`
--

CREATE TABLE `team` (
  `id_team` int(5) NOT NULL,
  `Nombre` varchar(35) NOT NULL,
  `Descripcion` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `team`
--

INSERT INTO `team` (`id_team`, `Nombre`, `Descripcion`) VALUES
(1, 'Warriors', 'Equipo Warriors'),
(2, 'Golden ', 'Equipo Goldens');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` char(102) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Ape_pat` varchar(35) NOT NULL,
  `Ape_mat` varchar(35) NOT NULL,
  `Edad` int(10) NOT NULL,
  `GdoEstudios` varchar(50) NOT NULL,
  `Direccion` varchar(35) NOT NULL,
  `Estado` varchar(35) NOT NULL,
  `Municipio` varchar(35) NOT NULL,
  `Telefono` int(15) NOT NULL,
  `id_team` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `Nombre`, `Ape_pat`, `Ape_mat`, `Edad`, `GdoEstudios`, `Direccion`, `Estado`, `Municipio`, `Telefono`, `id_team`) VALUES
(1, 'ADRIAN', 'pbkdf2:sha256:50000$PLLuA5PF$30a9ef9efd6b6f799e6071b1013ca9fe53e31bcbb60359e9cab6c3c2fe82aa55', 'Adrian', 'Salamanca', 'Dolores', 18, 'Universidad', 'Av Pino Suarez', 'Tlaxcala', 'Huamantla', 24710023, 2),
(2, 'CHUCHO', 'pbkdf2:sha256:600000$YSQl0cnRH8uJf661$cb0479b41d1c0f349f18041fee4846ff2a407e1d4efe5c0cc0c1f72929e16818', 'Jesuss', 'Trinidad', 'Ramirez', 18, 'Prepa', 'Independencia', 'Tlaxcala', 'Huamantla', 2147483647, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Indices de la tabla `proyect`
--
ALTER TABLE `proyect`
  ADD PRIMARY KEY (`id_proyecto`),
  ADD KEY `id_cliente` (`id_cliente`),
  ADD KEY `id_team` (`id_team`);

--
-- Indices de la tabla `team`
--
ALTER TABLE `team`
  ADD PRIMARY KEY (`id_team`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_team` (`id_team`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `client`
--
ALTER TABLE `client`
  MODIFY `id_cliente` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `proyect`
--
ALTER TABLE `proyect`
  MODIFY `id_proyecto` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `team`
--
ALTER TABLE `team`
  MODIFY `id_team` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `proyect`
--
ALTER TABLE `proyect`
  ADD CONSTRAINT `proyect_ibfk_1` FOREIGN KEY (`id_team`) REFERENCES `team` (`id_team`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `proyect_ibfk_2` FOREIGN KEY (`id_cliente`) REFERENCES `client` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id_team`) REFERENCES `team` (`id_team`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
