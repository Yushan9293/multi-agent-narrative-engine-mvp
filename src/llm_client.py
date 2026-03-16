"""模型调用占位接口。"""

from typing import Any, Dict


class BaseLLMClient:
    """最小 LLM Client 占位类。

    后续这里可以接入火山 API、OpenAI API 或其他模型服务。
    当前仅提供统一接口，避免上层逻辑直接耦合具体 SDK。
    """

    def generate_text(self, prompt: str) -> str:
        """生成文本结果。

        TODO: 接入真实模型调用。
        """
        return f"[mock_text] {prompt[:60]}"

    def generate_json(self, prompt: str) -> Dict[str, Any]:
        """生成 JSON 结果。

        TODO: 接入真实模型调用，并增加结构化校验。
        """
        return {"mock": True, "prompt_preview": prompt[:60]}
