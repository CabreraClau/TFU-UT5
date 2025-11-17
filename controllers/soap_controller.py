from flask import Blueprint, request, Response
from services.usuarios_service import get_all

soap_bp = Blueprint("soap", __name__)

@soap_bp.post("/soap/usuarios")
def soap_listar_usuarios():
    xml_body = request.data.decode("utf-8")

    if "<ListarUsuarios" not in xml_body:
        return Response("Operación no soportada", status=400)

    usuarios = get_all()

    # XML de respuesta
    xml_response = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">',
        '  <soap:Body>',
        '    <ListarUsuariosResponse>'
    ]

    # Agregar usuarios de forma segura
    for u in usuarios:
        xml_response.extend([
            '      <Usuario>',
            f'        <Id>{u["id"]}</Id>',
            f'        <Nombre>{u["nombre"]}</Nombre>',
            f'        <Email>{u["email"]}</Email>',
            '      </Usuario>'
        ])

    # Cerrar nodos
    xml_response.extend([
        '    </ListarUsuariosResponse>',
        '  </soap:Body>',
        '</soap:Envelope>'
    ])

    final_xml = "\n".join(xml_response)
    return Response(final_xml, mimetype="text/xml")
