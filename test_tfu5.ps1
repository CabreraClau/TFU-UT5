Write-Host "===== TEST AUTOMATIZADO TFU5 =====" -ForegroundColor Yellow

###############################################
#  1. CREAR USUARIOS
###############################################

Write-Host "`n===== CREANDO 4 USUARIOS =====" -ForegroundColor Cyan

(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/usuarios" -Headers @{ "Content-Type"="application/json"} -Body '{"nombre":"Claudio","email":"claudio@ucu.edu.uy"}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/usuarios" -Headers @{ "Content-Type"="application/json"} -Body '{"nombre":"Agus","email":"agus@ucu.edu.uy"}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/usuarios" -Headers @{ "Content-Type"="application/json"} -Body '{"nombre":"Rami","email":"rami@ucu.edu.uy"}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/usuarios" -Headers @{ "Content-Type"="application/json"} -Body '{"nombre":"Sofi","email":"sofi@ucu.edu.uy"}').Content




###############################################
#  2. CREAR PROYECTOS
###############################################

Write-Host "`n===== CREANDO 4 PROYECTOS =====" -ForegroundColor Cyan

(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/proyectos" -Headers @{ "Content-Type"="application/json"} -Body '{"nombre":"Proyecto A","usuario_id":1}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/proyectos" -Headers @{ "Content-Type"="application/json"} -Body '{"nombre":"Proyecto B","usuario_id":2}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/proyectos" -Headers @{ "Content-Type"="application/json"} -Body '{"nombre":"Proyecto C","usuario_id":3}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/proyectos" -Headers @{ "Content-Type"="application/json"} -Body '{"nombre":"Proyecto D","usuario_id":4}').Content


###############################################
#  3. LISTAR PROYECTOS
###############################################

Write-Host "`n===== LISTA DE PROYECTOS (TABLA) =====" -ForegroundColor Green
Invoke-RestMethod -Uri "http://localhost:5000/proyectos"

Write-Host "`n===== LISTA DE PROYECTOS (JSON CRUDO) =====" -ForegroundColor Yellow
Invoke-WebRequest -Uri "http://localhost:5000/proyectos" | Select-Object -ExpandProperty Content


###############################################
#  4. CREAR TAREAS
###############################################

Write-Host "`n===== CREANDO 4 TAREAS =====" -ForegroundColor Cyan

(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/tareas" -Headers @{ "Content-Type"="application/json"} -Body '{"descripcion":"Tarea 1","proyecto_id":1}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/tareas" -Headers @{ "Content-Type"="application/json"} -Body '{"descripcion":"Tarea 2","proyecto_id":2}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/tareas" -Headers @{ "Content-Type"="application/json"} -Body '{"descripcion":"Tarea 3","proyecto_id":3}').Content
(Invoke-WebRequest -Method POST -Uri "http://localhost:5000/tareas" -Headers @{ "Content-Type"="application/json"} -Body '{"descripcion":"Tarea 4","proyecto_id":4}').Content


###############################################
#  5. LISTAR TAREAS
###############################################

Write-Host "`n===== LISTA DE TAREAS (TABLA) =====" -ForegroundColor Green
Invoke-RestMethod -Uri "http://localhost:5000/tareas"

Write-Host "`n===== LISTA DE TAREAS (JSON CRUDO) =====" -ForegroundColor Yellow
Invoke-WebRequest -Uri "http://localhost:5000/tareas" | Select-Object -ExpandProperty Content


###############################################
#  6. PRUEBA SOAP
###############################################

Write-Host "`n===== EJECUTANDO SOAP (ListarUsuarios) =====" -ForegroundColor Magenta

$soapBody = '<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ListarUsuarios />
  </soap:Body>
</soap:Envelope>'

(Invoke-WebRequest -Method POST `
    -Uri "http://localhost:5000/soap/usuarios" `
    -ContentType "text/xml" `
    -Body $soapBody).Content


Write-Host "`n===== FIN DEL SCRIPT =====" -ForegroundColor Yellow
