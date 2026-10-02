class Libro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.isbn = ISBN
        self._disponible = True

    @property
    def disponible(self):
        return self._disponible

    def prestar(self):
        if not self._disponible:
            raise ValueError("El libro ya se encuentra prestado")
        self._disponible = False

    def devolver(self):
        if self._disponible:
            raise ValueError("El libro ya se encuentra disponible")
        self._disponible = True

    def __str__(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({estado})"


