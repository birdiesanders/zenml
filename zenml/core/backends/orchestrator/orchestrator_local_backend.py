#  Copyright (c) maiot GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Definition of the base Orchestrator Backend"""

from zenml.core.backends.base_backend import BaseBackend


class OrchestratorLocalBackend(BaseBackend):
    """Base class for all ZenML backends.

    Every ZenML pipeline runs in backends
    """
    BACKEND_TYPE = 'local'
    BACKEND_KEY = 'orchestrator'