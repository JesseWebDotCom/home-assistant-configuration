# BACKUPS


- [Github](#github)
  - [Setup](#setup)
    - [.gitignore](#gitignore)
  - [Backing up](#backing-up)
- [Snapshots](#snapshots)
  - [Taking a snapshot](#taking-a-snapshot)
  - [Restoring from a snapshot](#restoring-from-a-snapshot)

## Github
Github will help you track code changes as well as backup the shareable parts of your coded configuration.

### Setup

1. Create your `/config/.gitignore` file (see below)
2. SSH into your instance
3. Change directories to your Config share:
```bash
cd /config
```
1. Run (replacing `YOUR_EMAIL` and `YOUR_NAME` appropriately):
```bash
git init
git config user.email "YOUR_EMAIL"
git config user.name "YOUR_NAME"
git add .
git commit -m "Initial Commit"
git push
```

#### .gitignore
The .gitignore file will prevent unwanted files from being sent to Github.  Simply create your `/config/.gitignore` file with the following content:

```bash
# Generic ignores
*.log
*.db
*.db-shm
*.db-wal
*.pyc
._*
__pycache__

# Directory (contents) ignores
.cloud
.storage
custom_components
deps
esphome
node-red
tensorflow
tts
www

# Specific file ignores
secrets.yaml

# ESPHome ignores
esphome/secrets.yaml
esphome/**/
```

### Backing up
> WARNING: Ensure sensitive data is only stored in your */config/secrets.yaml* before backing up files to Github

Whenever you make code changes in your /config directory:

1. SSH into your instance
2. Change directories to your Config share:
```bash
cd /config
``` 
3. Stage the files you changed:  
```bash
git add /path_/to_/your_changed_file.yaml
```
4. Commit with a comment describing the change:  
```bash
git commit -m "Fixed spelling error"
```
5. Push your change to Github:  
```bash
git push
```

## Snapshots
Snapshots will backup your complete instance including your coded configuration, secrets, add-ons, and more.  Take snapshots:  
- Before you make material changes
- Before Home Assistant and add-on upgrades
- Routinely

Snapshots are stored in the */backup* share.

### Taking a snapshot

1. Click Supervisor | Snapshots
2. Enter a snapshot name (ex. 200218)
3. Ensure type is set to full
4. Click Create

> TIP: Move each snapshot off local disk to avoid filling up local storage and to protect against local disk failure.

### Restoring from a snapshot

1. Copy your backed up snapshot to the */backup* share.
2. Click Supervisor | Snapshots
3. Click on your desired snapshot listed under "Available snapshots"
4. Check the desired components to restore
5. If your are rebuilding your instance, click "Wipe & Restore"
6. Otherwise click "Restore selected"
   
***

[Previous](security.md) | [Next](remote-access.md) |
[Table of Contents](../README.md#table-of-contents)