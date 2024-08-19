-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-08-2024 a las 19:16:56
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rancho`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividades`
--

CREATE TABLE `actividades` (
  `id_actividad` int(11) NOT NULL,
  `tipo` text NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `fecha_elab` date NOT NULL,
  `responsable` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `actividades`
--

INSERT INTO `actividades` (`id_actividad`, `tipo`, `descripcion`, `fecha_elab`, `responsable`) VALUES
(1, 'limpieza de caca', 'se limpio el area de los perros', '2024-07-23', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id_empleado` int(11) NOT NULL,
  `nombre` text NOT NULL,
  `apellido_p` text NOT NULL,
  `apellido_m` text NOT NULL,
  `curp` varchar(20) NOT NULL,
  `fecha_nac` date NOT NULL,
  `rol` varchar(60) NOT NULL,
  `salario` float NOT NULL,
  `estatus` varchar(1) NOT NULL,
  `ranchoID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id_empleado`, `nombre`, `apellido_p`, `apellido_m`, `curp`, `fecha_nac`, `rol`, `salario`, `estatus`, `ranchoID`) VALUES
(1, 'Matias', 'Rosales', 'Perez', 'IJKE2023432JHSDEF03', '2000-02-14', 'vaquero', 2000.2, '1', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ganado`
--

CREATE TABLE `ganado` (
  `id_ganado` int(11) NOT NULL,
  `especie` varchar(60) NOT NULL,
  `raza` varchar(60) NOT NULL,
  `sexo` text NOT NULL,
  `edad` date NOT NULL,
  `peso` float NOT NULL,
  `salud` text NOT NULL,
  `destino` varchar(50) NOT NULL,
  `ubicacion` int(11) NOT NULL,
  `estatus` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ganado`
--

INSERT INTO `ganado` (`id_ganado`, `especie`, `raza`, `sexo`, `edad`, `peso`, `salud`, `destino`, `ubicacion`, `estatus`) VALUES
(1, 'Bovino', 'jersey', 'MACHO', '2020-10-02', 200.987, 'saludable', 'semental', 1, '0');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instalaciones`
--

CREATE TABLE `instalaciones` (
  `id_instalacion` int(11) NOT NULL,
  `tipo` varchar(255) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `extencion` float NOT NULL,
  `ubicacion` varchar(255) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `fecha_revision` date NOT NULL,
  `estatus` varchar(1) NOT NULL,
  `rancho_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `instalaciones`
--

INSERT INTO `instalaciones` (`id_instalacion`, `tipo`, `fecha_creacion`, `extencion`, `ubicacion`, `estado`, `fecha_revision`, `estatus`, `rancho_id`) VALUES
(1, 'ESTABLO', '2024-05-09', 99, 'cerca de la puerta norte', 'buenas condiciones', '2024-08-01', '1', 1),
(3, 'Establo', '2024-08-14', 100, 'cerca del rio sur', 'buenas condiciones', '2024-08-14', '0', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `id_producto` int(11) NOT NULL,
  `tipo` varchar(100) NOT NULL COMMENT 'herramienta,alimento, suministros, etc',
  `nombre` varchar(255) NOT NULL,
  `cantidad` float NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `responsable` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rancho`
--

CREATE TABLE `rancho` (
  `id_rancho` int(11) NOT NULL,
  `nombre_rancho` varchar(255) NOT NULL,
  `propietario` text NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `extencion` decimal(12,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rancho`
--

INSERT INTO `rancho` (`id_rancho`, `nombre_rancho`, `propietario`, `direccion`, `extencion`) VALUES
(1, 'Los Dos Garcia', 'Matias Rosales', 'Gabino Santillan calle 15 de mayo #103', 900000.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reg_vacunas`
--

CREATE TABLE `reg_vacunas` (
  `num_registro` int(11) NOT NULL,
  `animal` int(11) NOT NULL,
  `responsable` varchar(255) NOT NULL,
  `observacion` varchar(255) NOT NULL,
  `fecha_admin` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reg_vacunas`
--

INSERT INTO `reg_vacunas` (`num_registro`, `animal`, `responsable`, `observacion`, `fecha_admin`) VALUES
(1, 1, 'matias', 'ninuna', '0000-00-00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_uduario` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_uduario`, `nombre`, `apellidos`, `email`, `password`) VALUES
(1, 'manuel', 'rosales', 'manuel@hotmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(2, 'Greogorio', 'Rivas', 'gregorio@gmail.com', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividades`
--
ALTER TABLE `actividades`
  ADD PRIMARY KEY (`id_actividad`),
  ADD KEY `fkempleado` (`responsable`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id_empleado`),
  ADD UNIQUE KEY `curp` (`curp`),
  ADD KEY `id_rancho` (`ranchoID`);

--
-- Indices de la tabla `ganado`
--
ALTER TABLE `ganado`
  ADD PRIMARY KEY (`id_ganado`),
  ADD KEY `id_instalacion` (`ubicacion`);

--
-- Indices de la tabla `instalaciones`
--
ALTER TABLE `instalaciones`
  ADD PRIMARY KEY (`id_instalacion`),
  ADD KEY `rancho` (`rancho_id`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `fkempleado` (`responsable`);

--
-- Indices de la tabla `rancho`
--
ALTER TABLE `rancho`
  ADD PRIMARY KEY (`id_rancho`);

--
-- Indices de la tabla `reg_vacunas`
--
ALTER TABLE `reg_vacunas`
  ADD PRIMARY KEY (`num_registro`),
  ADD KEY `fk1animal` (`animal`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_uduario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `actividades`
--
ALTER TABLE `actividades`
  MODIFY `id_actividad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `instalaciones`
--
ALTER TABLE `instalaciones`
  MODIFY `id_instalacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rancho`
--
ALTER TABLE `rancho`
  MODIFY `id_rancho` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `reg_vacunas`
--
ALTER TABLE `reg_vacunas`
  MODIFY `num_registro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_uduario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `actividades`
--
ALTER TABLE `actividades`
  ADD CONSTRAINT `actividades_ibfk_1` FOREIGN KEY (`responsable`) REFERENCES `empleado` (`id_empleado`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`ranchoID`) REFERENCES `rancho` (`id_rancho`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `ganado`
--
ALTER TABLE `ganado`
  ADD CONSTRAINT `ganado_ibfk_1` FOREIGN KEY (`ubicacion`) REFERENCES `instalaciones` (`id_instalacion`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `instalaciones`
--
ALTER TABLE `instalaciones`
  ADD CONSTRAINT `instalaciones_ibfk_1` FOREIGN KEY (`rancho_id`) REFERENCES `rancho` (`id_rancho`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`responsable`) REFERENCES `empleado` (`id_empleado`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `reg_vacunas`
--
ALTER TABLE `reg_vacunas`
  ADD CONSTRAINT `reg_vacunas_ibfk_1` FOREIGN KEY (`animal`) REFERENCES `ganado` (`id_ganado`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
