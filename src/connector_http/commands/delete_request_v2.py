from typing import Any

import requests  # type: ignore
from spiffworkflow_connector_command.command_interface import ConnectorCommand
from spiffworkflow_connector_command.command_interface import ConnectorProxyResponseDict

from connector_http.http_request_base import HttpRequestBase


class DeleteRequestV2(ConnectorCommand, HttpRequestBase):
    def __init__(
        self,
        url: str,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        data: dict[str, str] | None = None,
        basic_auth_username: str | None = None,
        basic_auth_password: str | None = None,
        verify: bool | None = False
    ):
        HttpRequestBase.__init__(
            self, url=url, headers=headers, basic_auth_username=basic_auth_username, basic_auth_password=basic_auth_password,verify=verify
        )

        self.params = params
        self.data = data

    def execute(self, _config: Any, _task_data: dict) -> ConnectorProxyResponseDict:
        return self.run_request(requests.delete)
