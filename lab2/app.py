import gradio as gr
import random

# ---------------- Naive Search ----------------
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches, comparisons = [], 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)

    return matches, comparisons


# ---------------- KMP ----------------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:

        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


# ---------------- Rabin Karp ----------------
def rabin_karp(text, pattern, q=101):

    n = len(text)
    m = len(pattern)

    d = 256

    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for s in range(n - m + 1):

        if p_hash == t_hash:

            for k in range(m):

                comparisons += 1

                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)

        if s < n - m:

            t_hash = (
                d * (t_hash - ord(text[s]) * h)
                + ord(text[s + m])
            ) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


# ---------------- Compare ----------------
def compare_algorithms(text, pattern):

    if len(pattern) == 0:
        return "Pattern cannot be empty."

    if len(pattern) > len(text):
        return "Pattern length cannot exceed text length."

    n_match, n_comp = naive_search(text, pattern)

    k_match, k_comp = kmp_search(text, pattern)

    r_match, r_comp = rabin_karp(text, pattern)

    output = f"""
### Results

Naive Search

Matches : {n_match}

Comparisons : {n_comp}

------------------------------------

KMP

Matches : {k_match}

Comparisons : {k_comp}

------------------------------------

Rabin-Karp

Matches : {r_match}

Comparisons : {r_comp}
"""

    return output


demo = gr.Interface(

    fn=compare_algorithms,

    inputs=[
        gr.Textbox(
            label="Text",
            value="AABAACAADAABAABA"
        ),
        gr.Textbox(
            label="Pattern",
            value="AABA"
        ),
    ],

    outputs="markdown",

    title="String Pattern Matching Visualizer",

    description="Compare Naive, KMP and Rabin-Karp algorithms."
)

demo.launch()