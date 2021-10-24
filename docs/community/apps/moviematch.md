# MovieMatch

## What is it?

[MovieMatch](https://github.com/LukeChannings/moviematch){: target=_blank rel="noopener noreferrer" } is an app that helps you and your friends pick a movie to watch from a Plex server.

MovieMatch connects to your Plex server and gets a list of movies (from any libraries marked as a movie library).

As many people as you want connect to your MovieMatch server and get a list of shuffled movies. Swipe right to +1, swipe left to -1.

If two (or more) people swipe right on the same movie, it'll show up in everyone's matches. The movies that the most people swiped right on will show up first.

## Project Information

- [:material-home: MovieMatch ](https://github.com/LukeChannings/moviematch){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://github.com/LukeChannings/moviematch){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/LukeChannings/moviematch#readme){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/lukechannings/moviematch){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-moviematch

```

### 2. URL

- To access MovieMatch, visit `https://moviematch._yourdomain.com_`

### 3. Setup

#### Via UI

- If you prefer to set up MovieMatch using a web interface, just start MovieMatch and you will be presented with a configuration screen. <br />
  The configuration will be saved in the working directory.

#### Via YAML

- MovieMatch can be configured with a simple YAML document, which allows connecting to multiple Plex servers. <br />
  Here's a simple example:

  ```YAML
    host: 0.0.0.0
    port: 8000
    servers:
      - url: https://plex.example.com
        token: abcdef12346
  ```

MovieMatch will read the config from `/opt/moviematch/config.yaml` by default.

- [:octicons-link-16: Documentation](https://github.com/LukeChannings/moviematch){: .header-icons target=_blank rel="noopener noreferrer" }
