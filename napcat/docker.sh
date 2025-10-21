docker run -d \
-e NAPCAT_GID=$(id -g) \
-e NAPCAT_UID=$(id -u) \
-p 6099:6099 \
-v ./data/ntqq:/app/.config/QQ \
-v ./data/config:/app/napcat/ \
--name napcat \
--restart=unless-stopped \
mlikiowa/napcat-docker:latest