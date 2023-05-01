
## Connect to AWS EC2 instance


#### keep .pem file name as same as you have currently in directory , check with ls command
#### Replace PUBLIC_IP with your instance public ip

```bash

ssh -i "aws.pem"  ubuntu@PUBLIC_IP

```


## Run Commands After Connecting to EC2 instance one by one


```bash
git clone https://github.com/rahul-agrawal-99/Solar-Django

cd Solar-Django

chmod +x cmd.sh

byobu

sudo ./cmd.sh
```


## After that , You can close the terminal and check the website on your browser with your instance public ip As

### http://PUBLIC_IP:8000/
