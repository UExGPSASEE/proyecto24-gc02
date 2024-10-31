# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.capitulo import Capitulo  # noqa: F401,E501
from swagger_server import util


class Temporada(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, descripcion: str=None, numero: int=None, capitulos: List[Capitulo]=None):  # noqa: E501
        """Temporada - a model defined in Swagger

        :param id: The id of this Temporada.  # noqa: E501
        :type id: str
        :param descripcion: The descripcion of this Temporada.  # noqa: E501
        :type descripcion: str
        :param numero: The numero of this Temporada.  # noqa: E501
        :type numero: int
        :param capitulos: The capitulos of this Temporada.  # noqa: E501
        :type capitulos: List[Capitulo]
        """
        self.swagger_types = {
            'id': str,
            'descripcion': str,
            'numero': int,
            'capitulos': List[Capitulo]
        }

        self.attribute_map = {
            'id': 'id',
            'descripcion': 'descripcion',
            'numero': 'numero',
            'capitulos': 'capitulos'
        }
        self._id = id
        self._descripcion = descripcion
        self._numero = numero
        self._capitulos = capitulos

    @classmethod
    def from_dict(cls, dikt) -> 'Temporada':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Temporada of this Temporada.  # noqa: E501
        :rtype: Temporada
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Temporada.


        :return: The id of this Temporada.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Temporada.


        :param id: The id of this Temporada.
        :type id: str
        """

        self._id = id

    @property
    def descripcion(self) -> str:
        """Gets the descripcion of this Temporada.


        :return: The descripcion of this Temporada.
        :rtype: str
        """
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        """Sets the descripcion of this Temporada.


        :param descripcion: The descripcion of this Temporada.
        :type descripcion: str
        """

        self._descripcion = descripcion

    @property
    def numero(self) -> int:
        """Gets the numero of this Temporada.


        :return: The numero of this Temporada.
        :rtype: int
        """
        return self._numero

    @numero.setter
    def numero(self, numero: int):
        """Sets the numero of this Temporada.


        :param numero: The numero of this Temporada.
        :type numero: int
        """

        self._numero = numero

    @property
    def capitulos(self) -> List[Capitulo]:
        """Gets the capitulos of this Temporada.


        :return: The capitulos of this Temporada.
        :rtype: List[Capitulo]
        """
        return self._capitulos

    @capitulos.setter
    def capitulos(self, capitulos: List[Capitulo]):
        """Sets the capitulos of this Temporada.


        :param capitulos: The capitulos of this Temporada.
        :type capitulos: List[Capitulo]
        """

        self._capitulos = capitulos
