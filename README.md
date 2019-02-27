# ubuntu-18.04 + cuda-10.1 + tensorflow-gpu の環境構築
## 環境
- NVIDIA GeForce GTX 1060 6GB
- ubuntu-18.04
- cuda-10.1
- tensorflow-gpu
## NVIDIA GPU driver のインストール
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#ubuntu-installation の通りにインストールすればよい。  
https://developer.nvidia.com/cuda-downloads から
- Operating System: Linux
- Architecture: x86_64
- Distribution: Ubuntu
- Version: 18.01
- Installer Type: deb (network)

と選んで  
https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-repo-ubuntu1804_10.1.105-1_amd64.deb  
をダウンロードする。表示される Install Instructions の通り、下記を実行する
- `sudo dpkg -i cuda-repo-ubuntu1804_10.1.105-1_amd64.deb`
- `sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub`
- `sudo apt-get update`
- `sudo apt-get install cuda`

終わったら再起動して動作確認をする。
- reboot
- nvidia-smi

## Docker のインストール
https://docs.docker.com/install/linux/docker-ce/ubuntu/ の通りインストールする。
### docker が既にインストールされている場合は uninstall する。
- `sudo apt-get remove docker docker-engine docker.io containerd runc`
### docker-ce をインストールする
```
sudo apt-get update
sudo apt-get install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable" `
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## nvidia-docker のインストール
https://github.com/NVIDIA/nvidia-docker の通りインストールする。
```
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd
```

## 動作確認
```
docker run --runtime=nvidia -it --rm tensorflow/tensorflow:latest-gpu \
   python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
```

## docker container の起動
```
docker run --runtime=nvidia -it tensorflow/tensorflow:latest-gpu bash
```
