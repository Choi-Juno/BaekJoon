import os
import shutil
from pathlib import Path


def create_problem_dirs():
    for i in range(1, 35):  # 1000 ~ 34000
        problem_dir = Path(f"problems/{i*1000:05d}")
        problem_dir.mkdir(parents=True, exist_ok=True)


def get_problem_dir(filename):
    try:
        number = int("".join(filter(str.isdigit, filename)))
        dir_number = (number // 1000) * 1000
        if number % 1000 == 0:
            dir_number = number
        if dir_number < 1000:
            dir_number = 1000
        return f"problems/{dir_number:05d}"
    except ValueError:
        return None


def organize_files():
    today_path = Path("today")
    if not today_path.exists():
        print("today 폴더가 존재하지 않습니다.")
        return
    for py_file in today_path.glob("*.py"):
        problem_dir = get_problem_dir(py_file.name)
        if problem_dir:
            destination = Path(problem_dir) / py_file.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            print(f"Moving {py_file} to {destination}")
            shutil.copy2(py_file, destination)


def check_and_cleanup():
    today_path = Path("today")
    problems_path = Path("problems")
    today_files = {f.name for f in today_path.glob("*.py")}
    problems_files = set()
    for py_file in problems_path.rglob("*.py"):
        problems_files.add(py_file.name)
    missing = today_files - problems_files
    if missing:
        print(f"누락된 파일이 있습니다: {sorted(missing)}")
    else:
        print("모든 파일이 정상적으로 이동되었습니다. today 폴더를 정리합니다.")
        for f in today_path.glob("*.py"):
            f.unlink()
        print("today 폴더가 비워졌습니다.")


if __name__ == "__main__":
    create_problem_dirs()
    organize_files()
    check_and_cleanup()
    print("작업이 완료되었습니다.")
