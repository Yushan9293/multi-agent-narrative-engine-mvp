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
        # 当前使用稳定的简单规则，优先展示“灵感拆解”而不是“梗概生成”。
        fragments = self._extract_fragments(raw_input)
        characters = self._extract_characters(raw_input)
        tone = self._extract_tone(raw_input)
        character_drives = self._extract_character_drives(raw_input, characters)
        antagonist_force = self._extract_antagonist_force(raw_input)
        high_stakes = self._extract_high_stakes(raw_input)
        world_rules = self._extract_world_rules(raw_input)
        thematic_premise = self._extract_thematic_premise(raw_input)
        opening_hook = self._extract_opening_hook(raw_input)
        missing_elements = self._extract_missing_elements(raw_input)

        return StoryElements(
            raw_fragments=fragments,
            character_drives=character_drives,
            antagonist_force=antagonist_force,
            high_stakes=high_stakes,
            world_rules=world_rules,
            thematic_premise=thematic_premise,
            opening_hook=opening_hook,
            missing_elements=missing_elements,
            premise="围绕老剧场改造展开的一组都市情感叙事资产。",
            characters=characters,
            conflict=antagonist_force,
            tone=tone,
        )

    def _load_prompt(self) -> str:
        """读取 prompt 草稿，便于后续替换成真实提示词。"""
        return self.prompt_path.read_text(encoding="utf-8")

    def _extract_fragments(self, raw_input: str) -> list[str]:
        """提取可展示的原始灵感碎片。"""
        fragments: list[str] = []
        candidates = ["都市情感短剧", "女主", "男主", "老剧场", "改造", "反转", "拉扯"]
        for item in candidates:
            if item in raw_input:
                fragments.append(item)
        return fragments or [raw_input.strip()]

    def _extract_characters(self, raw_input: str) -> list[str]:
        """用最简单规则提取角色信息。"""
        characters: list[str] = []

        if "失业编剧" in raw_input:
            characters.append("失业编剧女主")
        elif "女主" in raw_input:
            characters.append("女主")

        if "投资人" in raw_input:
            characters.append("冷面投资人男主")
        elif "男主" in raw_input:
            characters.append("男主")

        if "反派" in raw_input:
            characters.append("反派")

        if not characters:
            characters = ["主角"]

        return characters

    def _extract_character_drives(self, raw_input: str, characters: list[str]) -> str:
        """提炼外在目标与内在缺陷。"""
        if "改造" in raw_input and "老剧场" in raw_input:
            return (
                f"{'、'.join(characters)}围绕老剧场改造被迫合作。"
                "女主的外在目标是保住创作阵地，内在缺陷是过度执着理想；"
                "男主的外在目标是推进项目落地，内在缺陷是习惯压抑真实情感。"
            )
        return "主角有明确追求，但各自带着尚未解决的性格缺口。"

    def _extract_antagonist_force(self, raw_input: str) -> str:
        """提炼核心反派力量。"""
        if "改造" in raw_input:
            return "商业改造目标与理想主义创作诉求之间的结构性冲突。"
        if "秘密" in raw_input or "隐瞒" in raw_input:
            return "建立在隐瞒之上的关系与迟早会暴露的真相。"
        return "主角目标推进过程中持续出现的外部阻力。"

    def _extract_high_stakes(self, raw_input: str) -> str:
        """提炼核心赌注。"""
        if "老剧场" in raw_input:
            return "如果合作失败，老剧场将失去最后的生存机会，主角也会错失各自的人生转机。"
        return "如果失败，主角将失去重要的人际关系与行动机会。"

    def _extract_world_rules(self, raw_input: str) -> str:
        """提炼关键设定与道具。"""
        if "都市" in raw_input and "老剧场" in raw_input:
            return "都市现实背景，核心场域是等待改造的老剧场，关键事项围绕剧场改造项目展开。"
        if "都市" in raw_input:
            return "都市现实背景，人物关系受现实资源与情感拉扯共同影响。"
        return "故事发生在一个具有明确规则约束的现实场景中。"

    def _extract_thematic_premise(self, raw_input: str) -> str:
        """提炼核心困境主题。"""
        if "情感" in raw_input and "拉扯" in raw_input:
            return "当理想、利益与情感同时发生碰撞时，人是否还能守住真正珍视的东西。"
        return "人物在欲望与代价之间作出选择，并承受其后果。"

    def _extract_opening_hook(self, raw_input: str) -> str:
        """提炼黄金开局点。"""
        if "老剧场" in raw_input and "投资人" in raw_input:
            return "女主守着即将停摆的老剧场做最后挣扎时，男主带着强势改造方案出现。"
        return "主角在一次高压事件中首次相遇，核心矛盾当场被抛出。"

    def _extract_missing_elements(self, raw_input: str) -> list[str]:
        """列出当前灵感中仍不够明确的要素。"""
        missing_elements: list[str] = []

        if "反派" not in raw_input and "阻力" not in raw_input:
            missing_elements.append("更具体的反派力量或外部阻力")
        if "赌注" not in raw_input and "代价" not in raw_input:
            missing_elements.append("失败后的更极致代价")
        if "开场" not in raw_input and "开局" not in raw_input:
            missing_elements.append("更具画面感的开场事件")

        return missing_elements

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
