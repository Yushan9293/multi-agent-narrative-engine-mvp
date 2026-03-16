"""节奏 Agent。"""

from src.models import Beat, RhythmOutput, StoryElements, Treatment


class Agent3Rhythm:
    """这是“节奏 Agent”。

    未来负责把选中的梗概转成 beats / 节奏表。
    """

    def run(self, story_elements: StoryElements, selected_treatment: Treatment) -> RhythmOutput:
        """根据已选梗概输出最小 mock 节奏表。"""
        # TODO: 后续基于 story_elements + selected_treatment 生成更细的节奏设计。
        return RhythmOutput(
            beats=[
                Beat(beat_id="beat_1", description=f"开场建立设定：{story_elements.premise}"),
                Beat(beat_id="beat_2", description=f"核心冲突升级：{selected_treatment.summary}"),
                Beat(beat_id="beat_3", description="中后段抛出一次关键反转，推动人物关系变化。"),
            ]
        )
