# Docker

## Why does Saltbox use the Docker network "saltbox" instead of bridge?

(1) keeps all Saltbox containers organized under one network; and (2), bridge network does not allow network aliases.
