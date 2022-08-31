from pathlib import Path

# Absolute path = c\Program files\Microsf**
# Relative path

#path = Path("ecommerce")
#print(path.exists())
#path.mkdir()   path.rmdir()

#example finding files
path = Path()

for file in path.glob('*.py'):
    print(file)