# Docker

## Why does Saltbox use the Docker network "saltbox" instead of bridge?

1. This keeps all Saltbox containers organized under one network
2. the docker bridge network does not allow network aliases.
