# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.api_contenidoscomponentsschemasseries import APIContenidoscomponentsschemasseries  # noqa: F401,E501
from swagger_server import util


class VisualizacionesSeries(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, serie: APIContenidoscomponentsschemasseries=None, num_visualizaciones: int=None):  # noqa: E501
        """VisualizacionesSeries - a model defined in Swagger

        :param id: The id of this VisualizacionesSeries.  # noqa: E501
        :type id: str
        :param serie: The serie of this VisualizacionesSeries.  # noqa: E501
        :type serie: APIContenidoscomponentsschemasseries
        :param num_visualizaciones: The num_visualizaciones of this VisualizacionesSeries.  # noqa: E501
        :type num_visualizaciones: int
        """
        self.swagger_types = {
            'id': str,
            'serie': APIContenidoscomponentsschemasseries,
            'num_visualizaciones': int
        }

        self.attribute_map = {
            'id': 'id',
            'serie': 'serie',
            'num_visualizaciones': 'numVisualizaciones'
        }
        self._id = id
        self._serie = serie
        self._num_visualizaciones = num_visualizaciones

    @classmethod
    def from_dict(cls, dikt) -> 'VisualizacionesSeries':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The visualizacionesSeries of this VisualizacionesSeries.  # noqa: E501
        :rtype: VisualizacionesSeries
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this VisualizacionesSeries.


        :return: The id of this VisualizacionesSeries.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this VisualizacionesSeries.


        :param id: The id of this VisualizacionesSeries.
        :type id: str
        """

        self._id = id

    @property
    def serie(self) -> APIContenidoscomponentsschemasseries:
        """Gets the serie of this VisualizacionesSeries.


        :return: The serie of this VisualizacionesSeries.
        :rtype: APIContenidoscomponentsschemasseries
        """
        return self._serie

    @serie.setter
    def serie(self, serie: APIContenidoscomponentsschemasseries):
        """Sets the serie of this VisualizacionesSeries.


        :param serie: The serie of this VisualizacionesSeries.
        :type serie: APIContenidoscomponentsschemasseries
        """

        self._serie = serie

    @property
    def num_visualizaciones(self) -> int:
        """Gets the num_visualizaciones of this VisualizacionesSeries.


        :return: The num_visualizaciones of this VisualizacionesSeries.
        :rtype: int
        """
        return self._num_visualizaciones

    @num_visualizaciones.setter
    def num_visualizaciones(self, num_visualizaciones: int):
        """Sets the num_visualizaciones of this VisualizacionesSeries.


        :param num_visualizaciones: The num_visualizaciones of this VisualizacionesSeries.
        :type num_visualizaciones: int
        """

        self._num_visualizaciones = num_visualizaciones
