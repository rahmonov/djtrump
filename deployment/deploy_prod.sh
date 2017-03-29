#!/usr/bin/env bash

ssh root@104.236.57.112 <<EOF
  cd djtrump
  git pull
  source /opt/envs/djtrump/bin/activate
  pip install -r requirements.txt
  sudo supervisorctl restart djtrump
  exit
EOF
