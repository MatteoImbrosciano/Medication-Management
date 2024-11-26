import os
import py_compile

def check_syntax():
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    py_compile.compile(file_path, doraise=True)
                    print(f"✔ Syntax OK: {file_path}")
                except py_compile.PyCompileError as e:
                    print(f"✘ Syntax Error: {file_path}")
                    print(e)

if __name__ == "__main__":
    check_syntax()
