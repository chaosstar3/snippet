
CLI
-  -d : detach
-  -it: interactive,tty
-  -h {host}
-  --mount type=bind,source={},target={dir}
-  -p {host-host}:{cont-cont}
```sh
docker pull {image}:{tag}
docker build -t image:tag -f Dockerfile .
docker run -it --rm --name {name} {image}
docker attach {name}
docker restart {name}
```

host discovery
- host.docker.internal (from 18.03)
- docker.for.mac.localhost (17.06), docker.for.mac.host.internal (17.12)

windows port fowarding
```sh
netsh interface portproxy add v4tov6 listenport=21001 listenaddress=127.0.0.1 connectport=21001 connectaddress=::1
netsh interface portproxy delete v4tov4 listenport=21002 listenaddress=0.0.0.0
```
# container runtime

## lima
install
```sh
brew install lima
``` 
### docker
```sh
brew install docker
```
vm create&start
```sh
limactl start --vm-type=vz --rosetta --name docker template://docker
# qemu
# limactl start --vm-type=qemu --arch=x86_64 --name docker_x64 template://docker
```

docker context (vm 시작시 나옴)
```sh
docker context create lima-docker --docker "host=unix:///.lima/docker/sock/docker.sock"
docker context use lima-docker
``` 
## colima
install
```sh
brew install colima
```
vm create&start
```sh
colima start --vm-type=vz --vz-rosetta colima-docker
# qemu
# colima start --vm-type=qemu --arch=x86_64 colima-docker
```