"""梗概生成 Agent。"""

from pathlib import Path

from src.models import GeneratorOutput, StoryElements, Treatment


class Agent2Generator:
    """这是“梗概生成 Agent”。

    未来负责基于结构化要素生成多个梗概方向。
    """

    def __init__(self) -> None:
        self.prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "agent2_generator.md"

    def run(self, story_elements: StoryElements) -> GeneratorOutput:
        """基于 StoryElements 输出多个 treatment 候选。"""
        _prompt_template = self._load_prompt()
        # TODO: 后续结合 story_elements 与 prompt_template 调用 llm_client。
        premise = story_elements.premise
        conflict = story_elements.conflict

        return GeneratorOutput(
            treatments=[
                Treatment(
                    treatment_id="treatment_1",
                    title="旧剧场重生",
                    summary=(
                        f"围绕“{premise}”，男女主在老剧场改造中从互相否定到逐步理解，"
                        f"主线聚焦于 {conflict}"
                    ),
                ),
                Treatment(
                    treatment_id="treatment_2",
                    title="合作关系失控",
                    summary=(
                        "女主把剧场当作最后的创作阵地，男主则把项目视作资本试验，"
                        "两人在合作过程中不断试探彼此底线。"
                    ),
                ),
                Treatment(
                    treatment_id="treatment_3",
                    title="反转式治愈爱情",
                    summary=(
                        "外表冷漠的投资人其实暗中守护剧场，而女主在追查真相的过程中，"
                        "重新找回表达欲与爱的能力。"
                    ),
                ),
            ]
        )

    def _load_prompt(self) -> str:
        """读取 prompt 草稿。"""
        return self.prompt_path.read_text(encoding="utf-8")
