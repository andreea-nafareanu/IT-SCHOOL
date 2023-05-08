from pathlib import Path
working_dir = Path(".")
print (working_dir)
print(f"Curerent working directory: {working_dir.absolute()}")
script_path = Path(__file__) 
print(f"Script path: {script_path}")
print(f"Script parent directory: {script_path.parent}")

print(f"{script_path} exista? {script_path.exists()}")
start_time_path = script_path.parent / "program_data" / "start_time.txt"

print(start_time_path)

if not start_time_path.parent.exists():
    start_time_path.parent.mkdir()
    # mkdir = make directory
    print(f"Created {start_time_path.parent}")
