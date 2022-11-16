--
-- Base de datos: `proy_colab_bbbbb5`
--
CREATE DATABASE IF NOT EXISTS `proy_colab_bbbbb5` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `proy_colab_bbbbb5`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `biografias`
--

-- DESCOMENTAR LA SIGUIENTE LINEA SÓLO SI SE DESEA BORRAR LA TABLA biografias EXISTENTE, ANTES DE VOLVER A CREARLA
-- DROP TABLE IF EXISTS `biografias`;  

CREATE TABLE IF NOT EXISTS `biografias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `autor` varchar(100) CHARACTER SET latin1 NOT NULL,
  `bio` text CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

-- DESCOMENTAR LA SIGUIENTE LINEA SÓLO SI SE DESEA BORRAR LA TABLA libros EXISTENTE, ANTES DE VOLVER A CREARLA
-- DROP TABLE IF EXISTS `libros`;

CREATE TABLE IF NOT EXISTS `libros` (
  `id` int(15) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `disponibilidad` varchar(30) DEFAULT NULL,
  `precio` double(20,2) DEFAULT NULL,
  `editorial` varchar(100) DEFAULT NULL,
  `isbn` varchar(100) DEFAULT NULL,
  `paginas` varchar(100) DEFAULT NULL,
  `idioma` varchar(100) DEFAULT NULL,
  `formato` varchar(100) DEFAULT NULL,
  `clasificacion` varchar(255) DEFAULT NULL,
  `fechaPub` varchar(50) DEFAULT NULL,
  `sinopsis` text NOT NULL,
  `imagenUrl` varchar(100) DEFAULT NULL,
  `libroUrl` varchar(100) DEFAULT NULL,
  `visible` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `libros` ADD UNIQUE INDEX `isbn` (`isbn`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `variaciondeprecios`
--

-- DESCOMENTAR LA SIGUIENTE LINEA SÓLO SI SE DESEA BORRAR LA TABLA variaciondeprecios EXISTENTE, ANTES DE VOLVER A CREARLA
-- DROP TABLE IF EXISTS `variaciondeprecios`;

CREATE TABLE IF NOT EXISTS `variaciondeprecios` (
  `id` int(15) NOT NULL,
  `isbn` int(100) NOT NULL,
  `precio` float(20,2) NOT NULL,
  `fechaDelRegistro` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
