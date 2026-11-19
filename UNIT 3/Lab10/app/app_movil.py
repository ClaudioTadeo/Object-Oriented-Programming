# --- 1. Jerarquía de Excepciones del Dominio ---

class SuscripcionExpiradaError(Exception):
    """Excepción lanzada al intentar operaciones restringidas sin suscripción activa."""
    pass


class PuntosInsuficientesError(Exception):
    """Excepción lanzada cuando una transacción excede el balance de gemas disponibles."""
    pass


# --- 2. Clase Base: PerfilMovil ---

class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True):
        if gemas < 0:
            raise ValueError("El balance inicial de gemas no puede ser negativo.")
        
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas a ganar debe ser estrictamente positiva.")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas a gastar debe ser estrictamente positiva.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError(
                f"Gemas insuficientes. Intentaste gastar {cantidad}, pero solo tienes {self.gemas}."
            )
        self.gemas -= cantidad
        return self.gemas


# --- 3. Subclase Derivada: PerfilPro ---

class PerfilPro(PerfilMovil):
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True, meses_suscripcion: int = 1):
        if meses_suscripcion <= 0:
            raise ValueError("Los meses iniciales de suscripción deben ser mayores a cero.")
        
        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0 or not self.es_pro:
            self.es_pro = False
            raise SuscripcionExpiradaError("Tu suscripción Pro ha expirado. No puedes descargar contenido offline.")
        return "Descarga de contenido offline iniciada con éxito."