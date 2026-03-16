"""Router：总调度器 / orchestration layer，不负责创作内容本身。"""

from src.agents.agent1_extractor import Agent1Extractor
from src.agents.agent2_generator import Agent2Generator
from src.agents.agent3_rhythm import Agent3Rhythm
from src.agents.agent4_mapping import Agent4Mapping
from src.agents.agent5_writer import Agent5Writer
from src.models import PipelineState, Treatment


class Router:
    """编排多 Agent 主链路，并负责全局状态流转。"""

    def __init__(self) -> None:
        """注册各个 Agent。

        Router 只负责调度，不承担具体创作生成逻辑。
        """
        self.agent1 = Agent1Extractor()
        self.agent2 = Agent2Generator()
        self.agent3 = Agent3Rhythm()
        self.agent4 = Agent4Mapping()
        self.agent5 = Agent5Writer()

    def run_agent1_only(self, raw_input: str) -> PipelineState:
        """只运行到 Agent1，用于最小演示链路。"""
        state = PipelineState(raw_input=raw_input)
        state.story_elements = self.agent1.run(state.raw_input)
        return state

    def run(self, raw_input: str) -> PipelineState:
        """执行最小可见的完整主链路。"""
        state = PipelineState(raw_input=raw_input)

        # Step 1: 将用户原始灵感整理为结构化故事要素。
        state.story_elements = self.agent1.run(state.raw_input)

        # Step 2: 基于结构化要素生成多个梗概候选。
        state.generator_output = self.agent2.run(state.story_elements)

        # Step 3: MVP 默认选择第一个梗概，后续可替换为评分或人工选择。
        selected_treatment = self._select_treatment(state)
        state.selected_treatment_id = selected_treatment.treatment_id

        # Step 4: 将选中的梗概扩展为 beats / 节奏表。
        state.rhythm_output = self.agent3.run(state.story_elements, selected_treatment)

        # Step 5: 将节奏表映射为分集大纲。
        state.mapping_output = self.agent4.run(state.rhythm_output)

        # Step 6: 基于分集大纲和故事要素生成剧本正文。
        state.scripts = self.agent5.run(state.mapping_output, state.story_elements)

        return state

    def _select_treatment(self, state: PipelineState) -> Treatment:
        """默认选择第一个 treatment。"""
        if not state.generator_output or not state.generator_output.treatments:
            raise ValueError("generator_output is empty, cannot select treatment.")
        return state.generator_output.treatments[0]
