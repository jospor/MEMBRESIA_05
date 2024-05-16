
class Membresia:
    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        self._correo_electronico = correo_electronico
        self._numero_tarjeta = numero_tarjeta

    def cambiar_suscripcion(self, tipo_membresia: int):
        # lógica para cambiar la suscripción según el tipo solicitado
        pass

    def cancelar_suscripcion(self):
        # lógica para cancelar la suscripción (generar membresía Gratis)
        pass

    def obtener_correo_electronico(self):
        return self._correo_electronico

    def obtener_numero_tarjeta(self):
        return self._numero_tarjeta

class Gratis(Membresia):
    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        super().__init__(correo_electronico, numero_tarjeta)
        # Atributos y comportamiento específico para membresía Gratis

class Basica(Membresia):
    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        super().__init__(correo_electronico, numero_tarjeta)
        # atributos y comportamiento específico para membresía Básica

class Familiar(Membresia):
    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        super().__init__(correo_electronico, numero_tarjeta)
        self._dias_regalo = 7
        # atributos y comportamiento específico para membresía Familiar

    def modificar_control_parental(self):
        # lógica para modificar control parental (sin implementación)
        pass

class SinConexion(Membresia):
    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        super().__init__(correo_electronico, numero_tarjeta)
        self._dias_regalo = 7
        # atributos y comportamiento específico para membresía Sin Conexión

    def incrementar_contenido_sin_conexion(self):
        # lógica para incrementar contenido sin conexión (sin implementación)
        pass

class Pro(Membresia):
    def __init__(self, correo_electronico: str, numero_tarjeta: str):
        super().__init__(correo_electronico, numero_tarjeta)
        self._dias_regalo = 15
        # atributos y comportamiento específico para membresía Pro

    def modificar_control_parental(self):
        # lógica para modificar control parental (igual a membresía Familiar)
        pass

    def incrementar_contenido_sin_conexion(self):
        # lógica para incrementar contenido sin conexión (igual a membresía Sin Conexión)
        pass
