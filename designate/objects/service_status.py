# Copyright 2016 Hewlett Packard Enterprise Development Company LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from designate.objects import base


class ServiceStatus(base.PersistentObjectMixin,
                    base.DictObjectMixin,
                    base.DesignateObject):
    FIELDS = {
        "service_name": {
            "schema": {
                "type": "string"
            }
        },
        "hostname": {
            "schema": {
                "type": "string"
            }
        },
        "heartbeated_at": {
            "schema": {
                'type': ['string', 'null'],
                'format': 'date-time'
            }
        },
        "status": {
            "schema": {
                "type": "string",
                "enum": ["UP", "DOWN", "WARNING"]
            }
        },
        "stats": {
            "schema": {
                "type": "object",
            }
        },
        "capabilities": {
            "schema": {
                "type": "object"
            }
        }
    }

    STRING_FIELDS = [
        'service_name', 'hostname', 'status'
    ]


class ServiceStatusList(base.ListObjectMixin, base.DesignateObject):
    LIST_ITEM_TYPE = ServiceStatus
