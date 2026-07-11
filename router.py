import re
def classify_task(task_prompt: str) -> str:
    return "factual_qa"


ROUTER_RULES = {
    "code_debugging": [
        r"\bdebug\w*\b",
        r"\bfix\b.*\bcode\b",
        r"\bfix\b.*\bbug\b",
        r"\berror\b",
        r"\bbuggy\b",
        r"\bsyntax error\b",
        r"\btraceback\b",
        r"\bexception\b",
        r"\bfails\b",
        r"\bdoesn't work\b",
        r"\bresolve\b.*\bissue\b",
        r"\bstack trace\b",
        r"\btypeerror\b",
        r"\bvalueerror\b",
        r"\bnot compiling\b",
        r"\bbug\b",
        r"\bidentify\b.*\bbug\b",
        r"\bcorrected code\b",
        r"\bwrong output\b",
        r"\bincorrect(?:ly)?\b.*\bcode\b",
    ],

    "code_generation": [
        r"\bwrite\b.*\b(?:function|script|class|program|code|query|api|component)\b",
        r"\bimplement\b",
        r"\bgenerate code\b",
        r"\bbuild\b.*\b(?:app|application|interface)\b",
        r"\bcode a\b",
        r"\bcreate a\b.*\b(?:script|app|page)\b",
        r"\bhtml\b",
        r"\bcss\b",
        r"\bsql\b",
    ],

    "math_reasoning": [
        r"\b(?:calculate|solve|equation|derivative|integral|matrix|algebra|arithmetic)\b",
        r"\bmath\b",
        r"\b\d+\b.*\b(?:solve|calculate|how many|total|left)\b",
        r"\bcompute\b",
        r"\bevaluate\b",
        r"\bgeometry\b",
        r"\bstatistics\b",
        r"\bfraction\b",
        r"\bpercentage\b",
        r"\bword problem\b",
        r"\btriangle\b",
        r"\bcircle\b",
        r"\bdiscount\b",
        r"\boriginal price\b",
        r"\b\d+%\b",
        r"\$\d+",
        r"\bgrew?\b",
        r"\bcagr\b",
        r"\bgrowth rate\b",
        r"\bmillion\b",
        r"\bcompound\b",
        r"\bhow much\b",
        r"\bprofit\b",
        r"\brevenue\b",
        r"\bprice\b",
        r"\bcost\b",
    ],

    "summarization": [
        r"\bsummar\w*\b",
        r"\btl;dr\b",
        r"\bcondense\b",
        r"\bshorten\b",
        r"\boverview\b",
        r"\babstract\b",
        r"\bmain points\b",
        r"\bkey takeaways\b",
        r"\bsynthesize\b",
        r"\brecap\b",
        r"\bbrief\b",
        r"\bin a few words\b",
        r"\bwrap up\b",
    ],

    "sentiment_classification": [
        r"\bsentiment\b",
        r"\bpositive\b.*\bnegative\b",
        r"\bclassify\b.*\breview\b",
        r"\bmood\b",
        r"\btone\b",
        r"\bemotion\b",
        r"\bangry\b",
        r"\bhappy\b",
        r"\bsad\b",
        r"\bfeedback\b",
        r"\bopinion\b",
        r"\bstance\b",
        r"\bhow does the author feel\b",
        r"\bclassify\b.*\bsentiment\b",
        r"\bpositive\b.*\bmixed\b",
        r"\boverall sentiment\b",
    ],

    "named_entity_recognition": [
        r"\bextract\b.*\bentit\w*\b",
        r"\bnames\b.*\b(?:people|locations|organizations|dates)\b",
        r"\bner\b",
        r"\bidentify names\b",
        r"\btag entities\b",
        r"\bfind\b.*\bplaces\b",
        r"\bcompanies\b",
        r"\bextract\b.*\b(?:dates|persons|organizations)\b",
        r"\bproper nouns\b",
        r"\bnamed entit\w*\b",
        r"\b(?:person|org|location|date)\b",
    ],

    "logical_reasoning": [
        r"\bif\b.*\bthen\b",
        r"\bpuzzle\b",
        r"\btrue\b.*\bfalse\b",
        r"\blogic(?:al)?\b",
        r"\bdeduction\b",
        r"\bsyllogism\b",
        r"\briddle\b",
        r"\bbrain teaser\b",
        r"\bsequence\b",
        r"\bnext in pattern\b",
        r"\bparadox\b",
        r"\btruth value\b",
        r"\bassume\b",
        r"\bvalid argument\b",
        r"\bclues?\b",
        r"\bdetermine\b.*\beach\b",
        r"\beach\b.*\bdifferent\b",
        r"\bconstraint\b",
        r"\bdoes not\b.*\blive\b",
        r"\bwho owns\b",
    ],
}


def classify_task_keyword(task_prompt: str) -> str:
    prompt_lower = task_prompt.lower()
    scores = {category: 0 for category in ROUTER_RULES}

    for category, patterns in ROUTER_RULES.items():
        for pattern in patterns:
            matches = re.findall(pattern, prompt_lower)
            scores[category] += len(matches)

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        return "factual_qa"

    return best_category