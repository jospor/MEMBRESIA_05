
import membresia

gratis = membresia.Gratis("correo_electronico", "numero_tarjeta")
basica = membresia.Basica("correo_electronico", "numero_tarjeta")
familiar = membresia.Familiar("correo_electronico", "numero_tarjeta")
sin_conexion = membresia.SinConexion("correo_electronico", "numero_tarjeta")
pro = membresia.Pro("correo_electronico", "numero_tarjeta")

print(gratis.obtener_correo_electronico())
print(basica.obtener_numero_tarjeta())
familiar.modificar_control_parental()
sin_conexion.incrementar_contenido_sin_conexion()
pro.modificar_control_parental()
pro.incrementar_contenido_sin_conexion()
