#!/bin/bash

export MAIL_TOKEN='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'
export TELEGRAM_TOKEN='879341611:AAHjdFnz30JHuXepwl4XUgaufH8hriMDjT8'
export TELEGRAM_GROUP='-328266093'
export SERVER='pg1'
export PROXY_IP='proxy1.qcluster.org'
export PROXY_PORT=3128
export http_proxy="http://kube:bloodsucker@$PROXY_IP:$PROXY_PORT"
export https_proxy="http://kube:bloodsucker@$PROXY_IP:$PROXY_PORT"

#backup_date=`date '+%Y%m%d'`
#lastest_backup_available=`barman list-backup pg1 | awk '{ print $2 }' | head -1 | head -c8`
export MSG="test for toman-healthChk"


#if [ -n "$BARMAN_ERROR" -o "$backup_date" != "$lastest_backup_available" ]
#then
        curl -x $https_proxy -X GET "https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage?chat_id=$TELEGRAM_GROUP&text=$MSG"
	#fi

	$cred = Get-Credential -Message 'Please enter your credentials for the proxy server.'
