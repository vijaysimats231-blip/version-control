# Team Project Repository

## Steps Implemented

### 1. Create GitHub Repository
```bash
git init
git remote add origin https://github.com/username/team-project.git
```

### 2. Set Up Team Repository
Main branch:
```bash
git branch -M main
git push -u origin main
```

### 3. Create Branches for Individual Modules
```bash
git checkout -b frontend
git checkout -b backend
git checkout -b database
```

### 4. Merge Branches with Pull Requests
```bash
git checkout main
git merge frontend
git merge backend
git merge database
```

### 5. Resolve Merge Conflicts
Open conflicted files, edit manually, then:
```bash
git add .
git commit -m "Resolved merge conflicts"
```

### 6. Push Final Code
```bash
git push origin main
```

---

## Workflow Diagram

1. Create Repository
2. Create Branches
3. Develop Modules
4. Commit Changes
5. Create Pull Requests
6. Resolve Conflicts
7. Merge to Main

---

## Team Members
- Developer 1 → Frontend Module
- Developer 2 → Backend Module
- Developer 3 → Database Module
