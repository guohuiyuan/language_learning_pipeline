import re
from collections import defaultdict


def extract_words(text):
    """从文本中提取所有单词，包括连字符单词，转换为小写"""
    # 正则表达式修改为包含连字符，匹配由字母、撇号和连字符组成的词
    # \b 表示单词边界，确保我们提取的是完整单词
    # [a-zA-Z'-]+ 匹配一个或多个字母、撇号或连字符
    words = re.findall(r"\b[a-zA-Z'-]+\b", text)

    # 转换为小写并去除可能的前后标点
    words = [word.strip("'-.,;:()[]{}").lower() for word in words]

    # 过滤掉空字符串和仅由连字符/撇号组成的字符串
    return [word for word in words if word and not re.fullmatch(r"['-]+", word)]


def get_stopwords():
    """返回常见的英文停用词列表"""
    return {
        "a",
        "an",
        "the",
        "and",
        "or",
        "but",
        "is",
        "are",
        "was",
        "were",
        "in",
        "on",
        "at",
        "to",
        "of",
        "for",
        "with",
        "as",
        "by",
        "from",
        "i",
        "you",
        "he",
        "she",
        "it",
        "we",
        "they",
        "me",
        "him",
        "her",
        "us",
        "them",
        "my",
        "your",
        "his",
        "its",
        "our",
        "their",
        "this",
        "that",
        "these",
        "those",
        "am",
        "be",
        "been",
        "being",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "will",
        "would",
        "shall",
        "should",
        "may",
        "might",
        "must",
        "can",
        "could",
        "what",
        "which",
        "who",
        "whom",
        "whose",
        "why",
        "how",
        "where",
        "when",
        "all",
        "any",
        "both",
        "each",
        "few",
        "more",
        "most",
        "other",
        "some",
        "such",
        "no",
        "nor",
        "not",
        "only",
        "own",
        "same",
        "so",
        "than",
        "too",
        "very",
        "s",
        "t",
        "don",
        "now",
    }


def remove_stopwords(words, custom_stopwords=None):
    """去除单词列表中的停用词"""
    stopwords = get_stopwords()

    # 添加自定义停用词
    if custom_stopwords:
        stopwords.update(custom_stopwords)

    # 过滤掉停用词
    return [word for word in words if word not in stopwords]


def process_text(text, custom_stopwords=None):
    """处理文本：提取单词并去除停用词"""
    words = extract_words(text)
    filtered_words = remove_stopwords(words, custom_stopwords)
    return filtered_words


def count_words(words):
    """统计单词出现的频率"""
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    # 按频率排序
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)


# 示例用法
if __name__ == "__main__":
    with open("article.txt", "r", encoding="utf-8") as file:
        sample_text = file.read()

    # 处理文本
    processed_words = process_text(sample_text)

    print("提取并过滤后的单词（包含连字符单词）：")
    print(processed_words)

    # 统计单词频率
    word_counts = count_words(processed_words)
    print("\n单词频率统计：")
    for word, count in word_counts:
        print(f"{word}: {count}")

    filtered_words = list(dict.fromkeys(processed_words))
    print(filtered_words)
