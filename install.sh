#!/usr/bin/env bash

INSTALL_PATH=~/.bin/google-cloud-utils

append-module-to-path() {
  echo 'PATH="$PATH:'"$INSTALL_PATH/$1\"" >> ~/.bashrc
}

mkdir -p "$INSTALL_PATH"

cp -r create-cloud-function "$INSTALL_PATH"


append-module-to-path "create-cloud-function"
