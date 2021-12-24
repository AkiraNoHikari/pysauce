# ![Kanna Inspect][logo] **Pysauce**
![](https://img.shields.io/github/workflow/status/AkiraNoHikari/pysauce/Docker%20Image%20CI?logo=github&style=flat-square)
![](https://img.shields.io/badge/version-0.1.0-green.svg?style=flat-square)
![](https://img.shields.io/badge/python-3.8-blue?style=flat-square)
![](https://img.shields.io/github/license/AkiraNoHikari/pysauce?style=flat-square)
![](https://img.shields.io/discord/923228837968511056?color=5865F2&style=flat-square)

> Pysauce is a Discord bot which utilizes the [SauceNAO](sauce_nao) API to locate the source of images.

## Use
Pysauce has one public instance always running, if you simply want to use Pysauce [invite][pysauce_invite] it to your guild.

## Install
There are several ways to install Pysauce, the recommended methods are either by downloading a pre-built or locally building the Docker container and running the resulting image.

### **Docker** - *Docker Hub* [Prebuilt]
```sh
# Docker & Python 3.8 or higher is required

docker pull

docker run -e BOT_TOKEN=YOUR_BOT_TOKEN -e SAUCENAO_TOKEN=YOUR_SAUCENAO_TOKEN pysauce
```

### **Docker** - *Github Container Registry* [Prebuilt]
```sh
# Docker & Python 3.8 or higher is required

docker pull ghcr.io/AkiraNoHikari/pysauce:latest

docker run -e BOT_TOKEN=YOUR_BOT_TOKEN -e SAUCENAO_TOKEN=YOUR_SAUCENAO_TOKEN pysauce
```

### **Docker** - *Github* [Manually]
```sh
# Docker & Python 3.8 or higher is required

docker build -t pysauce https://github.com/AkiraNoHikari/pysauce.git

docker run -e BOT_TOKEN=YOUR_BOT_TOKEN -e SAUCENAO_TOKEN=YOUR_SAUCENAO_TOKEN pysauce
```


### **Git Repo** - *Github* [Manually]
```sh
# Python 3.8 or higher is required

git clone https://github.com/AkiraNoHikari/pysauce.git

cd pysauce

# Set `BOT_TOKEN=YOUR_BOT_TOKEN` and `SAUCENAO_TOKEN=YOUR_SAUCENAO_TOKEN` environment variables before running

py main.py
```


## Getting Help
The Pysauce community can be found [here][discord].

## License
Pysauce is distributed under the terms of the [MIT](LICENSE) license.

[logo]: https://cdn.discordapp.com/emojis/585556199924170761.png?size=60
[sauce_nao]: https://saucenao.com/
[discord]: https://discord.gg/Dr7CktccPC
[pysauce_invite]: https://discord.com/api/oauth2/authorize?client_id=922926032917495839&permissions=139586710528&scope=applications.commands%20bot