import json
import os


def load_json_file(file_path):
    """加载JSON文件"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return None
    except json.JSONDecodeError:
        print(f"错误：文件 {file_path} 不是有效的JSON格式")
        return None


def merge_phrases_and_words(phrases_data, words_data):
    """整合短语和单词数据为欧路词典卡片格式"""
    eudic_cards = []

    # 处理短语数据
    if phrases_data and "output" in phrases_data:
        for phrase_item in phrases_data["output"]:
            card = {
                "单词": phrase_item.get("短语", ""),
                "单词释义": create_phrase_definition(phrase_item),
            }
            eudic_cards.append(card)

    # 处理单词数据
    if words_data and "output" in words_data:
        for word_item in words_data["output"]:
            card = {
                "单词": word_item.get("单词", ""),
                "单词释义": create_word_definition(word_item),
            }
            eudic_cards.append(card)

    return eudic_cards


def create_phrase_definition(phrase_item):
    """创建短语的释义内容 - 动态遍历所有字段"""
    definition_parts = []

    # 遍历所有字段，排除"短语"字段（因为"短语"字段用作单词）
    for key, value in phrase_item.items():
        if key != "短语" and value and value != "无":  # 排除空值和"无"
            definition_parts.append(f"{key}: {value}")

    return "    #    ".join(definition_parts)


def create_word_definition(word_item):
    """创建单词的释义内容 - 动态遍历所有字段"""
    definition_parts = []

    # 遍历所有字段，排除"单词"字段（因为"单词"字段用作单词）
    for key, value in word_item.items():
        if key != "单词" and value:  # 排除空值
            definition_parts.append(f"{key}: {value}")

    return "    #    ".join(definition_parts)


def main():
    # 文件路径
    phrases_file = "input1.json"
    words_file = "input2.json"
    output_file = "eudic_cards_output.json"

    # 加载数据
    print("正在加载短语数据...")
    phrases_data = load_json_file(phrases_file)

    print("正在加载单词数据...")
    words_data = load_json_file(words_file)

    if not phrases_data or not words_data:
        print("数据加载失败，请检查文件路径和格式")
        return

    # 整合数据
    print("正在整合数据为欧路词典卡片格式...")
    eudic_cards = merge_phrases_and_words(phrases_data, words_data)

    # 输出结果
    print(f"共生成 {len(eudic_cards)} 张卡片")

    # 保存到文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(eudic_cards, f, ensure_ascii=False, indent=2)

    print(f"结果已保存到 {output_file}")

    # 显示前几个卡片作为示例
    print("\n前5张卡片示例:")
    for i, card in enumerate(eudic_cards[:5]):
        print(f"\n--- 卡片 {i+1} ---")
        print(f"单词: {card['单词']}")
        print(f"单词释义:\n{card['单词释义']}")
        print("-" * 40)


if __name__ == "__main__":
    main()
