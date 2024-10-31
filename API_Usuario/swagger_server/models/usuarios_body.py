# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UsuariosBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nombre_completo: str=None, correo: str=None, contrasea: str=None, imagen_perfil: str=None, metodo_pago: str=None, idioma: str=None, generos_favoritos: List[str]=None):  # noqa: E501
        """UsuariosBody - a model defined in Swagger

        :param nombre_completo: The nombre_completo of this UsuariosBody.  # noqa: E501
        :type nombre_completo: str
        :param correo: The correo of this UsuariosBody.  # noqa: E501
        :type correo: str
        :param contrasea: The contrasea of this UsuariosBody.  # noqa: E501
        :type contrasea: str
        :param imagen_perfil: The imagen_perfil of this UsuariosBody.  # noqa: E501
        :type imagen_perfil: str
        :param metodo_pago: The metodo_pago of this UsuariosBody.  # noqa: E501
        :type metodo_pago: str
        :param idioma: The idioma of this UsuariosBody.  # noqa: E501
        :type idioma: str
        :param generos_favoritos: The generos_favoritos of this UsuariosBody.  # noqa: E501
        :type generos_favoritos: List[str]
        """
        self.swagger_types = {
            'nombre_completo': str,
            'correo': str,
            'contrasea': str,
            'imagen_perfil': str,
            'metodo_pago': str,
            'idioma': str,
            'generos_favoritos': List[str]
        }

        self.attribute_map = {
            'nombre_completo': 'nombre_completo',
            'correo': 'correo',
            'contrasea': 'contraseña',
            'imagen_perfil': 'imagen_perfil',
            'metodo_pago': 'metodo_pago',
            'idioma': 'idioma',
            'generos_favoritos': 'generos_favoritos'
        }
        self._nombre_completo = nombre_completo
        self._correo = correo
        self._contrasea = contrasea
        self._imagen_perfil = imagen_perfil
        self._metodo_pago = metodo_pago
        self._idioma = idioma
        self._generos_favoritos = generos_favoritos

    @classmethod
    def from_dict(cls, dikt) -> 'UsuariosBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The usuarios_body of this UsuariosBody.  # noqa: E501
        :rtype: UsuariosBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nombre_completo(self) -> str:
        """Gets the nombre_completo of this UsuariosBody.

        Nombre completo del usuario  # noqa: E501

        :return: The nombre_completo of this UsuariosBody.
        :rtype: str
        """
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, nombre_completo: str):
        """Sets the nombre_completo of this UsuariosBody.

        Nombre completo del usuario  # noqa: E501

        :param nombre_completo: The nombre_completo of this UsuariosBody.
        :type nombre_completo: str
        """
        if nombre_completo is None:
            raise ValueError("Invalid value for `nombre_completo`, must not be `None`")  # noqa: E501

        self._nombre_completo = nombre_completo

    @property
    def correo(self) -> str:
        """Gets the correo of this UsuariosBody.

        Correo electrónico del usuario  # noqa: E501

        :return: The correo of this UsuariosBody.
        :rtype: str
        """
        return self._correo

    @correo.setter
    def correo(self, correo: str):
        """Sets the correo of this UsuariosBody.

        Correo electrónico del usuario  # noqa: E501

        :param correo: The correo of this UsuariosBody.
        :type correo: str
        """
        if correo is None:
            raise ValueError("Invalid value for `correo`, must not be `None`")  # noqa: E501

        self._correo = correo

    @property
    def contrasea(self) -> str:
        """Gets the contrasea of this UsuariosBody.

        Contraseña del usuario  # noqa: E501

        :return: The contrasea of this UsuariosBody.
        :rtype: str
        """
        return self._contrasea

    @contrasea.setter
    def contrasea(self, contrasea: str):
        """Sets the contrasea of this UsuariosBody.

        Contraseña del usuario  # noqa: E501

        :param contrasea: The contrasea of this UsuariosBody.
        :type contrasea: str
        """
        if contrasea is None:
            raise ValueError("Invalid value for `contrasea`, must not be `None`")  # noqa: E501

        self._contrasea = contrasea

    @property
    def imagen_perfil(self) -> str:
        """Gets the imagen_perfil of this UsuariosBody.

        URL de la imagen de perfil del usuario  # noqa: E501

        :return: The imagen_perfil of this UsuariosBody.
        :rtype: str
        """
        return self._imagen_perfil

    @imagen_perfil.setter
    def imagen_perfil(self, imagen_perfil: str):
        """Sets the imagen_perfil of this UsuariosBody.

        URL de la imagen de perfil del usuario  # noqa: E501

        :param imagen_perfil: The imagen_perfil of this UsuariosBody.
        :type imagen_perfil: str
        """

        self._imagen_perfil = imagen_perfil

    @property
    def metodo_pago(self) -> str:
        """Gets the metodo_pago of this UsuariosBody.

        Método de pago preferido del usuario  # noqa: E501

        :return: The metodo_pago of this UsuariosBody.
        :rtype: str
        """
        return self._metodo_pago

    @metodo_pago.setter
    def metodo_pago(self, metodo_pago: str):
        """Sets the metodo_pago of this UsuariosBody.

        Método de pago preferido del usuario  # noqa: E501

        :param metodo_pago: The metodo_pago of this UsuariosBody.
        :type metodo_pago: str
        """

        self._metodo_pago = metodo_pago

    @property
    def idioma(self) -> str:
        """Gets the idioma of this UsuariosBody.

        Idioma preferido (\"español\", \"inglés\", \"portugués\"...)  # noqa: E501

        :return: The idioma of this UsuariosBody.
        :rtype: str
        """
        return self._idioma

    @idioma.setter
    def idioma(self, idioma: str):
        """Sets the idioma of this UsuariosBody.

        Idioma preferido (\"español\", \"inglés\", \"portugués\"...)  # noqa: E501

        :param idioma: The idioma of this UsuariosBody.
        :type idioma: str
        """

        self._idioma = idioma

    @property
    def generos_favoritos(self) -> List[str]:
        """Gets the generos_favoritos of this UsuariosBody.

        Lista de géneros favoritos del usuario (máximo 4)  # noqa: E501

        :return: The generos_favoritos of this UsuariosBody.
        :rtype: List[str]
        """
        return self._generos_favoritos

    @generos_favoritos.setter
    def generos_favoritos(self, generos_favoritos: List[str]):
        """Sets the generos_favoritos of this UsuariosBody.

        Lista de géneros favoritos del usuario (máximo 4)  # noqa: E501

        :param generos_favoritos: The generos_favoritos of this UsuariosBody.
        :type generos_favoritos: List[str]
        """

        self._generos_favoritos = generos_favoritos
