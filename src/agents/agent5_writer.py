"""撰写 Agent。"""

from src.models import EpisodeScript, MappingOutput, StoryElements


class Agent5Writer:
    """这是“撰写 Agent”。

    未来负责根据单集大纲生成剧本正文。
    """

    def run(self, mapping_output: MappingOutput, story_elements: StoryElements) -> list[EpisodeScript]:
        """根据分集大纲返回最小 mock 剧本正文列表。"""
        # TODO: 后续这里可按单集逐个调用模型生成标准剧本格式。
        scripts: list[EpisodeScript] = []
        for episode in mapping_output.episodes:
            scripts.append(
                EpisodeScript(
                    episode_no=episode.episode_no,
                    content=(
                        f"【第{episode.episode_no}集 mock 剧本】\n"
                        f"基调：{story_elements.tone}\n"
                        f"大纲：{episode.summary}\n"
                        "场景与对白内容待后续 Writer Agent 实现。"
                    ),
                )
            )
        return scripts
