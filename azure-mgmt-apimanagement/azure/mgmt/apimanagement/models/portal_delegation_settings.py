# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class PortalDelegationSettings(Resource):
    """Delegation settings for a developer portal.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type for API Management resource.
    :vartype type: str
    :param url: A delegation Url.
    :type url: str
    :param validation_key: A base64-encoded validation key to validate, that a
     request is coming from Azure API Management.
    :type validation_key: str
    :param subscriptions: Subscriptions delegation settings.
    :type subscriptions:
     ~azure.mgmt.apimanagement.models.SubscriptionsDelegationSettingsProperties
    :param user_registration: User registration delegation settings.
    :type user_registration:
     ~azure.mgmt.apimanagement.models.RegistrationDelegationSettingsProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'properties.url', 'type': 'str'},
        'validation_key': {'key': 'properties.validationKey', 'type': 'str'},
        'subscriptions': {'key': 'properties.subscriptions', 'type': 'SubscriptionsDelegationSettingsProperties'},
        'user_registration': {'key': 'properties.userRegistration', 'type': 'RegistrationDelegationSettingsProperties'},
    }

    def __init__(self, **kwargs):
        super(PortalDelegationSettings, self).__init__(**kwargs)
        self.url = kwargs.get('url', None)
        self.validation_key = kwargs.get('validation_key', None)
        self.subscriptions = kwargs.get('subscriptions', None)
        self.user_registration = kwargs.get('user_registration', None)
