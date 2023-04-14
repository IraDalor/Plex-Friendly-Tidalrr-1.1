<div align="center">
  <h1>Tidalrr</h1>
</div>
<p align="center">
  Tidalrr is a self-hosted service that lets you download music tracks from Tidal.<br/>
  It can be interfaced with Lidarr to sync Artists, Albums, Playlists, etc. using the Lidarr integration.<br/>
  Tidalrr can also sync your Tidal Playlists to Plex & Plexamp.
</p>

## Todo:
- ✅ refactor and cleanup code
- ✅ remove video support
- ✅ configureable highest quality
- ✅ migrate interactive settings to a json config file
- ✅ migrate interactive settings to CLI arguments
- ✅ download content from a file list of links (great for playlists)
- ✅ query Lidarr wanted list of albums and downloads them
- Sync all user's playlists
- generate .pls and .m3u8 playlist files
- create and sync Plex Playlist from Tidal Playlists
- create an api webserver that can be used with Lidarr
- ✅ package it in a docker container [Dockerhub](https://hub.docker.com/r/jacobroyquebec/tidalrr)
- ✅ documentation

## 🎨 Libraries and reference

- [aigpy](https://github.com/yaronzz/AIGPY)
- [python-tidal](https://github.com/tamland/python-tidal)
- [redsea](https://github.com/redsudo/RedSea)
- [tidal-wiki](https://github.com/Fokka-Engineering/TIDAL/wiki)
- [tidal-dl](https://github.com/yaronzz/Tidal-Media-Downloader)
- [lidarr API](https://lidarr.audio/docs/api/#/)

## 📜 Disclaimer
- Private use only.
- Need a Tidal-HIFI subscription. 
- Do not use this method to distribute or pirate music.
- It may be illegal to use this in your country, so be informed.

## Usage
I recommend that you run it using docker or docker-compose.
The image is available on [dockerhub](https://hub.docker.com/r/jacobroyquebec/tidalrr)
but I also provide an example of a docker-compose file.
Modify it and run `docker-compose up -d`

To use, watch the docker logs to capture the login URL and authenticate your tidalrr instance to Tidal.

## Developing

```shell
./build.sh
```

