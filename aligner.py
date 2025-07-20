# aligner.py

def align_question_paper(raw_text: str) -> str:
    lines = raw_text.strip().split("\n")
    aligned_lines = []

    for line in lines:
        line = line.strip()

        if line.startswith("I.") or "I." in line:
            aligned_lines.append("\nI. सही उत्तर चुनकर लिखें -\t\t1*4=4\n")
        elif line.startswith("ii") or "ii ." in line:
            aligned_lines.append("\nii. दो या तीन वाक्य में उत्तर लिखिए |\t\t2*2=4\n")
        elif line.startswith("iii") or "iii ." in line:
            aligned_lines.append("\niii. आशय स्पष्ट कीजिए |\t\t2*2=4\n")
        elif line.startswith("iv") or "iv ." in line:
            aligned_lines.append("\niv. सोचिए और लिखिए\t\t2*1=2\n")
        elif line.startswith("v") or "v ." in line:
            aligned_lines.append("\nv. निर्देशानुसार लिखिए |\t\t1*6=6\n")
        else:
            aligned_lines.append(line)

    return "\n".join(aligned_lines)
