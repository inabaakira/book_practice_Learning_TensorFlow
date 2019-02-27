# 環境構築
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
