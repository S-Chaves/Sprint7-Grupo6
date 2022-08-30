# Sprint 8 Grupo 6
En este Sprint creamos una API utilizando Django Rest Framework con multiples endpoints con distintos métodos HTTP.

## Rutas
- OBTENER DATOS DE UN CLIENTE  
  `/api/clientes/<int:customer_id>/` (Cliente Autenticado)
- OBTENER SALDO DE CUENTA DE UN CLIENTE  
  `/api/cuentas/<int:customer_id>/` (Cliente Autenticado)
- OBTENER MONTO DE PRESTAMOS DE UN CLIENTE  
  `/api/prestamos/<int:customer_id>/` (Cliente Autenticado)
- OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL  
  `/api/sucursales/prestamos/<int:branch_id>/` (Empleado Autenticado)
- OBTENER TARJETAS ASOCIADAS A UN CLIENTE  
  `/api/tarjetas/<int:customer_id>/` (Empleado Autenticado)
- GENERAR UNA SOLICITUD DE PRESTAMO PARA UN CLIENTE  
  `/api/prestamos/create/<int:customer_id>/<int:account_id>/` (Empleado Autenticado)
- ANULAR SOLICITUD DE PRESTAMO DE CLIENTE  
  `/api/prestamos/delete/<int:loan_id>/<int:account_id>/` (Empleado Autenticado)
- MODIFICAR DIRECCION DE UN CLIENTE  
  `/api/clientes/direccion/<int:customer_id>/` (Empleado o Cliente Autenticado)
- LISTADO DE TODAS LAS SUCURSALES  
  `/api/sucursales/` (Publico)

## Integrantes
- Timoteo Beltran
- María Constanza Weber
- Alexis Sanz
- Santiago Chaves
