import os
import subprocess

git_log_command = "git log --decorate=no --no-merges --abbrev-commit --pretty=fuller " \
                  "--date=format:'%Y-%m-%d %H:%M:%S' > raw_data.txt"

content = r"""
\documentclass[margin=1in, 12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{fancyhdr}
\usepackage{amsmath}
\usepackage{tabularx,booktabs}
\usepackage{array}
\usepackage{graphicx}
\usepackage{tcolorbox}
\usepackage{minted}

\newcolumntype{L}{>{$}l<{$}}
\newcolumntype{C}{>{$}c<{$}} 
\newcolumntype{R}{>{$}r<{$}}
\newcommand{\nm}[1]{\textnormal{#1}}

\addtolength{\topmargin}{-.875in}
\addtolength{\textheight}{1.75in}

\pagestyle{fancy}
\fancyhf{}
\rhead{MoM Adventure Language}
\lhead{Log Registry}
\rfoot{Page \thepage}

\begin{document}
    \tcbset{colback=black!5!white,colframe=black!5!white}
    \tcbsetforeverylayer{colframe=gray!50!blue}
"""

block = r"""
    \begin{{tcolorbox}}[title=Commit: {0}, subtitle style={{boxrule=0.4pt,
        colback=yellow!50!red!25!white}}, coltext=black!75!black,
        coltitle=white!75!white]

        \textbf{{Author}}: {1}

        \textbf{{Commit}}: {2}

        \textbf{{Date}}: {3}

        \vspace{{0.2em}}
        \begin{{tcolorbox}}[leftrule=3mm, colback=black!5!white, 
            colframe=black!60!white]
        {4}
        \end{{tcolorbox}}
"""

block_summary = r"""
\begin{{tcolorbox}}[leftrule=3mm, colback=black!5!white, 
            colframe=green!50!gray]
        \textbf{{Summary:}} {0}
\end{{tcolorbox}}
"""

block_issues = r"""
\begin{{tcolorbox}}[leftrule=3mm, colback=black!5!white, 
            colframe=red!60!white]
        \textbf{{Issues:}} {0}
        \end{{tcolorbox}}
"""

blocks = []


def create_block(git_hash, author, commit, date, title, summary, issues):
    blocks.append({
        "git_hash": git_hash,
        "author": author,
        "commit": commit,
        "date": date,
        "title": title,
        "summary": summary,
        "issues": issues
    })


def create_log():
    gen_raw_data = subprocess.Popen([git_log_command], shell=True)
    gen_raw_data.wait()

    with open("raw_data.txt", 'r') as f:
        git_hash = ""
        author = ""
        commit = ""
        date = ""
        in_summary = False
        in_issues = False
        summary = ""
        issues = ""
        title = ""
        first = True
        s_blank = False
        i_blank = False

        for line in f:
            line = line.replace("^", "\^")
            line = line.replace("&", "\&")
            line = line.replace("\\", "\\textbackslash ")
            line = line.replace("[", "{[")
            line = line.replace("]", "]}")
            line = line.replace(">", "$>$")
            line = line.replace("_", "\_")

            if "commit" in line:
                if not first:
                    create_block(git_hash, author, commit, date, title, summary, issues)

                first = False
                git_hash = line[7:].strip()
                author = ""
                commit = ""
                date = ""
                in_summary = False
                in_issues = False
                summary = ""
                issues = ""
                title = ""
                s_blank = False
                i_blank = False

                continue

            if "Author:" in line:
                author = line[8:line.index('<')].strip()
                continue

            if "Commit:" in line:
                commit = line[8:line.index('<')].strip()
                continue

            if "CommitDate: " in line:
                date = line[12:].strip()
                continue

            if "AuthorDate:" in line:
                continue

            if "Summary:" in line:
                in_summary = True
                continue

            if "Issues:" in line:
                in_summary = False
                in_issues = True
                continue

            if in_summary:
                if s_blank:
                    summary += " \n"
                    s_blank = False
                if not len(line.strip()) == 0:
                    summary += line.strip() + " "
                else:
                    s_blank = True

                continue

            if in_issues:
                if i_blank:
                    issues += " \n"
                    i_blank = False
                if not len(line.strip()) == 0:
                    issues += line.strip() + " "
                else:
                    i_blank = True

                continue

            if not in_summary or not in_issues:
                if not len(line.strip()) == 0:
                    title += line.strip() + " "

        create_block(git_hash, author, commit, date, title, summary, issues)

    with open('mom_log.tex', 'w') as f:
        f.write(content)

        for block_dict in blocks:
            text = block.format(block_dict["git_hash"],
                                block_dict["author"],
                                block_dict["commit"],
                                block_dict["date"],
                                block_dict["title"])

            if len(block_dict["summary"]) > 0:
                text += block_summary.format(block_dict["summary"])

            if len(block_dict["issues"]) > 0:
                text += block_issues.format(block_dict["issues"])

            text += "\end{tcolorbox}\n"
            f.write(text)

        f.write("\n\end{document}")

    cmd = ['/Library/TeX/Root/bin/x86_64-darwin/pdflatex', '-shell-escape', 'mom_log.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    if not retcode == 0:
        os.unlink('mom_log.pdf')
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

    os.unlink('mom_log.tex')
    os.unlink('mom_log.log')


create_log()
