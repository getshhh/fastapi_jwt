# 🛠 ToDo API (учебный проект)

**🔧 Текущий функционал:**
- ✅ **Авторизация**: JWT-токены (регистрация/вход)
- 📝 **Задачи**: CRUD + фильтрация по статусам
- 👨‍💻 **Админка**: Базовый доступ к пользователям
- 🗃 **База данных**: PostgreSQL + SQLAlchemy

**⚡ Скоро добавлю:**
```diff
+ CI/CD пайплайн (GitHub Actions)
+ Мониторинг: Grafana + Prometheus
+ Безопасность: Bandit сканер
+ Логирование: ELK-стек
+ Docker-контейнеризация

**🚀 Запуск:**
```bash
pip install -r requirements.txt
uvicorn main:app --reload
