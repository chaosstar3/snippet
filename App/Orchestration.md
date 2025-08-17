
### merge kube config
```sh
KUBECONFIG=FILE1:$HOME/.kube/config kubectl config view --merge --flatten > $HOME/.kube/config.merged
```

[krew](https://krew.sigs.k8s.io/)
> kubectl konfig import -p --save <config_file>
