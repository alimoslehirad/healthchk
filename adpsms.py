import json
import sys
from json import JSONDecodeError
from typing import Any, Optional

from rest_framework.status import HTTP_200_OK

from apps.supervised_request.models import ServiceInvocation
from apps.supervised_request.request_supervisor import SupervisedSender
from utils import services
from utils.exceptions import capture_exception
from utils.persian import ir_without_plus_phone_number


class ADPStatus:
    SUCCESSFUL = 'SMSC_MESSAGE_DELIVERED'
    PENDING = 'PENDING'


class ADPSmsSender(SupervisedSender):
    name = 'ADPSms'
    build_data_for_delivery_check_from_response = True
    secure_fields = ['X-SMS-APIKEY', 'apikey']
    send_message_response_key = 'send_message'
    check_status_response_key = 'status'

    @classmethod
    def check_credit(cls) -> int:
        pass

    @classmethod
    def build_data_for_delivery_from_response(cls, response: Any) -> Optional[dict]:
        return response.get(cls.send_message_response_key)

    @classmethod
    def build_data_for_delivery_from_request_data(cls, request_data: Optional[dict]) -> Optional[dict]:
        pass

    @classmethod
    def build_data_for_status_from_response(cls, response: dict) -> list:
        return list(set([d.get('msgId') for d in response.get('results')]))

    @classmethod
    def send_and_status_response(cls, send_message_response: dict, message_status_response):
        return {cls.send_message_response_key: send_message_response,
                cls.check_status_response_key: message_status_response}

    @classmethod
    def make_request(cls, data=None) -> (Any, int, Any):
        try:
            response, client_data = services.adp_sms_client.request_send_sms(data)
            msg_ids = cls.build_data_for_status_from_response(json.loads(response.content))
        except JSONDecodeError:
            exception_class = sys.exc_info()[0]
            response = {'exception': exception_class.__name__}
            status = ServiceInvocation.STATUS_CHOICES.failed
            return cls.send_and_status_response(response, {}), status, None
        except Exception as e:
            capture_exception(e)
            exception_class = sys.exc_info()[0]
            response = {'exception': exception_class.__name__}
            status = ServiceInvocation.STATUS_CHOICES.failed
            return cls.send_and_status_response(response, {}), status, None

        if len(msg_ids) > 1:
            status = ServiceInvocation.STATUS_CHOICES.delivered
            return cls.send_and_status_response(json.loads(response.content), {}), status, client_data
        try:

            status_response, is_multi_status = services.adp_sms_client.request_send_sms_status(msg_ids)
            approve_status_code = status_response.status_code
            raw_status_response = json.loads(status_response.content)
            status_response = cls.reformat_status_response(raw_status_response, msg_ids,
                                                           is_multi_status)
        except Exception as e:
            capture_exception(e)
            status = ServiceInvocation.STATUS_CHOICES.pending
            return cls.send_and_status_response(response, None), status, client_data

        status = cls.assert_status(response.status_code, approve_status_code, status_response)
        return cls.send_and_status_response(json.loads(response.content), raw_status_response), status, client_data

    @classmethod
    def reformat_status_response(cls, response, msg_ids, is_multi_status):
        """

        :param response: response from client's request_send_sms_status
        :param msg_ids: message ids which had been passed to the client
        :param is_multi_status: from this we predict the structure of response object
        :return: {`msg_id`: status for msg_id}
        """

        msg_id_status = {}
        if is_multi_status:
            if not isinstance(response, list):
                return {msg_id: '' for msg_id in msg_ids}
            for result in response:
                try:
                    msg_id_status[result[0]] = result[1] or ADPStatus.PENDING
                except:
                    msg_id_status[result[0]] = ADPStatus.PENDING
        else:
            try:
                msg_id_status[msg_ids[0]] = response[0][0] or ADPStatus.PENDING
            except:
                msg_id_status[msg_ids[0]] = ADPStatus.PENDING
        return msg_id_status

    @classmethod
    def assert_status(cls, status_code: int, approve_status_code: int, status_response: dict) -> int:
        if status_code != HTTP_200_OK:
            return ServiceInvocation.STATUS_CHOICES.failed
        if approve_status_code != HTTP_200_OK:
            return ServiceInvocation.STATUS_CHOICES.pending
        for msg_id, status in status_response.items():
            if status == ADPStatus.SUCCESSFUL:
                return ServiceInvocation.STATUS_CHOICES.delivered
        for msg_id, status in status_response.items():
            if status == ADPStatus.PENDING:
                return ServiceInvocation.STATUS_CHOICES.pending

        return ServiceInvocation.STATUS_CHOICES.failed

    @classmethod
    def check_delivery_status(cls, data: Optional[dict] = None) -> (Any, int):
        try:
            msg_ids = cls.build_data_for_status_from_response(data)
            response, is_multi_status = services.adp_sms_client.request_send_sms_status(msg_ids)
            status_code = response.status_code
            response = cls.reformat_status_response(json.loads(response.content), msg_ids, is_multi_status)
        except Exception as e:
            capture_exception(e)
            exception_class = sys.exc_info()[0]
            response = {'exception': exception_class.__name__}
            status = ServiceInvocation.STATUS_CHOICES.pending
            return response, status, None
        status = cls.assert_status(HTTP_200_OK, status_code, response)
        return response, status, data

    @classmethod
    def rebuild_data(cls, data: Optional[dict] = None) -> Optional[dict]:
        to = data.get('to')
        content = data.get('content')
        persian = data.get('persian')
        data = []
        phone_numbers = to if isinstance(to, list) else [to]
        for i in range(len(phone_numbers)):
            phone_number = ir_without_plus_phone_number(phone_numbers[i])
            msg = content[i] if isinstance(content, list) else content
            data.append({
                "src": "{prefix}{sender}".format(prefix='98', sender=services.adp_sms_client.sender),
                "dest": phone_number,
                "msg": services.adp_sms_client.clean_text(msg, persian)
            })
        return {'data': data}

    @classmethod
    def build_exported_data(cls, response: Any) -> Optional[dict]:
        pass
