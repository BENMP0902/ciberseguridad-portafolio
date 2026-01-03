# 📚 Git Cheatsheet Esencial

Guía rápida con los comandos más usados de Git, organizada por flujo de trabajo.

---

## ⚙️ Configuración Inicial

```bash
git config --global user.name "Nombre"
git config --global user.email "email"
```

Ver configuración actual:
```bash
git config --list
```

---

## 📁 Crear o Clonar Repositorios

```bash
git clone URL
git init
```

---

## 🔄 Workflow Diario

```bash
git status
git add .
git add archivo.txt
git commit -m "mensaje descriptivo"
git push origin main
git pull origin main
```

---

## 🔍 Ver Cambios e Historial

```bash
git diff
git diff --staged
git log
git log --oneline
```

---

## ⏪ Deshacer Cambios

```bash
git restore archivo.txt
git restore --staged archivo.txt
git reset --soft HEAD~1
```

---

## 🌐 Remotos

```bash
git remote -v
git remote add origin URL
git remote set-url origin URL
```

---

## ✅ Buenas Prácticas

- Commits pequeños y descriptivos  
- Usar `git status` frecuentemente  
- Evitar `reset --hard` sin respaldo  
