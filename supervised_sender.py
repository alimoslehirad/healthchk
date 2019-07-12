from typing import Any, Optional

from apps.supervised_request.models import ServiceInvocation


class SupervisedSender(object):
    @property
    def name(self) -> str:
        raise NotImplementedError("class parameter name should be set for sender")

    @property
    def uses_bulk_check_delivery(self) -> bool:
        raise NotImplementedError("class parameter uses_bulk_check_delivery should be set for sender")

    @property
    def build_data_for_delivery_check_from_response(self) -> bool:
        raise NotImplementedError(
            "class parameter build_data_for_delivery_check_from_response should be set for sender")

    @property
    def secure_fields(self) -> list:
        """
        A property that returns the field names that should be stored without full exposure
        :return: list of field names
        """
        raise NotImplementedError("Method secure_fields must be implemented.")

    @classmethod
    def make_request(cls, data: Optional[dict] = None) -> (Any, int, Any):
        """
        A function that takes request_data and performs the request and checks the response to detect the status.
        :param data: request data to send
        :return: A Tuple containing response object, status and client's request data
        :return :type: first argument is the response instance. The second argument is an integer
        defining what status the request is at. From constants.py of app STATUS_TYPES. The third argument is
        the data the client has used to make the request
        """
        raise NotImplementedError("Method make_request should be implemented")

    @classmethod
    def make_bulk_request(cls, data: Optional[dict] = None) -> (Any, int, Any, Any):
        """
        A function that takes request_data and performs the bulk request and checks the response to detect the status.
        :param data: request data to send
        :return: A Tuple containing response object, status, client's request data and states of each service
        :return :type: first argument is the response instance. The second argument is an integer
        defining what status the request is at. From constants.py of app STATUS_TYPES. The third argument is
        the data the client has used to make the request. The fourth argument is a list of each item in bulk request
        in the form of:
        {
            "data": SOME_DATA,
            "status": ServiceInvocation.STATUS_CHOICES
        }
        """
        raise NotImplementedError("Method make_bulk_request should be implemented")

    @classmethod
    def check_bulk_delivery(cls, data: Optional[dict] = None) -> (Any, int, Any, Any):
        """
        A function that takes request_data and performs the bulk request and checks the response to detect the status.
        :param data: request data to send
        :return: A Tuple containing response object, status, client's request data and states of each service
        :return :type: first argument is the response instance. The second argument is an integer
        defining what status the request is at. From constants.py of app STATUS_TYPES. The third argument is
        the data the client has used to make the request. The fourth argument is a list of each item in bulk request
        in the form of:
        {
            "data": SOME_DATA,
            "status": ServiceInvocation.STATUS_CHOICES
        }
        """
        raise NotImplementedError("Method check_bulk_delivery should be implemented")

    @classmethod
    def rebuild_data_for_bulk_request(cls, data: Optional[dict] = None) -> Any:
        """
        A function that takes request_data and changes it to make it usable by make_bulk_request
        :param data:
        :return:
        """
        raise NotImplementedError("Method rebuild_data_for_bulk_request must be implemented")

    @classmethod
    def build_exported_data_from_states(cls, states_detail) -> Any:
        """
        A function that takes a response object of the same sender and returns a dictionary of data to export for
        further use
        :param states_detail: The states_detail dictionary to build exported data from
        :return: The exported data dictionary
        """
        raise NotImplementedError("Method build_exported_data_from_states must be implemented")

    @classmethod
    def build_data_for_bulk_retry(cls, invocation: ServiceInvocation) -> Any:
        """
        A function that takes invocation and returns the data to use for retrying bulk invocation in recovery
        :param invocation: The invocation to extract data from
        :return: The new data
        """
        raise NotImplementedError("Method build_data_for_bulk_retry must be implemented")

    @classmethod
    def rebuild_pending_states_for_bulk_check(cls, pending_states) -> Any:
        """
        A function that takes invocation and returns the data to use for check_bulk_delivery invocation in recovery
        :param pending_states: The pending_states list
        :return: The new data
        """
        raise NotImplementedError("Method rebuild_pending_states_for_bulk_check must be implemented")

    @classmethod
    def check_delivery_status(cls, data: Optional[dict] = None) -> (Any, int, Any):
        """
        A function that takes request_data and performs the delivery check for this sender.
        :param data: request data to send
        :return: A Tuple containing Response object, status, and client data
        """
        raise NotImplementedError("Method check_delivery_status must be implemented")

    @classmethod
    def rebuild_data(cls, data: Optional[dict] = None) -> Optional[dict]:
        """
        A function that takes request_data and changes it to make it usable by make_request
        :param data:
        :return:
        """
        raise NotImplementedError("Method rebuild_data must be implemented")

    @classmethod
    def build_data_for_delivery_check(cls, response: Any, request_data: Optional[dict]) -> Optional[dict]:
        """
        A function that takes a response object of the same sender and a request data dictionary to pass to
        the appropriate function to build data for delivery check
        dictionary for method check_delivery_status
        :param request_data: The request data
        :param response: The response of request
        :return:
        """
        if cls.build_data_for_delivery_check_from_response:
            return cls.build_data_for_delivery_from_response(response)
        else:
            return cls.build_data_for_delivery_from_request_data(request_data)

    @classmethod
    def build_exported_data(cls, response: Any) -> Optional[dict]:
        """
        A function that takes a response object of the same sender and returns a dictionary of data to export for
        further use
        :param response: The response object to build exported data from
        :return: The exported data dictionary
        """
        raise NotImplementedError("Method build_exported_data must be implemented")

    @classmethod
    def build_data_for_delivery_from_response(cls, response: Any) -> Optional[dict]:
        """
        A function that takes a response object of the same sender and builds the data dictionary for checking delivery
        :param response: The response object to extract the data from
        :return: data dictionary
        """
        raise NotImplementedError("Method build_data_for_delivery_from_response must be implemented")

    @classmethod
    def build_data_for_delivery_from_request_data(cls, request_data: Optional[dict]) -> Optional[dict]:
        """
        A function that takes the request data of the original request and builds the data dictionary for checking
        delivery
        :param request_data: The request data that was used for this service
        :return: data dictionary
        """
        raise NotImplementedError("Method build_data_for_delivery_from_request_data must be implemented")

    @classmethod
    def check_credit(cls) -> Optional[int]:
        """
        A function that returns the remaining credit of a sender
        :return:
        """
        raise NotImplementedError("Method check_credit must be implemented.")
