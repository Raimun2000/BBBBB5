<?php 
include("modulos/conexion.php");
header("Content-Type: text/html;charset=utf-8");
?>
<!DOCTYPE html>
<html lang="es">
<head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Análisis de la información</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <style>
      img {
            width: 75px;
      }
      </style>
</head>
<body>
      <div class="container-fluid p-4">
            <div class="row text-center">
                  <div class="col-6"><a href="informeProyectoBBBBB5.php" class="btn btn-warning text-dark text-center">Informe del proyecto</a></div>
                  <div class="col-6"><a href="precioPromedio.php" class="btn btn-danger text-light text-center">Precio promedio por Editorial</a></div>
            </div>
            <div class="row">
                  <h1 class="text-primary p-4 text-center">Información de la tabla LIBROS</h1>
                  <h4 class="bg-info text-dark p-4 text-center rounded">Creada desde Python, usando BeautifulSoup</h4>
            <table class="table">
                  <thead>
                  <tr>
                        <th scope="col">Id</th>
                        <th scope="col">Tapa</th>
                        <th scope="col">Título</th>
                        <th scope="col">Autor</th>
                        <th scope="col">Disponible</th>
                        <th scope="col">Publicado</th>
                        <th scope="col">Clasificación</th>
                        <th scope="col">Formato</th>
                        <th scope="col">Idioma</th>
                        <th scope="col">Precio</th>
                        <th scope="col">Nº Pág.</th>
                        <th scope="col">ISBN</th>
                        <th scope="col">Editorial</th>
                  </tr>
                  </thead>
                  <tbody>
                  <?php 
                  $obj = new conectar();
			$sql = "SELECT id, titulo, autor, disponibilidad, fechaPub, clasificacion, formato, idioma, precio, paginas, isbn, editorial, imagenUrl FROM libros WHERE visible;";
                  $recup = $obj->ver($obj->conexion(), $sql);
                  while ($mostrar = mysqli_fetch_row($recup)) { ?>
                  <tr>
                        <th scope="row"><?php echo $mostrar[0] ?></th>
                        <td><?php echo "<a href='".$mostrar[12]."' target='_blank'><img src='".$mostrar[12]."' alt='Libro: ".$mostrar[1]." de ".$mostrar[2]."' title='Libro: ".$mostrar[1]." de ".$mostrar[2]."'></a>"; ?></td>
                        <td><?php echo $mostrar[1] ?></td>
                        <td><?php echo $mostrar[2]; ?></td>
                        <td><?php echo $mostrar[3]; ?></td>
                        <td><?php echo $mostrar[4]; ?></td>
                        <td><?php echo $mostrar[5]; ?></td>
                        <td><?php echo $mostrar[6]; ?></td>
                        <td><?php echo $mostrar[7]; ?></td>
                        <td><?php echo "$".$mostrar[8] ?></td>
                        <td><?php echo $mostrar[9] ?></td>
                        <td><?php echo $mostrar[10] ?></td>
                        <td><?php echo $mostrar[11]; ?></td>
                  </tr>
                  <?php } ?>
                  </tbody>
                  </table>
            </div>
      </div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
</body>
</html>