Сценарий 6: Настройка файрвола
Разработайте Ansible Playbook для настройки файрвола на сервере с определенными правилами доступа.

# запуск:

ansible-playbook -i inventory.yml firewal.yml 
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent 
sudo firewall-cmd --reload

# результат: 

<img width="754" alt="Снимок экрана 2024-06-27 в 15 35 28" src="https://github.com/PhilinVeselov/devops/assets/110721135/ce3d69fc-70ae-4af0-bac1-709ac2b6bd48">
