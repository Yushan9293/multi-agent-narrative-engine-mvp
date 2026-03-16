"""定义多 Agent 剧本生成链路中的最小数据结构。"""

from typing import List, Optional

from pydantic import BaseModel, Field


class StoryElements(BaseModel):
    """结构化故事要素，用于承接“灵感提取 Agent”的输出。"""

    premise: str = Field(..., description="故事核心设定")
    characters: List[str] = Field(default_factory=list, description="核心角色")
    conflict: str = Field(..., description="主要冲突")
    tone: str = Field(..., description="风格或情绪基调")


class Treatment(BaseModel):
    """梗概候选。"""

    treatment_id: str = Field(..., description="梗概唯一标识")
    title: str = Field(..., description="梗概标题")
    summary: str = Field(..., description="梗概摘要")


class GeneratorOutput(BaseModel):
    """“梗概生成 Agent”输出的多个梗概方向。"""

    treatments: List[Treatment] = Field(default_factory=list)


class Beat(BaseModel):
    """单个节奏点 / beats 节点。"""

    beat_id: str
    description: str


class RhythmOutput(BaseModel):
    """“节奏 Agent”输出的节奏表。"""

    beats: List[Beat] = Field(default_factory=list)


class EpisodeOutline(BaseModel):
    """单集大纲。"""

    episode_no: int
    summary: str


class MappingOutput(BaseModel):
    """“映射 Agent”输出的分集大纲。"""

    episodes: List[EpisodeOutline] = Field(default_factory=list)


class EpisodeScript(BaseModel):
    """单集剧本正文。"""

    episode_no: int
    content: str


class PipelineState(BaseModel):
    """全局状态：用于串联 Router 与各 Agent 的最小共享数据。"""

    raw_input: str
    story_elements: Optional[StoryElements] = None
    generator_output: Optional[GeneratorOutput] = None
    selected_treatment_id: Optional[str] = None
    rhythm_output: Optional[RhythmOutput] = None
    mapping_output: Optional[MappingOutput] = None
    scripts: List[EpisodeScript] = Field(default_factory=list)

