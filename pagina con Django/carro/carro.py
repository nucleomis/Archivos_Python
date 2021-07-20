#voy a crear una clase donde pueda obtener el request de la sesion para almacenar en una clase y usarla
#mas adelante

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"]= {}
        else:
            self.carro = carro

    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()):#compruebo que el id del producto no se repita en el carro
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url,
                "cantidad": 1,
            }
        else:
            for key, value in self.carro.items():
                if key == str (producto.id):
                    value["cantidad"] +=1
                    precio = float(producto.precio)+float(value["precio"])
                    value["precio"] = str(precio)
                    break
        self.guardar()
    
    def guardar(self):
        self.session["carro"] = self.carro
        self.session.modified = True#con esto modifico la session
    
    def eliminar(self, producto):
        producto.id = str(producto.id)

        if producto.id in self.carro:
            del self.carro[producto.id]
            self.session.modified = True
    
    def restar(self, producto):
        producto.id = str(producto.id)

        for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] -=1
                    precio = float(producto.precio)-float(value["precio"])
                    value["precio"] = str(precio)
                    if value["cantidad"] <= 0:
                        self.eliminar(producto)
                    break            
        self.guardar()
    
    def limpiar(self):
        self.session["carro"] = {}
        self.session.modified = True