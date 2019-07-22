#!/bin/bash

for i in `seq 1 $1`; do curl -X GET https://api-alpha.qbitpay.org/admin/transactions/transaction/?p=$i -k -vvv -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Cookie: csrftoken=1oushUA0aUNor2zTe2CeEsoLuVrltyOxJEWl6coKWwWfDTC2qCsOrSlTh7AMGRJ9; sessionid=3qzf88nge0gqpksnq96yh2yq7zqjrkum" > /dev/null 2>&1 &  done;
