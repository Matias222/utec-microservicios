from fastapi import FastAPI, HTTPException, Depends
from orm import Session, Cliente, get_db, Pedido, DetallePedido

app = FastAPI()

# CRUD for "clientes"
@app.post("/clientes/")
def create_cliente(nombre: str, correo: str, telefono: str = None, db: Session = Depends(get_db)):
    cliente = Cliente(nombre=nombre, correo=correo, telefono=telefono)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

@app.get("/clientes/{id_cliente}")
def read_cliente(id_cliente: int, db: Session = Depends(get_db)) :
    cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return cliente

@app.put("/clientes/{id_cliente}")
def update_cliente(id_cliente: int, nombre: str, correo: str, telefono: str = None, db: Session = Depends(get_db)) :
    cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    cliente.nombre = nombre
    cliente.correo = correo
    cliente.telefono = telefono
    db.commit()
    db.refresh(cliente)
    return cliente

@app.delete("/clientes/{id_cliente}")
def delete_cliente(id_cliente: int, db: Session = Depends(get_db)) :
    cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    db.delete(cliente)
    db.commit()
    return "Cliente deleted"

# CRUD for "pedidos"
@app.post("/pedidos/")
def create_pedido(id_cliente: int, fecha: str, total: float, db: Session = Depends(get_db)):
    pedido = Pedido(id_cliente=id_cliente, fecha=fecha, total=total)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido

@app.get("/pedidos/{id_pedido}")
def read_pedido(id_pedido: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido not found")
    return pedido

@app.put("/pedidos/{id_pedido}")
def update_pedido(id_pedido: int, id_cliente: int, fecha: str, total: float, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido not found")
    pedido.id_cliente = id_cliente
    pedido.fecha = fecha
    pedido.total = total
    db.commit()
    db.refresh(pedido)
    return pedido

@app.delete("/pedidos/{id_pedido}")
def delete_pedido(id_pedido: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido not found")
    db.delete(pedido)
    db.commit()
    return "Pedido deleted"

# CRUD for "detalle_pedidos"
@app.post("/detalle_pedidos/")
def create_detalle_pedido(id_pedido: int, id_libro: int, cantidad: int, precio_unitario: float, db: Session = Depends(get_db)):
    detalle = DetallePedido(id_pedido=id_pedido, id_libro=id_libro, cantidad=cantidad, precio_unitario=precio_unitario)
    db.add(detalle)
    db.commit()
    db.refresh(detalle)
    return detalle

@app.get("/detalle_pedidos/{id_detalle}")
def read_detalle_pedido(id_detalle: int, db: Session = Depends(get_db)):
    detalle = db.query(DetallePedido).filter(DetallePedido.id_detalle == id_detalle).first()
    if detalle is None:
        raise HTTPException(status_code=404, detail="DetallePedido not found")
    return detalle

@app.put("/detalle_pedidos/{id_detalle}")
def update_detalle_pedido(id_detalle: int, id_pedido: int, id_libro: int, cantidad: int, precio_unitario: float, db: Session = Depends(get_db)):
    detalle = db.query(DetallePedido).filter(DetallePedido.id_detalle == id_detalle).first()
    if detalle is None:
        raise HTTPException(status_code=404, detail="DetallePedido not found")
    detalle.id_pedido = id_pedido
    detalle.id_libro = id_libro
    detalle.cantidad = cantidad
    detalle.precio_unitario = precio_unitario
    db.commit()
    db.refresh(detalle)
    return detalle

@app.delete("/detalle_pedidos/{id_detalle}")
def delete_detalle_pedido(id_detalle: int, db: Session = Depends(get_db)):
    detalle = db.query(DetallePedido).filter(DetallePedido.id_detalle == id_detalle).first()
    if detalle is None:
        raise HTTPException(status_code=404, detail="DetallePedido not found")
    db.delete(detalle)
    db.commit()
    return "DetallePedido deleted"
