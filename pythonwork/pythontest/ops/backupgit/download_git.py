import os

os.system('git --version')
# git仓库名
url_f = 'urllist'
# backup_dir 是本地存放备份文件的目录
backup_dir = 'backup'
with open(url_f, mode='r', encoding='utf-8') as f:
    for i in f:
        ret = os.path.join('ssh://git@pj.cecurs.com:10122/data1/redmine/GitRepository', i)
        ret = ret.replace('\.', '').strip()
        print(ret)
        i1 = i.split('.git')[0]
        backup_dir1 = os.path.join(backup_dir, i1)
        backup_dir1 = backup_dir1.replace('\.', '')
        os.system('git clone {} {}'.format(ret, backup_dir1))
# os.system('git clone {} backup/.'.format('ssh://git@pj.cecurs.com:10122/data1/redmine/GitRepository/msg_Push/msg_Push.git'))
# os.system('git clone {} backup/123/'.format('ssh://git@120.132.33.249:10122/casher_platform/CashierPlatform.git'))
