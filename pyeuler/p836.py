#!/usr/bin/env python3

p836_txt = """
<p>Let $A$ be an <b>affine plane</b> over a <b>radically integral local field</b> $F$ with residual characteristic $p$.</p>

<p>We consider an <b>open oriented line section</b> $U$ of $A$ with normalized Haar measure $m$.</p>

<p>Define $f(m, p)$ as the maximal possible discriminant of the <b>jacobian</b> associated to the <b>orthogonal kernel embedding</b> of $U$ <span style="white-space:nowrap;">into $A$.</span></p>

<p>Find $f(20230401, 57)$. Give as your answer the concatenation of the first letters of each bolded word.</p>
"""

def p836(p836_txt):
    return ''.join(x[0] for y in [x[:x.index('</b>')] for x in p836_txt.split('<b>') if '</b>' in x] for x in y.split(' '))
print(p836(p836_txt))