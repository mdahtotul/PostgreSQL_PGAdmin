# HOST PGADMIN AND PGSQL IN AWS LIGHTSAIL

### Step-1

Create a Instance in Lightsail

### Step-2

Connect and update that instance and install nginx and docker

##### Update ubuntu

    sudo apt update
    sudo apt upgrade
    sudo install nginx

##### Install nginx

    sudo install nginx

##### Install docker

    Follow docker official docs [https://docs.docker.com/engine/install/ubuntu/]

### Step-3

Clone this repo to the instance

```
sudo git clone
https://<username>:<token>@github.com/ChiralX/chiralx_pgsql.git
```

### Step-4

Active root user and

##### Active root user

      sudo -i

##### Add .env file inside the directory copied from github

      cd chiralx_pgsql
      nano .env
      PGADMIN_DEFAULT_EMAIL=your_email
      PGADMIN_DEFAULT_PASSWORD=your_password
      POSTGRES_PASSWORD=your_password
      now save and exit: ctrl+x > y > Enter
      
##### Create pgadmin4 directory in the directory copied from github and Add config_local.py file in the pgadmin4
      sudo mkdir -p ./pgadmin4
      nano config_local.py
      SESSION_DB_PATH = '/tmp/pgadmin_sessions'
      now save and exit: ctrl+x > y > Enter

##### ensure read/write permission of pgadmin4 for pgadmin to use
      sudo chown -R 5050:5050 ./pgadmin4
      sudo chmod -R 700 ./pgadmin4



### Step-5

Run docker build command to start the app

```
docker compose up -d --build
```

### Step-6

Networking tab of lightsail instance

      Go to the networking tab do not delete any rules but add two rules in IPv4 Firewall

##### 1st Rule

      Application - Custom
      Port - 443

##### 2nd Rule

      Application - Custom
      Port - 5050

      Now go to the http://public_ip_address:5050

🎉 Congratulation You've hosted pgadmin and postgresql database in aws lightsail.
