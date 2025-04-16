
cli opt
   -d : detach
   -it: interactive,tty
   -h {host}
   --mount type=bind,source={},target={dir}
   -p {host-host}:{cont-cont}

host discovery
- host.docker.internal (from 18.03)
- docker.for.mac.localhost (17.06), docker.for.mac.host.internal (17.12)

- pull
> docker pull {image}:{tag}
- run
> docker run -it --rm --name {name} {image}
- build
> docker build -t image:tag -f Dockerfile .

> docker attach {name}
> docker restart {name}

windows port fowarding
> netsh interface portproxy add v4tov6 listenport=21001 listenaddress=127.0.0.1 connectport=21001 connectaddress=::1
> netsh interface portproxy delete v4tov4 listenport=21002 listenaddress=0.0.0.0

# apple silicon

## docker
> brew install docker

## docker container runtime
### lima
install
> brew install lima

vm create&start
> limactl start --vm-type=vz --rosetta --name docker template://docker
> limactl start --vm-type=qemu --arch=x86_64 --name docker_x64 template://docker

docker context (vm 시작시 나옴)
> docker context create lima-docker --docker "host=unix:///.lima/docker/sock/docker.sock"
> docker context use lima-docker

### colima

install
> brew install colima

vm create&start
> colima start --vm-type=vz --vz-rosetta colima-docker
> colima start --vm-type=qemu --arch=x86_64 colima-docker
