import connexion
import six

from ..models.visualizaciones_peliculas import VisualizacionesPeliculas  # noqa: E501
from .. import util

from flask import request, jsonify
from ..... import dbconnection


def visualizaciones_peliculas_id_get(id):  # noqa: E501
    """las visualizaciones de una pelicula

     # noqa: E501

    :param id: ID de las visualizaciones de una película
    :type id: str

    :rtype: VisualizacionesPeliculas
    """
    try:
        visualizacion = dbconnection.dbGetMovieViews(id) # Supongo que esta función existe en `dbconnection`.
        if visualizacion:
            return jsonify(visualizacion), 200
        return {"error": "Visualizaciones de la película no disponibles"}, 404
    except Exception as e:
        return {"error": f"Error al obtener visualizaciones de la pelicula: {str(e)}"}, 500


def visualizaciones_peliculas_id_put(body, id):  # noqa: E501
    """Actualizar las visualizaciones de una película

     # noqa: E501

    :param body: Datos para actualizar las visualizaciones de la película
    :type body: dict | bytes
    :param id: ID de las visualizaciones de una película
    :type id: str

    :rtype: None
    """
    # supongo que el id de las visualizaciones coincide con el id del usuario
    if connexion.request.is_json:
        body = VisualizacionesPeliculas.from_dict(connexion.request.get_json())  # noqa: E501
        view = body.num_visualizaciones
        
        if dbconnection.dbUpdateMovieViews(id, id, view):
            return {"mensaje": "Visualizaciones actualizadas correctamente"}, 200
        else:
            return {"error": "No se han podido actualizar las visualizaciones"}, 400
    return {"error": "Solicitud inválida"}, 400