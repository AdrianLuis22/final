# emergencias/views.py

import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateformat import DateFormat
from .models import AlertaEmergencia
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

@csrf_exempt
def recibir_alerta(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lat = data.get("lat")
        lng = data.get("lng")
        direccion = "Ubicación desconocida"

        # Convertir coordenadas a dirección
        if lat and lng:
            try:
                url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lng}&format=json"
                response = requests.get(url, headers={"User-Agent": "EmergenciasApp/1.0"})
                if response.status_code == 200:
                    direccion = response.json().get("display_name", direccion)
            except:
                pass

        AlertaEmergencia.objects.create(
            nombre=data.get("nombre"),
            cedula=data.get("cedula"),
            telefono=data.get("telefono", ""),
            ubicacion=direccion
        )

        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "Método no permitido"}, status=405)


def listar_alertas(request):
    alertas = AlertaEmergencia.objects.filter(atendido=False).order_by('-fecha_hora')[:5]
    data = [{
        "nombre": a.nombre,
        "ubicacion": a.ubicacion,
        "telefono": a.telefono,
        "fecha_hora": DateFormat(a.fecha_hora).format("d/m/Y H:i"),
    } for a in alertas]
    return JsonResponse(data, safe=False)
