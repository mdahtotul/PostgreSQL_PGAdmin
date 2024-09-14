1. Install and enable crontab on Ubuntu
```bash
sudo apt update
sudo apt install cron
sudo systemctl enable cron
```
For more details: [How to install crontab (digitalocean)](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804 "How to install crontab")

2. Install python packages
```bash
pip3 install -r requirements.txt
```
3. Give execution permission to files
```bash
chmod +x backup.sh
chmod +x backup_script.py
```
4. Update .env file [if not exists create one] with AWS credentials
```bash
AWS_ACCESS_KEY_ID=***
AWS_SECRET_ACCESS_KEY=***
```
5. Managing Crontabs
```bash
crontab -e
```
Output:

```bash
no crontab for sammy - using an empty one

Select an editor.  To change later, run 'select-editor'.
1. /bin/nano        <---- easiest
2. /usr/bin/vim.basic
3. /usr/bin/vim.tiny
4. /bin/ed

Choose 1-4 [1]: 
```
6. Add this line at the end (This will run backup.sh daily) [NB: Update the the backup.sh and new contrab log file path]
```bash
	0 0 * * * /home/ubuntu/postgresql-pgadmin-docker/backup.sh >> /home/ubuntu/postgresql-pgadmin-docker/crontab.log 2>&1
```
Press CTRL+O then enter to save and CTRL+X to exit

7. To download backup 
```bash
python3 download_backup.py
sudo chown -R 1001:1001 postgresql/
```