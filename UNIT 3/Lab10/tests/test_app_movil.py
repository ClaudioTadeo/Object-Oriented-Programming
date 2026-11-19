import pytest
from app.app_movil import (
    PerfilMovil,
    PerfilPro,
    SuscripcionExpiradaError,
    PuntosInsuficientesError
)

# --- 1. Estado Aislado (@pytest.fixture) ---

@pytest.fixture
def perfil_estandar():
    """Fixture que provee una instancia estandarizada de PerfilMovil."""
    return PerfilMovil(username="gamer_base", gemas=50)


@pytest.fixture
def perfil_pro_valido():
    """Fixture que provee una instancia de PerfilPro activa."""
    return PerfilPro(username="gamer_pro", gemas=100, meses_suscripcion=3)


# --- 2. Pruebas de Integridad Estructural y Aserciones ---

def test_inicializacion_perfil_movil(perfil_estandar):
    """Verifica la asignación inicial de atributos en PerfilMovil."""
    assert perfil_estandar.username == "gamer_base"
    assert perfil_estandar.gemas == 50
    assert perfil_estandar.racha_dias == 1
    assert perfil_estandar.notificaciones_activas is True


def test_gastar_gemas_consistencia_aritmetica(perfil_estandar):
    """Verifica que el gasto de gemas reduzca el balance de forma exacta."""
    balance_resultante = perfil_estandar.gastar_gemas(20)
    assert balance_resultante == 30
    assert perfil_estandar.gemas == 30


# --- 3. Validación de Excepciones (pytest.raises) ---

def test_gastar_gemas_insuficientes(perfil_estandar):
    """Verifica que se lance PuntosInsuficientesError si el saldo no alcanza."""
    with pytest.raises(PuntosInsuficientesError):
        perfil_estandar.gastar_gemas(100)


def test_gastar_gemas_monto_invalido(perfil_estandar):
    """Verifica que gastar un monto cero o negativo lance ValueError."""
    with pytest.raises(ValueError):
        perfil_estandar.gastar_gemas(0)

    with pytest.raises(ValueError):
        perfil_estandar.gastar_gemas(-10)


def test_creacion_perfil_gemas_negativas():
    """Verifica que crear un perfil con gemas iniciales negativas lance ValueError."""
    with pytest.raises(ValueError):
        PerfilMovil(username="invalid_user", gemas=-5)


def test_descargar_offline_suscripcion_expirada(perfil_pro_valido):
    """Verifica el comportamiento y la excepción al vencer los meses de suscripción."""
    perfil_pro_valido.meses_suscripcion = 0
    
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro_valido.descargar_contenido_offline()
    
    # Comprobar que el estado de suscripción cambió a False tras el fallo
    assert perfil_pro_valido.es_pro is False


# --- 4. Pruebas Parametrizadas (@pytest.mark.parametrize) ---

@pytest.mark.parametrize("incremento, balance_esperado", [
    (10, 60),
    (50, 100),
    (100, 150),
    (1, 51)
])
def test_ganar_gemas_casos_validos(perfil_estandar, incremento, balance_esperado):
    """Evalúa múltiples vectores de prueba para el incremento de gemas."""
    nuevo_balance = perfil_estandar.ganar_gemas(incremento)
    assert nuevo_balance == balance_esperado
    assert perfil_estandar.gemas == balance_esperado


@pytest.mark.parametrize("monto_invalido", [0, -1, -50])
def test_ganar_gemas_valores_limite_invalidos(perfil_estandar, monto_invalido):
    """Evalúa que valores frontera no positivos en ganar_gemas lancen ValueError."""
    with pytest.raises(ValueError):
        perfil_estandar.ganar_gemas(monto_invalido)


# --- 5. Verificación de Tipos y Jerarquía (isinstance) ---

def test_jerarquia_herencia_perfil_pro(perfil_pro_valido):
    """Comprueba formalmente la relación de herencia entre PerfilPro y PerfilMovil."""
    assert isinstance(perfil_pro_valido, PerfilPro)
    assert isinstance(perfil_pro_valido, PerfilMovil)


def test_descargar_contenido_offline_exitoso(perfil_pro_valido):
    """Comprueba la ejecución exitosa del método especializado de PerfilPro."""
    resultado = perfil_pro_valido.descargar_contenido_offline()
    assert resultado == "Descarga de contenido offline iniciada con éxito."
    assert perfil_pro_valido.es_pro is True