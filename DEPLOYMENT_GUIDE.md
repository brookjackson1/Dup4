# F1 Racing App - Deployment Guide

## Current Status

### ✅ GitHub - COMPLETE
- All code committed and pushed to: https://github.com/brookjackson1/Dup4
- Latest commit includes:
  - Professional racing-themed homepage
  - Complete database schema with branding columns
  - Full seed data for 10 teams and 20 drivers
  - All static images for pages
  - Utility scripts for database management

### 📦 Project Files Ready for Deployment

**Application Files:**
- `app.py` - Main Flask application
- `app/` - Application package with blueprints
- `app/templates/` - All HTML templates
- `app/static/` - Static files (images, CSS, JS)
- `.env` - Environment variables (NOT in git - configure separately)

**Database Files:**
- `database/schema.sql` - Complete database schema
- `database/seed_data_complete.sql` - Full seed data with 10 teams, 20 drivers, photos, branding

**Heroku Files:**
- `Procfile` - Heroku process file (web: gunicorn app:app)
- `requirements.txt` - Python dependencies

## Heroku Deployment Steps

### Step 1: Install Heroku CLI

**Windows:**
```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
# Or use chocolatey:
choco install heroku-cli
```

**Verify installation:**
```bash
heroku --version
```

### Step 2: Login to Heroku

```bash
heroku login
```

### Step 3: Create Heroku App

```bash
cd C:\Users\brook\OneDrive\Desktop\marshall\Dup4
heroku create your-f1-racing-app
# Or if app already exists:
heroku git:remote -a your-existing-app-name
```

### Step 4: Add MySQL Database

Heroku doesn't have built-in MySQL. You have two options:

**Option A: Use ClearDB MySQL (Free tier available)**
```bash
heroku addons:create cleardb:ignite
```

**Option B: Continue using AWS RDS MySQL**
- Keep your current AWS RDS database
- Configure environment variables (Step 5)

### Step 5: Configure Environment Variables

```bash
# Set database credentials
heroku config:set DB_HOST=your_db_host
heroku config:set DB_USERNAME=your_db_username
heroku config:set DB_PASSWORD=your_db_password
heroku config:set DB_DATABASE=your_db_name
heroku config:set DB_PORT=3306

# Set Flask secret key
heroku config:set SECRET_KEY=your-secret-key-here

# Verify configuration
heroku config
```

### Step 6: Deploy to Heroku

```bash
# Make sure all changes are committed
git status

# Push to Heroku
git push heroku master

# If you're on a different branch:
git push heroku main:master
```

### Step 7: Initialize Database

If using a new database, run the schema and seed data:

```bash
# Option A: Use Heroku MySQL CLI
heroku run mysql -h HOST -u USERNAME -p DATABASE < database/schema.sql

# Option B: Use your database GUI tool (MySQL Workbench, etc.)
# Connect to your database and run:
# 1. database/schema.sql
# 2. database/seed_data_complete.sql
```

### Step 8: Open Your App

```bash
heroku open
```

### Step 9: View Logs (if needed)

```bash
heroku logs --tail
```

## Database Setup Options

### Option 1: Fresh Database Setup
1. Run `database/schema.sql` - Creates tables
2. Run `database/seed_data_complete.sql` - Adds all 10 teams and 20 drivers

### Option 2: Current AWS RDS Database
- Your database already has all data
- Just configure environment variables in Heroku (Step 5)
- Deploy and it will connect to existing database

## Environment Variables Required

```env
DB_HOST=your_database_host
DB_USERNAME=your_database_username
DB_PASSWORD=your_database_password
DB_DATABASE=your_database_name
DB_PORT=3306
SECRET_KEY=your_flask_secret_key
```

## Post-Deployment Checklist

- [ ] App loads successfully
- [ ] Homepage displays with F1 logo and racing theme
- [ ] Teams page shows all 10 teams with logos and colors
- [ ] Drivers page shows all 20 drivers with photos
- [ ] CRUD operations work (add, edit, delete)
- [ ] Static pages load (History, Championships, Circuits, About)
- [ ] Images display correctly
- [ ] Database CASCADE operations work correctly

## Troubleshooting

### App won't start
```bash
heroku logs --tail
# Check for:
# - Database connection errors
# - Missing environment variables
# - Import errors
```

### Database connection failed
```bash
# Verify config
heroku config

# Test database connection
heroku run python -c "import pymysql; print('PyMySQL installed')"
```

### Static files not loading
- Heroku serves static files through Flask
- All static files are in `app/static/`
- Templates use `url_for('static', filename='...')`

## Current Database Status

Your AWS RDS database currently has:
- ✅ 10 F1 teams (including Ferrari)
- ✅ 20 drivers with photos (including Lewis Hamilton and Charles Leclerc)
- ✅ Team branding (colors, logos, car images)
- ✅ All CASCADE relationships configured

## Quick Deploy Command Reference

```bash
# One-time setup
heroku login
heroku create f1-racing-app
heroku config:set DB_HOST=xxx DB_USERNAME=xxx DB_PASSWORD=xxx DB_DATABASE=xxx DB_PORT=3306

# Regular deployment
git add .
git commit -m "Your commit message"
git push origin master
git push heroku master

# View app
heroku open

# Monitor
heroku logs --tail
```

## Support Resources

- Heroku Documentation: https://devcenter.heroku.com/
- Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
- ClearDB MySQL: https://devcenter.heroku.com/articles/cleardb
- Flask on Heroku: https://devcenter.heroku.com/articles/getting-started-with-python
