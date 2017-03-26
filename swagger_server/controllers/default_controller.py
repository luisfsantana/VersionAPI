import connexion
from swagger_server.models.error import Error
from swagger_server.models.properties import Properties
from swagger_server.models.property import Property
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def properties_get(ax=None, ay=None, bx=None, by=None):
    """
    Gets some properties
    Returns a list containing all properties.
    :param ax: Top right ax
    :type ax: int
    :param ay: Top right ay
    :type ay: int
    :param bx: Lower left bx
    :type bx: int
    :param by: Lower left by
    :type by: int

    :rtype: Properties
    """
    return 'do some magic!'


def properties_id_delete(id):
    """
    Deletes a property
    Delete a single property identified via its id
    :param id: The person&#39;s id
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def properties_id_get(id):
    """
    Gets a property
    Returns a single property for its id.
    :param id: The id&#39;s property
    :type id: str

    :rtype: Property
    """
    return 'do some magic!'


def properties_post(property=None):
    """
    Creates a property
    Adds a new property to the properties list.
    :param property: The property to create.
    :type property: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        property = Property.from_dict(connexion.request.get_json())
    return 'do some magic!'
