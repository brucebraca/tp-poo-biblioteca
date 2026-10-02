from libro import Libro
from socio import Socio


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.socios = []
        self._libros_por_isbn = {}
        self._socios_por_dni = {}

    def agregar_libro(self, libro):
        if libro.isbn in self._libros_por_isbn:
            raise ValueError("No se permiten ISBN repetidos")
        self.libros.append(libro)
        self._libros_por_isbn[libro.isbn] = libro

    def registrar_socio(self, socio):
        if socio.dni in self._socios_por_dni:
            raise ValueError("No se permiten DNI repetidos")
        self.socios.append(socio)
        self._socios_por_dni[socio.dni] = socio

    def prestar(self, isbn, dni):
        libro = self._libros_por_isbn.get(isbn)
        socio = self._socios_por_dni.get(dni)

        if libro is None or socio is None:
            raise ValueError("Libro o socio inexistente")
        if not libro.disponible:
            raise ValueError("El libro no está disponible")
        if not socio.puede_pedir():
            raise ValueError("El socio ya alcanzó el máximo de libros")

        socio.agregar_libro(libro)
        libro.prestar()

    def devolver(self, isbn, dni):
        libro = self._libros_por_isbn.get(isbn)
        socio = self._socios_por_dni.get(dni)

        if libro is None or socio is None:
            raise ValueError("Libro o socio inexistente")
        if libro not in socio.libros:
            raise ValueError("Ese socio no tiene ese libro")

        socio.quitar_libro(libro)
        libro.devolver()

    def libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def __str__(self):
        return f"{self.nombre} - Libros: {len(self.libros)} - Socios: {len(self.socios)}"
