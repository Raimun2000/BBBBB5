<?php 
	class conectar{
		public function conexion(){
			/* PRODUCCION */
			/// Incluir aquí los valores en caso de usarlos en producción
			/* ------------------------------------------------------------------------- */
			/* LOCAL */
			$conexion = mysqli_connect('localhost', 'root', '', 'Proy_Colab_BBBBB5');
			/* ------------------------------------------------------------------------- */
			$conexion->set_charset("utf8mb4");
			return $conexion;
		}

            public function ver($cnx, $sql){

                  $res = mysqli_query($cnx, $sql);
                  return $res;
            }
	}
 ?>