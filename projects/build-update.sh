#!/bin/bash
# ./build-update.sh username console.tw /home/username/console_tw_root_dir
pushd datachart && python build-org-term.py && popd
echo "update to $1@$2:$3"
pushd websites && rsync -av root/ $1@$2:$3 && popd
