# Git & Python 

**Duration:** ~1 week

## Prerequisites
- Python 3.8+ installed
- Git installed
- GitHub account created

---

## Exercise 1: Setup

### Tasks
1. **Work on this repository** to your own GitHub account

2. **Create and activate a Python virtual environment (work there)**

3. **Install dependencies and run the code**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .gitignore file** - figure out what shouldn't be committed to git

---

## Exercise 2: Branching & Bug Fixes

### Tasks
The calculator code has issues. Your job:

1. **Create a new branch** for your work
   
2. **Fix the problems** in `src/calculator.py`
   - Run the tests to identify what's broken
   - Make the necessary changes
   
3. **Commit your changes** with clear commit messages

4. **Push your branch** to GitHub

5. **Create a Pull Request** and merge it into your main branch

---

## Exercise 3: Merge Conflicts

### Tasks
There are two feature branches that need to be integrated:
- `feature/add-statistics`
- `feature/improved-ui`

Your job:
1. **Switch to main** and make sure it's up to date

2. **Merge both branches** into main
   - One should merge smoothly
   - One will cause a conflict

3. **Resolve any conflicts** that arise

4. **Complete the merge** and push to GitHub

---

## Exercise 4: Independent Feature

### Tasks
Now add something new to the calculator.

Ideas:
- Calculation history
- Scientific functions (trig, logarithms, etc.)
- Interactive menu
- Something else you think would be useful

Requirements:
- Create a new branch for your work
- Write one test for your feature
- Use proper Git workflow (commit, push, PR)
- Document what you added


