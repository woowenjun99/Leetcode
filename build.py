# Source: https://github.com/RussellDash332/kattis/blob/main/build.py
import os

image_src = 'https://github.com/abrahamcalf/programming-languages-logos/blob/master/src/' # hey this a credit!
image_mapper = {
    'py':   'python',
    'cpp':  'cpp'
}

contents = []
for path, directories, files in os.walk("src"):
    ori_path, path = path, path.split(os.sep)
    hyps = []
    has_py = has_cpp = False
    for file in sorted(files):
        extension = file.split(".")[-1]
        
        # Build last column. 
        # NOTE: URL will convert ? into %3f so we need to manually replace in our script.
        get_image = lambda e,s=24: f'{image_src}{image_mapper[e]}/{image_mapper[e]}_{s}x{s}.png'
        ori_path = ori_path.replace("?", "%3f")
        if extension in image_mapper:
            hyps.append(f"[![{extension}]({get_image(extension)})]({ori_path}/{file})")
        else:
            hyps.append(f"[![{extension}]({get_image(extension)})]()")

        # Build first two columns
        if not has_cpp and extension == "cpp":
            has_cpp = file
        if not has_py and extension == "py":
            has_py = file
        pid = (has_cpp or has_py).split(".")[0]
        url = f"https://leetcode.com/problems/{pid}" 
        if len(path) == 2: path = path[1]
        contents.append([pid, f"|[{path}]({url})| {pid} |{''.join(hyps).replace(' ','%20')}|\n"])

lines = open('README.md', 'r').readlines()[:3]
with open('README.md', 'w+') as f:
    for line in lines: f.write(line)
    # Used to prevent the total problems solved line from being written twice
    f.seek(0)
    f.write("# Leetcode Tracker\n\n")
    f.write("The code has been modified from Russell Dash's build.py of Autokattis for Leetcode\n\n")
    f.write(f'## Total problems solved: {len(contents)}\n\n')
    f.write('|Problem Name|Problem ID|Languages|\n|:---|:---|:---|\n')
    for key, content in sorted(contents): f.write(content)
print("Table generated")
