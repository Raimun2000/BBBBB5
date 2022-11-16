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
      <title>Comparaciones</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
      <style>
      img {
            width: 75px;
      }
      </style>
</head>
<body>
      <div class="container p-4">
            <div class="row">
                  <h1 class="text-primary p-4 text-center">Precio promedio de un libro según la editorial</h1>
                  <h4 class="bg-info text-dark p-4 text-center rounded">(en base a los libros guardados en la BBDD)</h4>
                  <table class="table">
                  <thead>
                  <tr>
                        <th scope="col">Editorial</th>
                        <th scope="col">Precio promedio</th>
                        <th scope="col">Libros promediados</th>
                  </tr>
                  </thead>
                  <tbody>
                  <?php 
                  $obj = new conectar();
			$sql = "SELECT editorial, AVG(precio), SUM(visible) FROM libros WHERE visible GROUP BY editorial;";
                  $recup = $obj->ver($obj->conexion(), $sql);
                  $contador = 0;
                  $libros = 0;
                  while ($mostrar = mysqli_fetch_row($recup)) { 
                        ?>
                  <th scope="row"><?php 
                  echo $mostrar[0]; ?></th>
                  <td><?php echo "$ ".number_format($mostrar[1], 2, ',', '.'); ?></td>
                  <td><?php echo $mostrar[2]; 
                  $contador++;
                  $libros = $libros+$mostrar[2];
                  ?></td>
                  </tr>
                        <?php } ?>
                  <tr class="bg-dark text-light">
                        <td><?php echo "Total editoriales: ".$contador; ?></td>
                        <td></td>
                        <td><?php echo "Total libros: ".$libros; ?></td>
                  </tr>
                  </tbody>
            </table>
            </div>
            <div class="row">
                              <div class="div col-12 text-center">
                                    <p><a class="btn btn-primary" href="index.php">Regresar</a></p>
                              </div>
                        </div>
      </div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
</body>
</html>