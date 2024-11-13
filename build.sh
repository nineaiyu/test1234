#!/bin/bash

docker run --rm -it -v ./:/app -e TZ=Asia/Shanghai \
  nineaiyu/test1234-base:20241113_092309 sh -c 'pnpm install --frozen-lockfile && pnpm build'

