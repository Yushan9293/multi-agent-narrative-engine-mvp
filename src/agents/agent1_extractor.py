"""灵感提取 Agent。"""

from pathlib import Path

from src.models import StoryElements


class Agent1Extractor:
    """这是“灵感提取 Agent”。

    未来负责把用户碎片灵感转成结构化故事要素。
    """

    def __init__(self) -> None:
        self.prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "agent1_extractor.md"

    def run(self, raw_input: str) -> StoryElements:
        """接收用户原始输入，输出最小可用 StoryElements。"""
        _prompt_template = self._load_prompt()
        # TODO: 后续将 raw_input + prompt_template 交给 llm_client 做结构化抽取。
        # 当前使用稳定的简单规则，确保展示时输入变化后仍能得到结构化结果。
        tone = self._extract_tone(raw_input)

        return StoryElements(
            premise=raw_input.strip(),
            characters=self._extract_characters(raw_input),
            conflict=self._extract_conflict(raw_input),
            tone=tone,
        )

    def _load_prompt(self) -> str:
        """读取 prompt 草稿，便于后续替换成真实提示词。"""
        return self.prompt_path.read_text(encoding="utf-8")

    def _extract_characters(self, raw_input: str) -> list[str]:
        """用最简单规则提取角色信息。"""
        characters: list[str] = []

        if "女主" in raw_input:
            characters.append("女主")
        if "男主" in raw_input:
            characters.append("男主")
        if "反派" in raw_input:
            characters.append("反派")

        if not characters:
            characters = ["主角"]

        return characters

    def _extract_conflict(self, raw_input: str) -> str:
        """用固定模板给出清晰可展示的冲突描述。"""
        if "对抗" in raw_input or "冲突" in raw_input:
            return "角色之间存在明显对抗，核心冲突会持续升级。"
        if "秘密" in raw_input or "隐瞒" in raw_input:
            return "人物关系建立在隐瞒与试探之上，真相会推动矛盾爆发。"
        if "改造" in raw_input:
            return "角色在共同推进项目时目标不一致，合作关系不断产生摩擦。"
        return "主角在追求目标的过程中遭遇外部阻力与情感拉扯。"

    def _extract_tone(self, raw_input: str) -> str:
        """提取风格基调。"""
        tone_tags: list[str] = []

        if "都市" in raw_input:
            tone_tags.append("都市")
        if "情感" in raw_input:
            tone_tags.append("情感")
        if "喜剧" in raw_input:
            tone_tags.append("喜剧")
        if "悬疑" in raw_input:
            tone_tags.append("悬疑")
        if "反转" in raw_input:
            tone_tags.append("带反转")
        if "拉扯" in raw_input:
            tone_tags.append("人物关系拉扯感强")

        if not tone_tags:
            tone_tags.append("剧情向")

        return "、".join(tone_tags)
