"""映射 Agent。"""

from src.models import EpisodeOutline, MappingOutput, RhythmOutput


class Agent4Mapping:
    """这是“映射 Agent”。

    未来负责把 beats / 节奏表映射成分集大纲。
    """

    def run(self, rhythm_output: RhythmOutput) -> MappingOutput:
        """根据节奏表输出最小 mock 分集大纲。"""
        # TODO: 后续可增加节奏点到集数的映射策略。
        return MappingOutput(
            episodes=[
                EpisodeOutline(
                    episode_no=1,
                    summary=f"建立世界观与主冲突：{rhythm_output.beats[0].description}",
                ),
                EpisodeOutline(
                    episode_no=2,
                    summary=f"矛盾升级并进入反转前夜：{rhythm_output.beats[1].description}",
                ),
                EpisodeOutline(
                    episode_no=3,
                    summary=f"反转落地并引出后续空间：{rhythm_output.beats[2].description}",
                ),
            ]
        )
