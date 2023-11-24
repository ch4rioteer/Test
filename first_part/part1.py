#Создать функцию на python, которая будет принимать на вход
#список репозиториев, скачав каждую ветку в отдельную папку,
#если уже были скачены, то обновить до последней версии, создать
#внутри файлик с текущей датой и временем, именем репозитория и веткой,
#в которой находится, залить этот файлик в репозиторий.

from datetime import datetime
import os
import git
import  logging 

#ввод ссылок, пока не будет введена пустая строка
logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'part1.py.log'), filemode="w", level=logging.INFO)

print('Введите ссылки (введите пустую строку для завершения ввода):')

repo_list = []

while repo_url := input():
    repo_list.append(repo_url)

logging.info(f"Список ссылок:{repo_list}")

def clone_update_repo(repo_url):
    #очистка от "шелухи"
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    repo_path = os.path.join(os.path.dirname(__file__), repo_name)
    logging.info(f"Обработка {repo_url}, задействуется папка {repo_path}")
    #загрузка или обновление репозиториев
    if not os.path.exists(repo_path):
        print('Загрузка', repo_name)
        logging.info("Загрузка")
        repo = git.Repo.clone_from(repo_url, repo_path)
    else:
        print('Обновление', repo_name)
        repo = git.Repo(repo_path)
        repo.remotes.origin.pull()
        logging.info("Обновление")
        #создание файла с измениениями
        file_name = f"{repo_name}_changes.txt"
        file_path = os.path.join(repo_path, file_name)

        with open(file_path, 'a') as file:
            file.write(f"Репозиторий {repo_name} был обновлён {datetime.now()} \n")
        logging.info(f"Фиксация обновления в {file_path} в {datetime.now()}")
        
for repo_url in repo_list:
    clone_update_repo(repo_url)
